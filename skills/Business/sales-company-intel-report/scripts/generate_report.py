#!/usr/bin/env python3
"""Render sales-company-intel-report's data.json into a self-contained HTML report.

This script only converts already-researched, structured data into a formatted
report (Jinja2 + Chart.js + an SVG decision-chain diagram). It does NOT search the
web, does NOT invent missing figures, and does NOT validate the truthfulness of the
data — that judgment call happens earlier, when the data.json is authored (see
references/report-structure.md). It also does not add any product/competitive/
pricing content — the report's scope is the customer's objective situation only.

Usage:
    python generate_report.py --data data.json --output report.html
"""
from __future__ import annotations

import argparse
import json
import logging
import re
from pathlib import Path
from typing import Any

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    from markupsafe import Markup, escape
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "jinja2 is required: pip install jinja2 --break-system-packages"
    ) from exc

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = SCRIPT_DIR.parent / "assets"
TEMPLATE_NAME = "report_template.html"

CONFIDENCE_CLASS_MAP = {"已证实": "fact", "推断": "infer", "待核实": "todo"}
CONFIDENCE_LABEL_MAP = {"fact": "已证实", "infer": "推断", "todo": "待核实"}

STANCE_VALUES = {"supportive", "resistant", "neutral", "unknown"}

# data.json field names must never surface in the reader-facing prose. Anything the
# researcher wrote using an internal key gets rewritten to its Chinese equivalent.
FIELD_ALIASES = {
    "vendor_summary": "供应商汇总",
    "it_bidding": "IT招投标",
    "open_questions": "待核实清单",
    "executive_summary": "执行摘要",
    "decision_chain": "决策链",
    "company_basics": "公司概况",
    "it_investment": "IT投入",
    "it_landscape": "IT现状",
    "customer_swot": "客户侧SWOT",
    "core_pain_points": "核心痛点",
    "business_architecture": "业务与IT架构",
    "five_year_development": "近5年业务发展",
    "profile_facts": "公司基本信息",
    "source_refs": "来源编号",
    "trend_analysis": "采购趋势分析",
}

# A trend paragraph is authored as "小标题：…。小标题：…" — split it so the report
# can set each strand as its own labelled row instead of one undifferentiated block.
TREND_SPLIT_RE = re.compile(r"(?<=。)(?=[^。；，]{2,10}：)")
TREND_LABEL_RE = re.compile(r"^([^。；，]{2,10})：(.+)$", re.S)

# Decision-chain diagram layout constants (SVG px)
NODE_W, NODE_H = 220, 68
NODE_GAP_X, LEVEL_GAP_Y = 26, 46
MARGIN_X, MARGIN_Y = 20, 20
SUBLABEL_CHARS_PER_LINE = 16


def load_data(data_path: Path) -> dict[str, Any]:
    if not data_path.exists():
        raise FileNotFoundError(f"data file not found: {data_path}")
    with data_path.open("r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSON in {data_path}: {exc}") from exc
    return data


def confidence_class(value: str | None) -> str:
    return CONFIDENCE_CLASS_MAP.get((value or "").strip(), "unknown")


def render_badge(confidence: str | None) -> Markup:
    """Jinja global: render a confidence pill. Returns '' when confidence is empty."""
    if not confidence:
        return Markup("")
    cls = confidence_class(confidence)
    label = CONFIDENCE_LABEL_MAP.get(cls, str(confidence))
    return Markup(
        f'<span class="badge badge-{cls}"><span class="d"></span>{escape(label)}</span>'
    )


def render_src(source_refs: list[str] | None) -> Markup:
    """Jinja global: render superscript source-reference links, e.g. ⁽ˢ¹ˢ²⁾."""
    if not source_refs:
        return Markup("")
    links = ", ".join(
        f'<a href="#src-{escape(ref)}">{escape(ref)}</a>' for ref in source_refs
    )
    return Markup(f'<sup class="src">[{links}]</sup>')


def annotate_confidence(items: list[dict] | None, key: str = "confidence") -> list[dict]:
    for item in items or []:
        if isinstance(item, dict) and key in item:
            item["confidence_class"] = confidence_class(item.get(key))
    return items or []


