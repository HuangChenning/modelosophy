---
name: mckinsey-7s
description: >
  用麦肯锡 7S 框架诊断组织是否「七要素对齐」：硬性（战略 Strategy、结构 Structure、制度 Systems）
  与软性（共同价值观 Shared Values、技能 Skills、风格 Style、人员 Staff）。Use when user says
  “7S”“麦肯锡七要素”“战略落地为什么卡住”“组织对齐/ congruence”“改结构却没效果”。
  不适用于行业利润池（五力）、业务组合投砍（BCG/GE 九宫）、或仅写 OKR 目标清单。
metadata:
  author: modelosophy（蒸馏自 McKinsey 7S / Waterman–Peters–Phillips，非原书卡片照抄）
  version: v0.x-draft
  source: Waterman, Peters & Phillips, “Structure Is Not Organization” (Business Horizons, 1980); McKinsey 7S framework; 研究笔记 docs/books/strategy-competition-7s-ge/
---

# 麦肯锡 7S McKinsey 7S

## 这是什么

**麦肯锡 7S**：把组织效能视为七个相互依赖要素的**对齐（congruence）**问题——三个偏「硬」：**Strategy（战略）、Structure（结构）、Systems（制度/流程）**；三个偏「软」：**Skills（技能）、Style（领导与管理风格）、Staff（人员构成与发展）**；中心是 **Shared Values（共同价值观 / 超ordinate goals）**。改其一而不调其余，常出现「战略写了、组织没跟上」。

它由麦肯锡顾问 Robert Waterman、Tom Peters、Julien Phillips 等在约 1980 年前后提出（经典表述见 *Structure Is Not Organization*），反驳「只改组织结构图就能解决问题」的机械观点。7S 是**诊断与变革设计清单**，不是行业分析工具，也不是组合投资矩阵。

硬/软之分是启发式：硬要素相对更易画在纸上；软要素更依赖文化与行为，却往往决定硬变革能否兑现。

## 什么时候用

用户出现以下意图时启用本 Skill：

- "战略定了但执行不动 / 组织跟不上"
- "7S / 麦肯锡七要素 / 组织对齐诊断"
- "我们改了汇报线/流程，为什么文化与能力还是老样子"
- 并购整合、转型启动、新战略宣贯前后的组织体检

**不要**在以下情况套用本模型：

- 问行业谁赚钱、议价谁强 → [`porters-five-forces`](../porters-five-forces/SKILL.md)
- 多业务单元投/砍/收割 → [`bcg-matrix`](../bcg-matrix/SKILL.md) 或 [`ge-mckinsey-matrix`](../ge-mckinsey-matrix/SKILL.md)
- 只需要目标–关键结果对齐写法 → [`okr`](../okr/SKILL.md)
- 内外部态势四格盘点 → [`swot`](../swot/SKILL.md)

## 怎么用（执行步骤）

每一步必须给出**可操作判据**（问什么、写什么、通过/失败长什么样），禁止只换说法重复结论。

1. **写清诊断对象与时间窗。** 对象可以是公司、事业部或关键转型项目；时间窗写「现状 vs 目标态」（如 12–18 个月后）。判据：能否用一句话说明「要对齐的是哪次变革/哪条战略」，否则 7S 会变成空泛企业文化讨论。

2. **先钉 Shared Values（中心）。** 用可观察行为写 3–5 条「我们真正奖励/惩罚什么」，禁止只抄官网口号。判据：每条都能举出近 90 天内的真实决策或人事信号；若口号与行为冲突，以行为为准并标红。

3. **逐项填写其余六 S（现状）。** 每项只写**可验证事实**：Strategy（优先客户/不做清单）、Structure（决策权与汇报）、Systems（预算、KPI、信息系统、审批）、Style（一把手与中层实际管理习惯）、Staff（关键岗位编制与激励）、Skills（组织级核心能力，非「大家很努力」）。判据：外人能否据证据复核；含糊词（「协同好」「氛围佳」）一律打回。

