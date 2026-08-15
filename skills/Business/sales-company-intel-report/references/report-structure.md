---
title: 企业深度情报报告 - 数据结构与字段定义（v3.0）
date: 2026-08-12
tags: [sales, sales-company-intel-report, report-structure, schema]
---

# 报告十个板块与 data.json Schema

本文件定义 `data.json` 的完整结构，供你在 Step 3（结构化分析）阶段填写。字段级别的写作要求写在每个板块下方。`scripts/generate_report.py` 按此结构读取数据；**字段名不要自行改写**，否则脚本无法正确渲染对应图表/图形。

没有检索到的字段留空（字符串填 `""`，数组填 `[]`，数字填 `null`），不要用"暂无数据"之类的占位符塞进本该是数字或结构化的字段——脚本会根据字段是否为空来决定是否渲染对应图表/小节，占位符文字反而会被当成有效数据渲染出来。

**置信度术语统一为三档**：`已证实`（有明确来源，理想情况下 ≥2 个独立来源交叉印证）、`推断`（基于事实的合理推理）、`待核实`（缺乏直接证据，需要在拜访中确认）。全文件所有 `confidence` 字段只能是这三个值之一，不要自造其他说法。

**来源引用**：能标来源编号的字段尽量带 `source_refs`（数组，元素是 `sources` 里定义的 `id`，如 `["S1","S3"]`），对应到报告末尾的来源列表。老字段里保留的自由文本 `source` 字段仍然可以写，但只要能拆出明确来源，优先用 `source_refs` 编号方式，方便报告正文用 `[S1]` 上标引用。

## 完整 Schema