def build_financials_chart(financials: dict | None) -> dict | None:
    if not financials:
        return None
    years = financials.get("years") or []
    revenue = financials.get("revenue") or []
    net_profit = financials.get("net_profit") or []
    has_data = any(v is not None for v in revenue) or any(v is not None for v in net_profit)
    if not years or not has_data:
        return None
    return {"years": years, "revenue": revenue, "net_profit": net_profit, "unit": financials.get("revenue_unit", "")}


def build_vendor_chart(vendor_summary: list[dict] | None) -> dict | None:
    entries = [v for v in (vendor_summary or []) if v.get("total_amount")]
    if not entries:
        return None
    entries = sorted(entries, key=lambda v: v["total_amount"], reverse=True)
    return {"labels": [v["vendor"] for v in entries], "amounts": [v["total_amount"] for v in entries]}


def build_bidding_timeline_chart(records: list[dict] | None) -> dict | None:
    dated = [r for r in (records or []) if r.get("date") and r.get("amount")]
    if not dated:
        return None
    dated = sorted(dated, key=lambda r: r["date"])
    return {
        "labels": [f"{r['date']} {r['project_name']}" for r in dated],
        "amounts": [r["amount"] for r in dated],
    }


def _wrap_sublabel(text: str, max_lines: int = 2) -> list[str]:
    """Best-effort character-count wrap for CJK/mixed text inside an SVG node box."""
    if not text:
        return []
    lines: list[str] = []
    remaining = text
    while remaining and len(lines) < max_lines:
        if len(remaining) <= SUBLABEL_CHARS_PER_LINE or len(lines) == max_lines - 1:
            lines.append(remaining[: SUBLABEL_CHARS_PER_LINE - 1] + ("…" if len(remaining) > SUBLABEL_CHARS_PER_LINE else ""))
            remaining = ""
        else:
            lines.append(remaining[:SUBLABEL_CHARS_PER_LINE])
            remaining = remaining[SUBLABEL_CHARS_PER_LINE:]
    return lines


def build_decision_diagram(nodes: list[dict] | None, edges: list[dict] | None) -> dict | None:
    """Compute an SVG layout for the decision-chain diagram: nodes grouped into rows by
    `level`, evenly spaced and centered per row, with straight connector lines for edges."""
    nodes = nodes or []
    if not nodes:
        return None

    by_level: dict[int, list[dict]] = {}
    for n in nodes:
        level = n.get("level")
        if level is None:
            continue
        by_level.setdefault(int(level), []).append(n)
    if not by_level:
        return None

    levels_sorted = sorted(by_level)
    max_row_count = max(len(v) for v in by_level.values())
    row_width = max_row_count * NODE_W + (max_row_count - 1) * NODE_GAP_X
    total_width = row_width + 2 * MARGIN_X
    total_height = len(levels_sorted) * NODE_H + (len(levels_sorted) - 1) * LEVEL_GAP_Y + 2 * MARGIN_Y

    positioned: dict[str, dict] = {}
    for row_idx, level in enumerate(levels_sorted):
        row_nodes = by_level[level]
        n = len(row_nodes)
        row_span = n * NODE_W + (n - 1) * NODE_GAP_X
        start_x = MARGIN_X + (row_width - row_span) / 2
        y = MARGIN_Y + row_idx * (NODE_H + LEVEL_GAP_Y)
        for i, node in enumerate(row_nodes):
            x = start_x + i * (NODE_W + NODE_GAP_X)
            stance = node.get("stance") if node.get("stance") in STANCE_VALUES else "unknown"
            sub_lines = _wrap_sublabel(node.get("sublabel", ""))
            positioned[node.get("id", f"n{row_idx}_{i}")] = {
                "id": node.get("id"),
                "label": node.get("label", ""),
                "sublabel": node.get("sublabel", ""),
                "sublabel_lines": sub_lines,
                # Precomputed text anchors so the template needs no arithmetic.
                "sublabel_line1": sub_lines[0] if sub_lines else "",
                "sublabel_line2": sub_lines[1] if len(sub_lines) > 1 else "",
                "stance": stance,
                "x": round(x, 1),
                "y": round(y, 1),
                "w": NODE_W,
                "h": NODE_H,
                "cx": round(x + NODE_W / 2, 1),
                "y_label": round(y + 25, 1),
                "y_sub1": round(y + 44, 1),
                "y_sub2": round(y + 59, 1),
            }

    layout_edges = []
    for e in edges or []:
        src = positioned.get(e.get("from"))
        dst = positioned.get(e.get("to"))
        if not src or not dst:
            continue
        layout_edges.append({
            "x1": round(src["x"] + src["w"] / 2, 1), "y1": round(src["y"] + src["h"], 1),
            "x2": round(dst["x"] + dst["w"] / 2, 1), "y2": round(dst["y"], 1),
        })

    return {
        "width": round(total_width, 1),
        "height": round(total_height, 1),
        "nodes": list(positioned.values()),
        "edges": layout_edges,
    }