4. **做对齐矩阵，标冲突边。** 对任意两 S，问：A 的要求是否被 B 系统性阻碍？至少标出 3 条高影响冲突（例：Strategy 要平台化，Systems 仍按产品线考核；Structure 扁平，Style 仍事无巨细审批）。判据：每条冲突写「谁在日常流程里被卡住」。

5. **区分硬杠杆与软约束，排变革顺序。** 默认：先明确目标态 Shared Values + Strategy，再改 Structure/Systems 中能解除冲突的最小集合，同时规划 Skills/Staff/Style 的配套（培训、编制、领导行为）。判据：每个硬改动旁边必须有至少一项软配套；只有结构图没有激励/技能计划 → 不合格。

6. **输出「7S 对齐行动包」。** 每条行动：改哪个 S、解除哪条冲突、90 天可观察信号、复盘日。禁止输出无优先级的七段散文。

> 常见错误提醒：把 Shared Values 写成海报文案；把 Skills 写成个人简历；把 Systems 只理解为 IT 系统而忽略考核与预算规则。

## 例证

**结构已改、激励未改（经典失败模式）**：公司按客户行业重划事业部（Structure），但奖金与晋升仍按旧产品线出货（Systems），前线继续「卖好卖的」——揭示硬结构变更被软/制度要素抵消，正是 7S 要抓的对齐失败。

**并购后文化与人员未对齐**：战略上宣布「一体化平台」（Strategy），保留两套审批与两套销售激励（Systems），核心人才双轨观望（Staff/Style）——揭示 Shared Values 未统一时，结构合并只是名义。

**与 OKR 连用**：7S 诊断出「战略要探索第二曲线，但 Skills/Staff 全压在现金牛交付」后，再用 OKR 把探索配额写成可度量关键结果——揭示 7S 管组织对齐，OKR 管目标度量，不互相替代。

## 什么时候不适用（边界）

- **问题本质是产业利润池或竞争结构**：7S 不回答「这行业值不值得做」→ 先五力/护城河。
- **问题是组合里哪条业务投砍**：用 BCG 或 GE 九宫；7S 回答「选定业务后组织能否兑现」。
- **微团队、无正式制度**：七要素过度工程；改用更轻的角色/节奏对齐即可。
- **把 7S 当万能变革剧本**：它是诊断清单，不自动给出战略内容本身。

## 常见误用

- **只改 Structure**：以为换架构图等于转型 → 必须同步 Systems/Skills/Style。
- **价值观口号化**：官网使命当 Shared Values → 改写为可观察的奖惩信号。
- **与 SWOT 混用成一张表**：SWOT 扫内外态势；7S 扫组织内部对齐——可先后用，勿合并成洗衣单。
- **与 OKR 对立**：OKR 写目标；若 Systems/Style 惩罚冒险，OKR 会形式化 → 先 7S 清障碍再写 OKR。
- **七格平均用力**：无冲突优先级 → 只打高影响冲突边。

## 相关模型

- **与[SWOT](../swot/SKILL.md)**：SWOT 做内外部匹配与行动方向；7S 检验组织能否支撑该方向。说「优劣势机会威胁」走 SWOT；说「战略落地组织卡住」走 7S。
- **与[OKR](../okr/SKILL.md)**：对齐目标写法走 OKR；对齐结构/制度/文化走 7S。常先 7S 清阻碍再设 OKR。
- **与[VRIO](../vrio/SKILL.md)**：VRIO 审计单条资源是否有持续优势；7S 看组织整体是否对齐以兑现资源。Skills/Staff 讨论可与 VRIO 互证。
- **与[五力](../porters-five-forces/SKILL.md)**：五力看外部产业；7S 看内部组织。
- **与[第二曲线](../second-curve/SKILL.md)**：第二曲线定切换时机与输血；落地时用 7S 检查探索单元是否有独立 Systems/Staff。
- **与[GE 九宫](../ge-mckinsey-matrix/SKILL.md)**：九宫做组合优先级；入选业务的组织兑现用 7S。

## 记忆钩子

**战略不是组织**：硬三件（战略/结构/制度）+ 软三件（技能/风格/人员）绕着**共同价值观**转——缺一对齐边，变革就空转。
