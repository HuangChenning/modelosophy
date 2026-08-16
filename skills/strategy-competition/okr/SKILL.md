---
name: okr
description: >
  用 OKR（Objectives and Key Results）把鼓舞性目标与可度量关键结果对齐，驱动聚焦与复盘，
  而不是写成 KPI 考核表或待办清单。Use when user says “OKR”“目标关键结果”“怎么写 KR”
  “对齐公司目标”。不要与 BCG（组合投资）或 VRIO（资源审计）混淆；也不要把 OKR 当惩罚工具。
metadata:
  author: modelosophy（蒸馏自 Intel/Google 流行的 OKR 实践与常见失败模式）
  version: v0.x-draft
  source: OKR 实践（Doerr 等传播）；目标设定文献边界
---

# OKR Objectives and Key Results

## 这是什么

**OKR**：用定性的 **Objective（目标）** 描述「要去哪」，用少量定量的 **Key Results（关键结果）** 描述「如何知道走到了」。强调对齐、聚焦、透明与周期复盘；理想中 KR 是结果而非任务列表。

它是**执行对齐框架**，不是战略生成器：战略方向仍来自五力/SWOT/蓝海等；OKR 把已选方向拆成可追踪结果。

## 什么时候用

- "团队目标太散，要对齐"
- "OKR / 关键结果怎么写"
- 季度/半年聚焦与复盘

**不要**当主模型：

- 业务组合投砍 → [`bcg-matrix`](../bcg-matrix/SKILL.md)
- 资源是否构成优势 → [`vrio`](../vrio/SKILL.md)
- 持续改进循环步骤 → [`pdca`](../../efficiency-execution/pdca/SKILL.md)

## 怎么用（执行步骤）

1. **写 1–3 个 Objective。** 鼓舞、定性、方向清晰；禁止「做好本职工作」。判据：外人能否理解优先级。
2. **每个 O 配 2–4 个 KR。** KR 必须可度量、有基线与目标值，且是**结果**（转化率、延迟、收入、质量）不是「上线某功能」。若只能写任务，先问「上线为了哪一结果」。
3. **检查对齐。** 下级 OKR 如何支撑上级 KR；标出冲突资源。禁止复制粘贴同一句空话。
4. **设挑战度。** 常见实践：满分难；以 0.6–0.7 为健康挑战（按组织文化调整）。全部稳稳 1.0 往往 KR 太保守。
5. **周期中检视。** 双周看进度与阻碍；改行动不轻易改 KR（除非前提崩塌）。
6. **复盘分离评分与绩效惩罚。** OKR 主要用于学习与聚焦；若完全绑死调薪惩罚，会诱发沙袋目标。

## 例证

**产品团队**：O「让新用户第一周体验到价值」；KR「D7 留存从 a→b」「激活漏斗步骤 X 完成率→y」——揭示结果型 KR。

**失败写法**：KR「完成 10 个项目」——揭示任务清单伪装。

**（局限）**：创新探索期过度 OKR 化会扼杀可选性；需与实验额度并存。

## 什么时候不适用（边界）

- **战略未定**：先战略工具，再 OKR。
- **强合规计件环境**：传统 KPI 可能更合适。
- **个人日常琐事**：用 GTD/清单，不要抬成 OKR。

## 常见误用

- **KR=待办**：改写为结果。
- **OKR 过多**：失去聚焦 → 砍到少数。
- **当考核大棒**：诱发保守目标 → 分离绩效机制。
- **与战略工具抢活**：OKR 不产生护城河分析。

## 相关模型

- **与[PDCA](../../efficiency-execution/pdca/SKILL.md)**：OKR 定周期目标；PDCA 管改进循环。可连用。
- **与[BCG 矩阵](../bcg-matrix/SKILL.md)**：组合决策后对选定业务写 OKR。
- **与[麦肯锡 7S](../mckinsey-7s/SKILL.md)**：OKR 写目标度量；组织结构/制度/文化卡住时先用 7S 清障碍。
- **与[SWOT](../swot/SKILL.md)**：SWOT 出战略选项；OKR 跟踪执行。
- **与[艾森豪威尔矩阵](../../efficiency-execution/eisenhower-matrix/SKILL.md)**：个人优先级；组织对齐用 OKR。
- **与[理论约束 TOC](../../cognitive-thinking-tools/theory-of-constraints/SKILL.md)**：若吞吐瓶颈未破，OKR 可能指向错误结果——先约束。

## 记忆钩子

O 定方向，KR 定**可验证结果**——不是把待办抬成目标。