def scrub_fields(value: Any) -> Any:
    """Recursively rewrite internal data.json key names out of any rendered string."""
    if isinstance(value, str):
        out = value
        for key, label in FIELD_ALIASES.items():
            if key in out:
                out = out.replace(key, label)
        return out
    if isinstance(value, list):
        return [scrub_fields(v) for v in value]
    if isinstance(value, dict):
        return {k: scrub_fields(v) for k, v in value.items()}
    return value


def split_trend_analysis(text: str | None) -> list[dict[str, str]]:
    """Break the procurement-trend paragraph into labelled strands.

    Returns [] when the text carries no "小标题：" structure, in which case the report
    falls back to rendering the paragraph as written."""
    if not text:
        return []
    chunks = [c.strip() for c in TREND_SPLIT_RE.split(text) if c.strip()]
    points: list[dict[str, str]] = []
    for chunk in chunks:
        match = TREND_LABEL_RE.match(chunk)
        if not match:
            return []
        points.append({"label": match.group(1).strip(), "text": match.group(2).strip()})
    return points if len(points) > 1 else []


def _wan(amount: float) -> str:
    """Format a CNY amount into 万元 with at most two decimals."""
    val = amount / 10000.0
    return f"{val:,.2f}".rstrip("0").rstrip(".") if val < 100 else f"{val:,.0f}"


def build_kpis(
    it_bidding: dict[str, Any],
    open_questions: list[dict],
    sources: list[dict],
    company_basics: dict[str, Any],
) -> list[dict[str, Any]]:
    """A small, always-derivable summary band for the top of the report.

    Every tile is computed from the data that is already present — nothing is
    estimated or filled in. Tiles whose input is missing are dropped."""
    records = it_bidding.get("records") or []
    vendor_summary = it_bidding.get("vendor_summary") or []
    amounts = [r.get("amount") for r in records if r.get("amount")]
    confirmed = sum(v.get("total_amount") or 0 for v in vendor_summary)
    kpis: list[dict[str, Any]] = []

    if records:
        kpis.append({
            "value": len(records), "unit": "项", "label": "IT招投标记录",
            "note": f"其中 {len(amounts)} 项金额可考",
        })
    if amounts:
        kpis.append({
            "value": _wan(sum(amounts)), "unit": "万元", "label": "检索到的项目金额合计",
            "note": "含预算口径，非全部为成交金额",
        })
    if confirmed:
        kpis.append({
            "value": _wan(confirmed), "unit": "万元", "label": "已确认中标金额",
            "note": f"覆盖 {len(vendor_summary)} 家已确认供应商",
        })
    high = [q for q in open_questions if (q.get("priority") or "").strip() == "高"]
    if open_questions:
        kpis.append({
            "value": len(open_questions), "unit": "条", "label": "待核实事项",
            "note": f"其中高优先级 {len(high)} 条" if high else None,
        })
    if sources:
        kpis.append({
            "value": len(sources), "unit": "个", "label": "参考来源",
            "note": (company_basics.get("financials") or {}).get("is_listed") and "含上市公司披露" or None,
        })
    return kpis[:5]