```json
{
  "meta": {
    "company_name": "目标公司全称",
    "industry": "所属行业",
    "report_purpose": "报告用途（对应 Step 1 采集的选项）",
    "generated_date": "YYYY-MM-DD",
    "research_cutoff": "YYYY-MM-DD（检索截止日期，通常等于生成日期）",
    "scope_note": "本报告仅覆盖客户客观情况（公司基本面、战略、IT现状、招投标、决策链），不含产品匹配、竞品对比、报价或销售话术。",
    "sources_note": "一句话说明本次信息来源的整体情况，例如：以下信息主要来自公司官网、企查查公开页面、XX省公共资源交易中心，检索时间为2026年8月"
  },
  "executive_summary": {
    "headline": "整份报告最重要的一句话判断——这家公司现在处于什么阶段、最值得销售/售前关注的信号是什么",
    "key_points": [
      {"point": "关键判断1（结论先行，一句话说完）", "confidence": "已证实/推断/待核实", "source_refs": ["S1"]}
    ],
    "first_contact_checklist": [
      "首次接触/拜访中必须核实的事项1（对应 open_questions 里优先级最高的几条）"
    ]
  },
  "company_basics": {
    "profile_facts": [
      {"label": "成立时间", "value": "...", "confidence": "已证实", "source_refs": ["S1"]},
      {"label": "注册资本", "value": "...", "confidence": "已证实", "source_refs": ["S1"]},
      {"label": "股权结构", "value": "...", "confidence": "已证实/推断", "source_refs": ["S1"]},
      {"label": "总部/分支机构", "value": "...", "confidence": "已证实", "source_refs": ["S1"]}
    ],
    "organization": {
      "summary": "部门设置、汇报关系概述（v3.0新增，参考华为MCR「业务全景研究」的组织架构分析项，仅描述客观事实，不做组织效能评价）",
      "key_departments": [
        {"name": "部门名称", "function": "职能一句话", "confidence": "已证实/推断", "source_refs": ["S.."]}
      ],
      "confidence": "已证实/推断",
      "source_refs": ["S.."]
    },
    "business_scale": {
      "revenue_scale": "营收规模描述，如「2025年营收约XX亿元」",
      "employee_count": "员工规模描述",
      "confidence": "已证实/推断",
      "source_refs": ["S2"]
    },
    "industry_position": "行业地位判断（市场份额、排名、细分领域优势等），需说明依据",
    "business_model": {
      "summary": "核心业务运作方式与价值链概述（v3.0新增，可用波特五力分析客户所在行业的竞争结构作为背景，见 references/business-context-tools.md）",
      "confidence": "已证实/推断",
      "source_refs": ["S.."]
    },
    "five_year_development": [
      {"year": "2022", "event": "该年度的关键业务动态（并购/上市/重大项目/组织调整等）", "confidence": "已证实/推断"}
    ],
    "financials": {
      "is_listed": true,
      "stock_code": "如非上市公司填 null",
      "years": ["2021", "2022", "2023", "2024", "2025"],
      "revenue": [null, null, null, null, null],
      "revenue_unit": "亿元",
      "net_profit": [null, null, null, null, null],
      "gross_margin_pct": [null, null, null, null, null],
      "source_refs": ["S3"],
      "note": "非上市公司或数据不全时，在此说明「未公开披露，数据缺失年份已留空」，不要用行业均值臆造具体数字"
    }
  },
  "core_pain_points": [
    {
      "point": "客户自己/媒体公开表达出的紧迫挑战，如「区域市场份额被本地新兴对手蚕食」（v3.0新增顶层字段）",
      "evidence": "支撑依据，说明这个判断来自哪条新闻/专访/财报信号",
      "confidence": "已证实/推断/待核实",
      "source_refs": ["S.."]
    }
  ],
  "strategy": {
    "summary": "战略方向总述（1-2段）",
    "key_initiatives": [
      {"title": "举措名称，如「数字化转型三年规划」", "description": "...", "confidence": "已证实/推断", "source_refs": ["S4"]}
    ]
  },
  "it_landscape": {
    "trend_summary": "该公司所处行业的IT发展趋势，以及该公司在其中的位置",
    "current_state": "该公司IT/信息化现状描述（系统架构、国产化进展、数字化成熟度等）",
    "tech_stack_signals": ["从招聘JD/新闻/招标中观察到的技术栈信号，如「招聘中出现 Oracle DBA 岗位」"],
    "known_vendor_relationships": [
      {"title": "合作方名称 + 一句话概括，如「联想 - 5年IT战略规划合作」", "description": "具体细节（案例来源、涉及的系统/架构），信息来自厂商官网案例展示、新闻通稿等非招投标渠道", "confidence": "已证实/推断", "source_refs": ["S5"]}
    ],
    "confidence_notes": "对上述判断的整体置信度说明"
  },
  "it_investment": {
    "budget_estimate": "IT预算规模的估计或披露值，说明是【已证实】还是【推断】",
    "it_team_size": "IT团队规模（如可获得）",
    "investment_trend": "近年IT投入变化趋势判断（增长/持平/收缩），需说明依据",
    "confidence": "已证实/推断/待核实",
    "source_refs": ["S6"]
  },
  "it_bidding": {
    "records": [
      {
        "project_name": "招标/中标项目全称",
        "amount": 1234567,
        "amount_display": "123.46万元",
        "date": "2024-05",
        "category": "数据库/基础软件 | 服务器存储 | 云服务 | 运维外包 | 信创/国产化 | 安全合规 | 其他",
        "vendor": "中标供应商全称",
        "source_refs": ["S7"],
        "confidence": "已证实"
      }
    ],
    "vendor_summary": [
      {"vendor": "供应商名称", "win_count": 3, "total_amount": 4500000, "share_pct": 35.2, "categories": ["数据库/基础软件"]}
    ],
    "trend_analysis": "采购趋势分析：预算变化、技术选型变化（如是否转向国产数据库）、供应商集中度变化、招采节奏（是否有固定周期）等，需明确引用 records 中的具体证据支撑判断，不要泛泛而谈"
  },
  "decision_chain": {
    "diagram_nodes": [
      {"id": "board", "label": "董事会/高级管理层", "sublabel": "最终预算与战略责任（姓名待核实）", "level": 0, "stance": "unknown"},
      {"id": "cio", "label": "首席信息官/信息化负责人", "sublabel": "姓名（如已知）+ 一句话职责", "level": 1, "stance": "supportive"},
      {"id": "ops", "label": "运维/DBA/数据团队负责人", "sublabel": "...", "level": 2, "stance": "unknown"},
      {"id": "procurement", "label": "采购/合规评审", "sublabel": "...", "level": 2, "stance": "neutral"}
    ],
    "diagram_edges": [
      {"from": "board", "to": "cio"},
      {"from": "cio", "to": "ops"},
      {"from": "cio", "to": "procurement"}
    ],
    "roles": [
      {
        "role": "CIO/信息化负责人 等岗位角色",
        "role_type": "UB/SP/TB/EB（v3.0新增，可选，见 references/decision-chain-framework.md 的四角色模型，映射不上就留空）",
        "name": "姓名（如已知）",
        "decision_position": "决策人 | 报批者 | 强影响者 | 执行者/影响者",
        "decision_weight": "高/中/低（v3.0新增，可选）",
        "communication_style": "控制型/倡导型/分析型/亲切型（v3.0新增，可选，仅在有公开信息支撑时填写）",
        "notes": "关注点、行为线索（例如公开发声、参与的项目）",
        "confidence": "已证实/推断",
        "source_refs": ["S8"]
      }
    ],
    "executives": [
      {"name": "...", "title": "...", "background": "教育背景/履历简述", "source_refs": ["S9"]}
    ]
  },
  "business_architecture": {
    "layers": [
      {
        "name": "业务分层名称，如「接入与业务层」「数据与数据库层」「基础设施与运维层」",
        "description": "客观描述该层承载的业务/系统",
        "attention_points": ["该层值得关注的IT/数据关切点，如「多引擎数据库并存，统一监控覆盖率未知」——只描述现象和关切，不点名解决方案或产品"],
        "confidence": "已证实/推断",
        "source_refs": ["S10"]
      }
    ]
  },
  "customer_swot": {
    "strengths": [{"point": "客户自身的优势，如「规模大，具备持续IT投入能力」", "source_refs": ["S2"]}],
    "weaknesses": [{"point": "客户自身的短板/风险，如「多次并购后系统整合复杂度高」", "source_refs": ["S4"]}],
    "opportunities": [{"point": "客户面临的外部机会，如「所在行业信创窗口期临近」", "source_refs": []}],
    "threats": [{"point": "客户面临的外部压力/风险，如「监管趋严、同业竞争加剧」", "source_refs": []}]
  },
  "open_questions": [
    {
      "question": "需要在下次接触中核实的具体问题",
      "why_it_matters": "为什么这个问题对理解客户重要",
      "priority": "高/中/低",
      "suggested_contact": "建议通过哪个角色了解（引用 decision_chain.roles 里的角色名，不涉及具体产品切入点）"
    }
  ],
  "sources": [
    {"id": "S1", "title": "来源标题/页面名称", "publisher": "发布方，如「公司官网」「XX省公共资源交易中心」", "date": "YYYY-MM-DD 或 YYYY-MM", "url": "链接（没有可留空）"}
  ]
}
```

