# Decision & Probability

期望值、决策树、不确定性下的可执行决策 Skill。

与兄弟分类分流：不确定下的量化与流程化决策（期望值/效用/贝叶斯/情景/可逆门等）；认知偏误纠偏见 `behavioral-biases/`；结构化拆解见 `cognitive-thinking-tools/`；仓位/凯利等见 `finance-investing-models/`（本类只互链不复制）。

路径：`skills/decision-probability/<skill-name>/SKILL.md`。

当前合计 **24** 个（迁入种子 2 + M2 首批 11 + **M2b 第二批 11**，新建均为 `v0.x-draft`；名录其余条目见 ROADMAP）。

## Skills

- **[after-action-review](./after-action-review/SKILL.md)** — 复盘四步法（AAR）：意图→实际→落差→下次（`v0.x-draft`）。
- **[asymmetric-payoff](./asymmetric-payoff/SKILL.md)** — 不对称回报：比较上行/下行损益形状（`v0.x-draft`）。
- **[base-rate](./base-rate/SKILL.md)** — 基率/参考类：先锚定同类事件频率，再谨慎并入个案（`v0.x-draft`）。
- **[bayesian-updating](./bayesian-updating/SKILL.md)** — 贝叶斯更新：先验 × 似然 → 后验（`v0.x-draft`）。
- **[decision-journal](./decision-journal/SKILL.md)** — 决策日志：预注册信念与预测，事后校准（`v0.x-draft`）。
- **[decision-tree](./decision-tree/SKILL.md)** — 决策树：选项已知、结果不确定时可估概率与后果的多阶段选择；折叠期望值并判断是否值得买信息。
- **[expected-utility](./expected-utility/SKILL.md)** — 期望效用：金额非线性/破产约束下用 EU 而非只报 EV（`v0.x-draft`）。
- **[expected-value](./expected-value/SKILL.md)** — 期望值：把不确定结果量化为概率加权平均 EV=Σp·x，用于赌局、保险与公平分配直觉。
- **[grey-thinking](./grey-thinking/SKILL.md)** — 灰度认知：用可修订置信度替代非黑即白（`v0.x-draft`）。
- **[loss-function](./loss-function/SKILL.md)** — 损失函数：非对称错误代价下的行动/阈值（`v0.x-draft`）。
- **[monte-carlo](./monte-carlo/SKILL.md)** — 蒙特卡洛：对不确定输入抽样得结果分布（`v0.x-draft`）。
- **[mvp](./mvp/SKILL.md)** — MVP：以最小投入获得针对危险假设的学习信号（`v0.x-draft`）。
- **[ooda-loop](./ooda-loop/SKILL.md)** — OODA：观察—定向—决策—行动的对抗节奏闭环（`v0.x-draft`）。
- **[oz-principle](./oz-principle/SKILL.md)** — 奥兹原则：Above the Line 问责四步（`v0.x-draft`）。
- **[planning-fallacy](./planning-fallacy/SKILL.md)** — 计划谬误：纠偏系统性低估工期/成本（`v0.x-draft`）。
- **[pre-mortem](./pre-mortem/SKILL.md)** — 事前验尸：假定已失败以生成可预防原因（`v0.x-draft`）。
- **[probability-thinking](./probability-thinking/SKILL.md)** — 概率论思维：事件定义与概率语言入口（`v0.x-draft`）。
- **[rapid-experimentation](./rapid-experimentation/SKILL.md)** — 快速试错：有止损的短周期实验序列（`v0.x-draft`）。
- **[red-team](./red-team/SKILL.md)** — 红队：独立结构化对抗以找出可利用裂口（`v0.x-draft`）。
- **[reversible-irreversible](./reversible-irreversible/SKILL.md)** — 可逆/不可逆决策：按反悔成本匹配速度与审查重量（`v0.x-draft`）。
- **[risk-premium](./risk-premium/SKILL.md)** — 风险溢价：无风险基准之上的风险补偿口径（`v0.x-draft`）。
- **[scenario-planning](./scenario-planning/SKILL.md)** — 情景规划：少数可信分歧未来下的稳健选项与预警（`v0.x-draft`）。
- **[sensitivity-analysis](./sensitivity-analysis/SKILL.md)** — 敏感性分析：找翻转假设与稳健区（`v0.x-draft`）。
- **[threshold-effect](./threshold-effect/SKILL.md)** — 阈值效应：剂量/规则门槛与临界点分流（`v0.x-draft`）。

## Notes

- 本目录均为**可执行** Skill（何时用 / 怎么用 / 边界 / 相关模型）。
- 原「9 字段知识卡」不作主交付；有用字段可吸收进各 `SKILL.md`。
- 迁入种子：expected-value / decision-tree。
- **M2 首批**（`v0.x-draft`）：bayesian-updating / grey-thinking / reversible-irreversible / mvp / red-team / pre-mortem / ooda-loop / planning-fallacy / scenario-planning / expected-utility / base-rate。
- **M2b 第二批**（`v0.x-draft`）：monte-carlo / decision-journal / after-action-review / rapid-experimentation / probability-thinking / sensitivity-analysis / asymmetric-payoff / threshold-effect / loss-function / risk-premium / oz-principle。
- **已有@他类（本类不复制）**：凯利 → `finance-investing-models/kelly-criterion`；沉没成本 → `behavioral-biases/sunk-cost`；机会成本 → `econ-micro-markets/opportunity-cost`；满意化 → `game-theory-models/bounded-rationality`；临界质量 → `systems-complexity/tipping-point`；杠铃/反脆弱 → `learning-growth/antifragility`。
- 新建条目标 `v0.x-draft`；迁入项保留原 version。名录其余缺口见 ROADMAP。

## Other categories

[`behavioral-biases`](../behavioral-biases/) · [`business`](../business/) · [`cognitive-thinking-tools`](../cognitive-thinking-tools/) · [`econ-macro-theories`](../econ-macro-theories/) · [`econ-micro-markets`](../econ-micro-markets/) · [`efficiency-execution`](../efficiency-execution/) · [`finance-investing-models`](../finance-investing-models/) · [`game-theory-models`](../game-theory-models/) · [`learning-growth`](../learning-growth/) · [`strategy-competition`](../strategy-competition/) · [`systems-classic-effects`](../systems-classic-effects/) · [`systems-complexity`](../systems-complexity/) · [`thinking-models`](../thinking-models/)