def prepare_context(data: dict[str, Any]) -> dict[str, Any]:
    data = scrub_fields(data)
    meta = data.get("meta", {}) or {}
    executive_summary = data.get("executive_summary", {}) or {}
    company_basics = data.get("company_basics", {}) or {}
    core_pain_points = data.get("core_pain_points", []) or []
    strategy = data.get("strategy", {}) or {}
    it_landscape = data.get("it_landscape", {}) or {}
    it_investment = dict(data.get("it_investment", {}) or {})
    it_bidding = data.get("it_bidding", {}) or {}
    decision_chain = data.get("decision_chain", {}) or {}
    business_architecture = data.get("business_architecture", {}) or {}
    customer_swot = data.get("customer_swot", {}) or {}
    open_questions = data.get("open_questions", []) or []
    sources = data.get("sources", []) or []

    annotate_confidence(executive_summary.get("key_points"))
    annotate_confidence(company_basics.get("profile_facts"))
    annotate_confidence((company_basics.get("organization") or {}).get("key_departments"))
    annotate_confidence(company_basics.get("five_year_development"))
    if company_basics.get("five_year_development"):
        company_basics["five_year_development"] = sorted(
            company_basics["five_year_development"], key=lambda i: str(i.get("year") or "")
        )
    annotate_confidence(core_pain_points)
    annotate_confidence(strategy.get("key_initiatives"))
    annotate_confidence(it_landscape.get("known_vendor_relationships"))
    annotate_confidence(it_bidding.get("records"))
    annotate_confidence(decision_chain.get("roles"))
    annotate_confidence(business_architecture.get("layers"))

    business_scale = dict(company_basics.get("business_scale") or {})
    company_basics["business_scale"] = business_scale
    if it_investment:
        it_investment["confidence_class"] = confidence_class(it_investment.get("confidence"))

    financials_chart = build_financials_chart(company_basics.get("financials"))
    vendor_chart = build_vendor_chart(it_bidding.get("vendor_summary"))
    timeline_chart = build_bidding_timeline_chart(it_bidding.get("records"))
    diagram = build_decision_diagram(decision_chain.get("diagram_nodes"), decision_chain.get("diagram_edges"))

    records = it_bidding.get("records") or []
    vendor_summary = sorted(it_bidding.get("vendor_summary") or [], key=lambda v: v.get("total_amount") or 0, reverse=True)
    # Precompute display strings so the template carries no formatting logic.
    for v in vendor_summary:
        total = v.get("total_amount")
        v["total_amount_display"] = f"{total:,.0f}" if total else "—"
        share = v.get("share_pct")
        v["share_display"] = f"{share}%" if share is not None else "—"
        v["categories_display"] = "、".join(v.get("categories") or []) or "—"
    it_bidding = {
        **it_bidding,
        "records": records,
        "record_count": len(records),
        "vendor_summary": vendor_summary,
        "trend_points": split_trend_analysis(it_bidding.get("trend_analysis")),
    }

    roles = decision_chain.get("roles") or []
    decision_chain = {
        **decision_chain,
        "has_role_type": any((r.get("role_type") or "").strip() for r in roles),
    }
    kpis = build_kpis(it_bidding, open_questions, sources, company_basics)

    charts_json = json.dumps(
        {"financials": financials_chart, "vendor": vendor_chart, "timeline": timeline_chart},
        ensure_ascii=False,
    )
    # Defuse "</script>" so embedded JSON can never terminate the surrounding <script> tag early.
    charts_json = charts_json.replace("</", "<\\/")

    return {
        "meta": meta,
        "executive_summary": executive_summary,
        "company_basics": company_basics,
        "core_pain_points": core_pain_points,
        "strategy": strategy,
        "it_landscape": it_landscape,
        "it_investment": it_investment,
        "it_bidding": it_bidding,
        "decision_chain": decision_chain,
        "business_architecture": business_architecture,
        "customer_swot": customer_swot,
        "open_questions": open_questions,
        "sources": sources,
        "financials_chart": financials_chart,
        "vendor_chart": vendor_chart,
        "timeline_chart": timeline_chart,
        "diagram": diagram,
        "kpis": kpis,
        "charts_json": charts_json,
    }


def render(data: dict[str, Any]) -> str:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html"]),
    )
    env.globals["render_badge"] = render_badge
    env.globals["render_src"] = render_src
    template = env.get_template(TEMPLATE_NAME)
    context = prepare_context(data)
    return template.render(**context)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", required=True, type=Path, help="Path to data.json")
    parser.add_argument("--output", required=True, type=Path, help="Path to write the HTML report")
    args = parser.parse_args()

    data = load_data(args.data)
    html = render(data)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    logger.info("Report written to %s", args.output)


if __name__ == "__main__":
    main()