## 字段级写作要求

### executive_summary（执行摘要）—— 最后写，放最前面

- 这是全篇报告唯一"结论先行"的地方，也是读者最先看到的部分。`headline` 一句话说完"这家公司现在是什么状态、最该关注什么"，不要写成模糊的"该公司具备一定的合作潜力"这类正确的废话。
- `key_points` 建议 3-5 条，每条都是一个独立的、可核查的判断，不是章节标题的复述。写法参考："2024年该公司IT招投标记录中，X供应商连续两年中标数据库类项目，供应商集中度较高"，而不是"该公司有一些招投标记录"。
- `first_contact_checklist` 直接从 `open_questions` 里挑优先级最高的 2-4 条，帮销售明确"这次见面必须搞清楚什么"。

### company_basics（公司基本情况）

- `profile_facts` 只填能查到来源的项，查不到的字段不要出现在数组里（不要填 value 为"未知"的条目）。
- `organization`（v3.0新增）：只需要说清楚部门设置和关键部门职能，不需要画出完整的组织树；能识别出与IT/信息化相关的部门（这块信息之后会和 `decision_chain` 联动）就够了。查不到公开的组织架构信息是常见情况，直接留空，不要靠"大公司一般都有XX部门"这类通用常识补全。
- `business_model`（v3.0新增）：客观描述客户的业务是怎么运转的（核心业务流程、价值链上的关键环节），可以用波特五力分析行业竞争结构作为背景（见 `references/business-context-tools.md`），但不要写成"我方产品在这个环节能发挥什么作用"。
- `five_year_development` 尽量覆盖近5年（当前年份往前推5年），条目按年份升序排列；某一年没有可记录的重大事件是正常的，不必凑数。
- `financials`：只有当公司是上市公司或有其他公开披露渠道（如行业协会年鉴、招股书）时才填数字；非上市公司的 `revenue`/`net_profit`/`gross_margin_pct` 全部填 `null`，在 `note` 里说明，并在 `business_scale` 里改用定性/区间描述。
- 某个指标（如毛利率）在你检索到的媒体报道/摘要里没提到，不代表年报原文里一定没有披露——`note` 里区分清楚这是"检索到的二手资料未提及，未逐页核对年报原文"，还是"公司确认未披露该指标"，这两者的置信度含义不同。

### core_pain_points（客户核心痛点，v3.0新增顶层字段）

只收录客户自己（高管发言/专访）或权威第三方（行业分析报告、财报风险因素章节）公开表达出的挑战，不要靠"这个行业普遍都有这个问题"的通用常识替客户代言。每条都要在 `evidence` 里说明这个判断的具体依据。这个字段和 `customer_swot.weaknesses` 有一定重叠，区别在于：`core_pain_points` 更聚焦"客户自己意识到、觉得紧迫"的问题，`customer_swot.weaknesses` 是研究者从外部视角做的客观分析判断，两者可以有重合条目，不必刻意去重。

### strategy（战略方向）

聚焦近1-2年公开披露的战略规划、转型方向、组织架构调整，与前面"近5年业务发展"区分开——这里要更聚焦"面向未来"的表述，比如年报里的"未来展望"、高管专访里提到的规划。

### it_landscape / it_investment（IT发展趋势与现状 / IT投入）

这两块通常是全报告中最难拿到直接公开数据的部分。允许更多使用【推断】，但每条推断都要写清楚"依据什么信号做出这个判断"。绝对不能凭空断言具体预算数字。

检索中经常会遇到这种情况：找到了厂商官网/新闻稿披露的具体合作案例，信息很具体但不是正式招投标公告，缺少项目名称、招标性质、金额这些 `it_bidding.records` 要求的字段。这类信息填入 `it_landscape.known_vendor_relationships`，并标注它是厂商宣传性案例还是双方联合发布的信息，提醒读者这类材料可能存在宣传口径夸大，仅作背景参考——不要因为信息量大就写成"这正好是某某产品的应用场景"，停在客观描述这一步。

### it_bidding（近3年IT招投标情况）—— 报告的核心板块之一

- 时间范围：从当前年份往前推3年（含当前年）。
- `records` 里的每一条都必须来自实际检索到的公开信息，字段不全的记录也要保留（比如金额未披露的可以把 `amount` 填 `null`，但 `amount_display` 写"未披露具体金额"），不要因为某个字段缺失就丢弃整条记录。
- `vendor_summary` 按 `records` 汇总生成：中标次数、中标金额合计（仅统计 `amount` 非空的记录）、金额份额百分比、涉及的项目类别。供应商名称需要做基本的归一化，否则份额统计会失真。
- `trend_analysis` 必须引用 `records` 里的具体项目作为证据，不能只写"预算呈上升趋势"这种空泛结论。这里只做客观趋势判断（预算变化、技术选型变化、供应商集中度），不做"我方如何切入"的判断。

详细的检索方法和分类标准见 `references/it-bidding-analysis.md`。

### decision_chain（决策链与高管）—— 含关系图数据

- `diagram_nodes` / `diagram_edges` 用于渲染 SVG 决策链关系图。`level` 从 0（最高层）往下递增，脚本会按 level 分层横向排布；`stance` 只允许四个值：`supportive`（对新方案/外部供应商态度开放）、`resistant`（倾向维持现状，路径依赖强）、`neutral`（中立/待观察）、`unknown`（信息不足，暂不判断）——**这是对组织行为倾向的客观研究判断，不是"这个人会不会买我们产品"，写 notes 时也保持这个分寸**。
- 节点数量建议 4-8 个，太多会让图看不清；找不到具体人名的岗位仍然要画出来（`label` 用岗位名，`sublabel` 写"姓名待核实"），因为决策链的组织结构本身就是有价值的信息，不必等有名字才画。
- `roles` 是表格形式的补充说明，字段含义同 v1：`decision_position` 描述决策链角色（决策人/报批者/强影响者/执行者），不涉及销售策略。
- 如果检索到具体姓名（如CIO姓名），填入 `executives`；只知道岗位没人名的，`name` 留空，仍然要填 `role` 和 `decision_position`。
- **v3.0新增**：`roles` 可以选填 `role_type`（UB/SP/TB/EB，见 `references/decision-chain-framework.md` 的四角色模型）、`decision_weight`（高/中/低）、`communication_style`（控制型/倡导型/分析型/亲切型，仅在有公开信息支撑时填写，不要凭岗位刻板印象猜测）。这三个字段都是可选的，映射不上或没有依据就留空，不要为了填满字段而编造。
- **明确不允许添加的字段**：不要给 `roles` 加"与我方关系状态"之类的打分字段（华为原始模型里有 -1到3 的五级评分）。这份报告只研究客户内部的权力结构，不评估这些人对我方的态度——那需要销售自己的一手接触经验，且属于产品匹配/攻坚方案层的工作范围。

### business_architecture（业务与IT架构分层）

参考决策链之外，这一板块回答"这家公司的业务是怎么运转的，每一层对数据/IT有什么客观关切"。分层粒度参考：接入/业务层 → 应用/核心系统层 → 数据/数据库层 → 基础设施/运维层，具体分几层、叫什么名字按行业和公司实际情况调整，不必强行套用银行业的四层模型。

**`attention_points` 只写现象和客观关切，不写解决方案或产品名。** 例如可以写"多个数据库引擎并存，统一监控和备份策略是否覆盖全部实例未知"，但不要写"这正是zCloud的最佳应用场景"——后半句是另一个技能的工作。

### customer_swot（客户侧SWOT）

**这个SWOT分析的主语是客户自己，不是"我方 vs 客户现有供应商"。** 优势/劣势描述客户自身的业务和组织状况（规模、执行力、系统复杂度等），机会/威胁描述客户面临的外部环境变化（行业政策、监管、竞争格局）。如果你发现自己在写"这是我们的机会窗口"，说明写偏了——那属于攻坚策略层，不是这份报告的范围。

### open_questions（待核实清单）

按优先级从高到低排列，每条要说清楚"为什么这个问题重要"和"该找谁了解"（引用 `decision_chain.roles` 里已经识别出的角色）。这份清单本质上是"下次拜访/接触的信息核实议程"，不是销售话术或切入策略——`suggested_contact` 只回答"问谁"，不回答"怎么说"。

### sources（来源列表）

每个 `source_refs` 引用的编号都必须能在这里找到对应条目。**编号从 S1 开始连续编号，不要跳号或重复编号**；同一个来源被多处引用时复用同一个编号，不要重复创建。`url` 没有可以留空，但 `title` 和 `publisher` 尽量填，方便销售自己回去复核。
