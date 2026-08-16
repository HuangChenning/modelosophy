<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="modelosophy —— 项目名旁是漏斗与水滴组成的蒸馏标记">
</p>

modelosophy 把人类千年沉淀的思维模型，转化为 AI 可以直接调用的 Skill。

SWOT、第一性原理、MECE、复利思维、第二序思维……每一个思维模型都成为一个独立、可组合的 Skill，而不是知识库里的一段文字。AI 像人一样使用它们——拆解问题、构建策略、做出决策。

## 项目简介与现状

这个仓库还处于早期阶段。`skills/<category>/` 下合计 **314** 个可执行 Skill（各分类 README 仍是分域索引；`_templates` 不是 Skill）。

早期「9 字段知识卡」方案已废弃为主交付；其中有用字段（提出者、常见误用、记忆钩子等）可吸收进可执行 `SKILL.md`。计划见 [`ROADMAP.md`](ROADMAP.md)。

分类一览（逐条简介见文末 [Skill 目录](#skill-目录)）：

| 分类 | 数量 | 目录 |
| --- | ---: | --- |
| [商业 / 组织情报](skills/business/README.md) | 1 | [目录](#商业--组织情报1) |
| [通用思维模型](skills/thinking-models/README.md) | 25 | [目录](#通用思维模型25) |
| [认知与思维工具](skills/cognitive-thinking-tools/README.md) | 28 | [目录](#认知与思维工具28) |
| [决策与概率](skills/decision-probability/README.md) | 24 | [目录](#决策与概率24) |
| [学习与成长](skills/learning-growth/README.md) | 23 | [目录](#学习与成长23) |
| [战略与竞争](skills/strategy-competition/README.md) | 12 | [目录](#战略与竞争12) |
| [效率与执行](skills/efficiency-execution/README.md) | 9 | [目录](#效率与执行9) |
| [系统与复杂](skills/systems-complexity/README.md) | 11 | [目录](#系统与复杂11) |
| [宏观经济学理论](skills/econ-macro-theories/README.md) | 30 | [目录](#宏观经济学理论30) |
| [微观经济学与市场](skills/econ-micro-markets/README.md) | 30 | [目录](#微观经济学与市场30) |
| [博弈论与策略](skills/game-theory-models/README.md) | 31 | [目录](#博弈论与策略31) |
| [行为经济学与偏误](skills/behavioral-biases/README.md) | 30 | [目录](#行为经济学与偏误30) |
| [金融与投资](skills/finance-investing-models/README.md) | 30 | [目录](#金融与投资30) |
| [系统与经典效应](skills/systems-classic-effects/README.md) | 30 | [目录](#系统与经典效应30) |

另有原属通用思维模型库的 Skill 已分批迁入学科分类（含本轮 **25** 条迁入认知/决策/学习/战略/效率/复杂系统），只在新分类下列出。

## 运作原理

<p align="center">
  <img src="./assets/readme/mechanism.svg" width="100%" alt="三阶段示意图：建模、蒸馏、复用">
</p>

一个思维模型首先被**识别为一种模式**（建模），然后被**提炼为可执行的步骤**（蒸馏），写成一份 `SKILL.md`，最终被**任何读取 skills 目录的 AI Agent 调用**（复用）。

## 使用方法

每个 Skill 都独立存放在 `skills/<category>/<name>/` 目录下，其中的 `SKILL.md` 供 AI Agent（例如 Claude Code）读取，了解这个 Skill 做什么、如何调用。

```bash
git clone https://github.com/HuangChenning/modelosophy.git
# 或者只把某一个 Skill 目录复制进你自己的项目
cp -r modelosophy/skills/<category>/<name> your-project/skills/<name>
```

如果一个 Skill 会生成报告，报告统一写入 `output/<skill-name>/`；这个目录只存在于本机，不会提交到本仓库。

## 仓库结构

```text
skills/<category>/<name>/SKILL.md      这个 Skill 做什么、何时使用
skills/<category>/<name>/references/   支撑该 Skill 的方法论与参考资料
skills/<category>/<name>/scripts/      生成/自动化脚本（如果有）
skills/<category>/<name>/assets/       该 Skill 渲染时使用的模板
```

`<category>` 按领域分组——例如 `business/`、`thinking-models/`、六学科分类，以及认知工具 / 决策 / 学习 / 战略 / 效率 / 复杂系统等平级目录。

输出 HTML 报告的 Skill 需遵循 [`DESIGN.md`](DESIGN.md) 中定义的统一视觉规范。

## 局限性

库仍处于早期：跨分类合计 **314** 个可执行模型（`business/` 1 + `thinking-models/` 25 + 六学科分类 181 + 名录扩充分类 107）。清单新补条目多为 `v0.x-draft`，尚待压力测试；编写规范仍可能随库扩张调整。

## 贡献一个思维模型

如果你有一个值得蒸馏的思维框架，欢迎按照上面的结构，新增一个 `skills/<category>/<name>/SKILL.md` 并提交 PR。

## Skill 目录

全部 **314** 个 Skill 的逐条简介。各分类 README 仍是分域索引。

### 商业 / 组织情报（1）

组织 / IT 情报与商业调研。

- **[org-it-intel-report](skills/business/org-it-intel-report/SKILL.md)** — 组织 IT 情报报告：按麦肯锡式结构输出组织整体情况 + IT 投入/招投标情报报告（厂商中立）。

### 通用思维模型（25）

通用推理、领导、沟通等杂项思维模型（学科专条已迁出）。

- **[abductive-reasoning](skills/thinking-models/abductive-reasoning/SKILL.md)** — 溯因推理：从令人惊讶的观察出发，生成并选择当前最佳解释假设（IBE），并标明待验点。
- **[contrarian-and-right](skills/thinking-models/contrarian-and-right/SKILL.md)** — 正确与非共识：检验非常规判断——超额洞见需既偏离主流，又经得起证据与可证伪预测。
- **[counterfactual-thinking](skills/thinking-models/counterfactual-thinking/SKILL.md)** — 反事实思维：处理「若非当时……」的心理模拟；区分上行/下行反事实，聚焦可控原因。
- **[deductive-reasoning](skills/thinking-models/deductive-reasoning/SKILL.md)** — 演绎法：从已接受的一般前提出发，按有效推理规则推出必然随之而来的结论。
- **[dual-goal-list](skills/thinking-models/dual-goal-list/SKILL.md)** — 双目标清单：写下约 25 个目标，圈定 Top 5 为 List A，其余列入主动回避的 List B。
- **[dual-process](skills/thinking-models/dual-process/SKILL.md)** — 双系统：用卡尼曼 System 1/2 判断何时信任直觉、何时强制慢思考。
- **[emotional-abc](skills/thinking-models/emotional-abc/SKILL.md)** — 情绪 ABC：把强烈情绪拆成触发事件 A、信念 B、情绪/行为后果 C，改 B 而非只压 C。
- **[five-w-one-h](skills/thinking-models/five-w-one-h/SKILL.md)** — 5W1H：把 Who/What/When/Where/Why/How 信息槽钉全，暴露缺腿事实。
- **[fogg-behavior-model](skills/thinking-models/fogg-behavior-model/SKILL.md)** — 福格行为模型：用 B=MAP（动机×能力×提示）诊断行为为何发生或未发生。
- **[gaslighting](skills/thinking-models/gaslighting/SKILL.md)** — 煤气灯效应：识别通过否认对方感知/记忆来夺取「现实定义权」的操纵模式。
- **[hook-model](skills/thinking-models/hook-model/SKILL.md)** — HOOK 模型：用 Trigger→Action→Variable Reward→Investment 设计可反复发生的习惯回路。
- **[implicit-premises](skills/thinking-models/implicit-premises/SKILL.md)** — 隐含前提：补全论证里未写出却托住结论的前提，并分类检验。
- **[johari-window](skills/thinking-models/johari-window/SKILL.md)** — 周哈里窗：用反馈与自我披露扩大开放区，减少盲目区与隐藏区误解。
- **[ladder-of-inference](skills/thinking-models/ladder-of-inference/SKILL.md)** — 推论阶梯：摊开从选数据、赋义、假设到信念与行动的攀升步骤。
- **[local-global-optima](skills/thinking-models/local-global-optima/SKILL.md)** — 局部最优：判断继续打磨当前路径是否已陷入小山峰，是否值得付代价换山。
- **[long-term-thinking](skills/thinking-models/long-term-thinking/SKILL.md)** — 长线思考：把决策放进多期后果与激励周期，写清近/中/远影响与考核约束。
- **[maslow-hierarchy](skills/thinking-models/maslow-hierarchy/SKILL.md)** — 马斯洛需求层次：把需求类别当检查表（非普遍定律），扫描生理到自我实现的缺口。
- **[munger-misjudgment](skills/thinking-models/munger-misjudgment/SKILL.md)** — 人类误判心理：用芒格 25 种心理倾向做清单扫描，并警惕 Lollapalooza 叠加。
- **[negentropy](skills/thinking-models/negentropy/SKILL.md)** — 负熵：用账本诊断开放系统如何靠输入自由能/信息维持局部有序并排出废热。
- **[process-replication](skills/thinking-models/process-replication/SKILL.md)** — 可复制化：把成功经验蒸馏为可迁移步骤，按本地约束适配后再规模化。
- **[redundancy](skills/thinking-models/redundancy/SKILL.md)** — 冗余备份：为故障与单点失效有意保留多余容量、路径或副本。
- **[situational-leadership](skills/thinking-models/situational-leadership/SKILL.md)** — 情境领导：按下属在具体任务上的准备度（能力×意愿）切换督导风格。
- **[socratic-questioning](skills/thinking-models/socratic-questioning/SKILL.md)** — 苏格拉底式质疑：用诘问检验主张是否站得住——追问到矛盾显现，而非直接反驳。
- **[spiral-of-silence](skills/thinking-models/spiral-of-silence/SKILL.md)** — 沉默的螺旋：诊断「怕被孤立→误判意见气候→少数派沉默→优势意见更响」的舆论动力。
- **[ten-ten-ten](skills/thinking-models/ten-ten-ten/SKILL.md)** — 10/10/10：从当下强烈情绪拉开时间距离，分别写出约 10 分钟/10 个月/10 年的后果。

### 认知与思维工具（28）

第一性原理、结构化拆解、批判性思维等认知工具。

- **[abstraction-ladder](skills/cognitive-thinking-tools/abstraction-ladder/SKILL.md)** — 抽象阶梯：在具体与抽象之间有意识上下钻（草稿；≠ 推论阶梯）。
- **[analogical-thinking](skills/cognitive-thinking-tools/analogical-thinking/SKILL.md)** — 类比思维：结构映射迁移并检验失效边界（草稿）。
- **[backward-goal](skills/cognitive-thinking-tools/backward-goal/SKILL.md)** — 反向目标：从可验收终态倒推到今日动作（草稿）。
- **[concept-map](skills/cognitive-thinking-tools/concept-map/SKILL.md)** — 概念图：概念+连接词构成命题网络（草稿）。
- **[critical-thinking](skills/cognitive-thinking-tools/critical-thinking/SKILL.md)** — 批判性思维：按 Facione Delphi 框架练诠释、分析、评估、推理、说明与自我校准。
- **[cross-validation-thinking](skills/cognitive-thinking-tools/cross-validation-thinking/SKILL.md)** — 交叉验证：多独立证据路径核验主张（草稿；≠ ML k-fold）。
- **[decision-matrix](skills/cognitive-thinking-tools/decision-matrix/SKILL.md)** — 决策矩阵：多标准加权评分与敏感性（草稿；概率树见决策与概率）。
- **[diamond-six-steps](skills/cognitive-thinking-tools/diamond-six-steps/SKILL.md)** — 菱形六步法：两轮发散—收敛门控（草稿）。
- **[first-principles](skills/cognitive-thinking-tools/first-principles/SKILL.md)** — 第一性原理：把判断拆到硬事实/物理约束，再从约束重新往上构建，少靠类比。
- **[five-whys](skills/cognitive-thinking-tools/five-whys/SKILL.md)** — 5Why：沿因果链追问至可行动根因（草稿）。
- **[golden-circle](skills/cognitive-thinking-tools/golden-circle/SKILL.md)** — 黄金圈：按 WHY–HOW–WHAT 整理沟通与策略叙事，先目的再方法再产品。
- **[hypothesis-testing](skills/cognitive-thinking-tools/hypothesis-testing/SKILL.md)** — 假设检验：写成可证伪命题并设计对照证据（草稿）。
- **[inversion](skills/cognitive-thinking-tools/inversion/SKILL.md)** — 逆向思维：从失败倒推——先问「怎样保证搞砸」，再把每条失败路径变成规避项。
- **[lateral-thinking](skills/cognitive-thinking-tools/lateral-thinking/SKILL.md)** — 水平思考：用挑衅/跳框逃离定势后再垂直评估（草稿）。
- **[logic-tree](skills/cognitive-thinking-tools/logic-tree/SKILL.md)** — 逻辑树：把主问题拆成可行动的议题/假设叶子（草稿）。
- **[mece](skills/cognitive-thinking-tools/mece/SKILL.md)** — MECE：把议题拆成相互独立、完全穷尽的类别，便于分析与分工。
- **[mind-map](skills/cognitive-thinking-tools/mind-map/SKILL.md)** — 思维导图：中心放射的层级联想笔记与外化（草稿）。
- **[occams-razor](skills/cognitive-thinking-tools/occams-razor/SKILL.md)** — 奥卡姆剃刀：在同样能解释现象的假设中，优先所需特设假设更少者，再验证。
- **[octopus-diagram](skills/cognitive-thinking-tools/octopus-diagram/SKILL.md)** — 八爪鱼图：中心主题+多腕足维度盘点（草稿）。
- **[pros-cons-list](skills/cognitive-thinking-tools/pros-cons-list/SKILL.md)** — 优劣势清单：利弊并列扫描（草稿；加权走决策矩阵）。
- **[pyramid-principle](skills/cognitive-thinking-tools/pyramid-principle/SKILL.md)** — 金字塔原理：结论先行，上层概括下层，同层 MECE 组织论证与沟通。
- **[scqa](skills/cognitive-thinking-tools/scqa/SKILL.md)** — SCQA：情境–冲突–问题–答案的开场与问题定义（草稿）。
- **[six-thinking-hats](skills/cognitive-thinking-tools/six-thinking-hats/SKILL.md)** — 六顶思考帽：把会议中的事实、感受、利益、风险与创意分时并行处理。
- **[star-method](skills/cognitive-thinking-tools/star-method/SKILL.md)** — STAR：情境–任务–行动–结果的经历叙事（草稿）。
- **[structured-thinking](skills/cognitive-thinking-tools/structured-thinking/SKILL.md)** — 结构化思维：问题定义→拆解→分析→综合的总流程（草稿）。
- **[theory-of-constraints](skills/cognitive-thinking-tools/theory-of-constraints/SKILL.md)** — TOC 约束理论：聚焦系统吞吐瓶颈的五步法（草稿）。
- **[thought-experiment](skills/cognitive-thinking-tools/thought-experiment/SKILL.md)** — 思维实验：反事实设定中澄清原则并声明限度（草稿）。
- **[triz](skills/cognitive-thinking-tools/triz/SKILL.md)** — TRIZ：把设计矛盾结构化并用分离/发明原理启发非折中解（草稿）。

### 决策与概率（24）

期望值、决策树、贝叶斯、蒙特卡洛、决策日志/复盘等不确定性决策工具（含 M2 + M2b draft）。

- **[after-action-review](skills/decision-probability/after-action-review/SKILL.md)** — 复盘四步法（AAR）：意图→实际→落差→下次（draft）。
- **[asymmetric-payoff](skills/decision-probability/asymmetric-payoff/SKILL.md)** — 不对称回报：比较上行/下行损益形状（draft）。
- **[base-rate](skills/decision-probability/base-rate/SKILL.md)** — 基率/参考类：先锚定同类频率再并入个案（draft）。
- **[bayesian-updating](skills/decision-probability/bayesian-updating/SKILL.md)** — 贝叶斯更新：先验 × 似然 → 后验（draft）。
- **[decision-journal](skills/decision-probability/decision-journal/SKILL.md)** — 决策日志：预注册信念与预测，事后校准（draft）。
- **[decision-tree](skills/decision-probability/decision-tree/SKILL.md)** — 决策树：在选项已知、结果不确定、能粗估概率与后果时，做多阶段选择与期望值比较。
- **[expected-utility](skills/decision-probability/expected-utility/SKILL.md)** — 期望效用：金额非线性或存在归零约束时用 EU（draft）。
- **[expected-value](skills/decision-probability/expected-value/SKILL.md)** — 期望值：把不确定结果量化为概率加权平均（EV = Σ pᵢ·xᵢ）。
- **[grey-thinking](skills/decision-probability/grey-thinking/SKILL.md)** — 灰度认知：用可修订置信度替代非黑即白（draft）。
- **[loss-function](skills/decision-probability/loss-function/SKILL.md)** — 损失函数：非对称错误代价下的行动/阈值（draft）。
- **[monte-carlo](skills/decision-probability/monte-carlo/SKILL.md)** — 蒙特卡洛：对不确定输入抽样得结果分布（draft）。
- **[mvp](skills/decision-probability/mvp/SKILL.md)** — MVP：以最小投入验证最危险假设（draft）。
- **[ooda-loop](skills/decision-probability/ooda-loop/SKILL.md)** — OODA：观察—定向—决策—行动的对抗节奏（draft）。
- **[oz-principle](skills/decision-probability/oz-principle/SKILL.md)** — 奥兹原则：Above the Line 问责四步（draft）。
- **[planning-fallacy](skills/decision-probability/planning-fallacy/SKILL.md)** — 计划谬误：用外部视图纠偏乐观工期/成本（draft）。
- **[pre-mortem](skills/decision-probability/pre-mortem/SKILL.md)** — 事前验尸：假定已失败以挖出可预防原因（draft）。
- **[probability-thinking](skills/decision-probability/probability-thinking/SKILL.md)** — 概率论思维：事件定义与概率语言入口（draft）。
- **[rapid-experimentation](skills/decision-probability/rapid-experimentation/SKILL.md)** — 快速试错：有止损的短周期实验序列（draft）。
- **[red-team](skills/decision-probability/red-team/SKILL.md)** — 红队：独立结构化对抗以找出可利用裂口（draft）。
- **[reversible-irreversible](skills/decision-probability/reversible-irreversible/SKILL.md)** — 可逆/不可逆决策：按反悔成本匹配速度与审查（draft）。
- **[risk-premium](skills/decision-probability/risk-premium/SKILL.md)** — 风险溢价：无风险基准之上的风险补偿口径（draft）。
- **[scenario-planning](skills/decision-probability/scenario-planning/SKILL.md)** — 情景规划：少数分歧未来下的稳健选项与预警（draft）。
- **[sensitivity-analysis](skills/decision-probability/sensitivity-analysis/SKILL.md)** — 敏感性分析：找翻转假设与稳健区（draft）。
- **[threshold-effect](skills/decision-probability/threshold-effect/SKILL.md)** — 阈值效应：剂量/规则门槛（≠临界点相变）（draft）。

### 学习与成长（23）

费曼技巧、心流、元认知、遗忘曲线、反脆弱，M3 草稿（刻意练习、间隔重复、成长型思维、深度工作、ZPD、一万小时澄清），以及本批草稿（检索/交错/迁移、双重编码、精细加工、组块、T 型、学习金字塔纠偏、导师制、教中学、元学习、去学习）。

- **[antifragility](skills/learning-growth/antifragility/SKILL.md)** — 反脆弱：设计能从波动与不确定性中获益的策略，而不只是抗住风险。
- **[chunking](skills/learning-growth/chunking/SKILL.md)** — 组块：把离散信息打成可命名的更大单元，降低工作记忆负荷（draft）。
- **[deep-work](skills/learning-growth/deep-work/SKILL.md)** — 深度工作：保护无干扰高认知专注块（主条在本类；效率类仅互链）。
- **[deliberate-practice](skills/learning-growth/deliberate-practice/SKILL.md)** — 刻意练习：针对弱点、有反馈、略超舒适区的训练设计。
- **[dual-coding](skills/learning-growth/dual-coding/SKILL.md)** — 双重编码：言语与示意表征对齐互译，增加提取线索（draft）。
- **[elaborative-interrogation](skills/learning-growth/elaborative-interrogation/SKILL.md)** — 精细加工提问：对命题追问「为什么合理」以锚进知识网（draft）。
- **[feynman-technique](skills/learning-growth/feynman-technique/SKILL.md)** — 费曼技巧：用简单语言「教别人」暴露理解空洞，再修补并复讲。
- **[flow](skills/learning-growth/flow/SKILL.md)** — 心流：当挑战与技能大致匹配、目标清晰且反馈及时时，诊断并调节投入状态。
- **[forgetting-curve](skills/learning-growth/forgetting-curve/SKILL.md)** — 遗忘曲线：解释记忆随时间衰减；复习日程操作见间隔重复。
- **[growth-mindset](skills/learning-growth/growth-mindset/SKILL.md)** — 成长型思维：把能力视为可发展，改写反馈与目标语言（非努力万能鸡汤）。
- **[interleaved-practice](skills/learning-growth/interleaved-practice/SKILL.md)** — 交错练习：混合易混题型以提升辨别与迁移（draft）。
- **[learning-by-teaching](skills/learning-growth/learning-by-teaching/SKILL.md)** — 学习中教：用教学任务强制提取与组织知识（draft）。
- **[learning-pyramid](skills/learning-growth/learning-pyramid/SKILL.md)** — 学习金字塔（谨慎）：纠偏假百分比，降级为主动参与启发式（draft）。
- **[mentorship](skills/learning-growth/mentorship/SKILL.md)** — 导师制：目标—节奏—反馈—渐撤的带教协议（draft）。
- **[meta-learning](skills/learning-growth/meta-learning/SKILL.md)** — 元学习：跨任务选择并实验「如何学」的策略菜单（draft）。
- **[metacognition](skills/learning-growth/metacognition/SKILL.md)** — 元认知：监控并调节自己的认知过程——觉察是否理解、是否用错策略并换方法。
- **[retrieval-practice](skills/learning-growth/retrieval-practice/SKILL.md)** — 检索练习：合上材料主动提取（测试效应），强化保持与诊断（draft）。
- **[spaced-repetition](skills/learning-growth/spaced-repetition/SKILL.md)** — 间隔重复：主动检索 + 递增间隔的 SRS/复习日程。
- **[t-shaped-skills](skills/learning-growth/t-shaped-skills/SKILL.md)** — T 型技能：一纵深可交付 + 多横杠可对话的能力组合（draft）。
- **[ten-thousand-hours](skills/learning-growth/ten-thousand-hours/SKILL.md)** — 一万小时定律（澄清）：纠偏时数神话，导流刻意练习。
- **[transfer-of-learning](skills/learning-growth/transfer-of-learning/SKILL.md)** — 迁移学习：显式设计近/远迁移变式与跨情境验收（draft）。
- **[unlearning](skills/learning-growth/unlearning/SKILL.md)** — 去学习：有管理地退役干扰性旧知识/旧反应（draft）。
- **[zpd](skills/learning-growth/zpd/SKILL.md)** — 最近发展区：独立/支架/做不到三带与渐撤支架。

### 战略与竞争（12）

波特五力、护城河、飞轮、SWOT，以及草稿（蓝海、第二曲线、颠覆式创新、BCG、GE 九宫、麦肯锡 7S、OKR、VRIO）。

- **[bcg-matrix](skills/strategy-competition/bcg-matrix/SKILL.md)** — BCG 矩阵：增长×相对份额四象限指导组合投砍。
- **[blue-ocean](skills/strategy-competition/blue-ocean/SKILL.md)** — 蓝海战略：价值创新与 ERRC 重建买方效用与成本边界。
- **[disruptive-innovation](skills/strategy-competition/disruptive-innovation/SKILL.md)** — 颠覆式创新：低端/新市场轨迹与在位者非对称激励。
- **[economic-moat](skills/strategy-competition/economic-moat/SKILL.md)** — 护城河：评估企业能否在竞争下维持超额回报，并识别壁垒来源与可持续性。
- **[flywheel](skills/strategy-competition/flywheel/SKILL.md)** — 飞轮：设计或诊断互相加强的因果闭环，使每一圈投入提高下一圈效率。
- **[ge-mckinsey-matrix](skills/strategy-competition/ge-mckinsey-matrix/SKILL.md)** — GE-麦肯锡九宫：行业吸引力×竞争实力九格指导投/选/撤。
- **[mckinsey-7s](skills/strategy-competition/mckinsey-7s/SKILL.md)** — 麦肯锡 7S：硬三/软三绕共同价值观对齐，诊断战略落地的组织对齐。
- **[okr](skills/strategy-competition/okr/SKILL.md)** — OKR：鼓舞性目标 + 可度量关键结果对齐与复盘（非待办清单）。
- **[porters-five-forces](skills/strategy-competition/porters-five-forces/SKILL.md)** — 波特五力：在行业层面诊断利润结构——竞争、进入、替代、买方与供方议价。
- **[second-curve](skills/strategy-competition/second-curve/SKILL.md)** — 第二曲线：在第一增长曲线趋缓前启动下一条 S 曲线并管理输血/停投。
- **[swot](skills/strategy-competition/swot/SKILL.md)** — SWOT 分析：盘点内部优势/劣势×外部机会/威胁，并做 SO/WO/ST/WT 匹配导向行动。
- **[vrio](skills/strategy-competition/vrio/SKILL.md)** — VRIO：资源/能力是否有价值、稀缺、难模仿且有组织支持。

### 效率与执行（9）

艾森豪威尔、PDCA，以及 M3 草稿（番茄、GTD、看板、敏捷迭代、精益、关键路径、5S）。深度工作见学习与成长类。

- **[agile-iteration](skills/efficiency-execution/agile-iteration/SKILL.md)** — 敏捷迭代：短时间盒交付可检视增量并检视适应。
- **[critical-path](skills/efficiency-execution/critical-path/SKILL.md)** — 关键路径：项目依赖网络中决定最短工期的最长链。
- **[eisenhower-matrix](skills/efficiency-execution/eisenhower-matrix/SKILL.md)** — 艾森豪威尔矩阵：按紧急×重要分配注意力，优先投入重要但不紧急的事项。
- **[five-s](skills/efficiency-execution/five-s/SKILL.md)** — 5S：整理整顿清扫清洁素养，稳固现场/数字工作区基础。
- **[gtd](skills/efficiency-execution/gtd/SKILL.md)** — GTD：收集-澄清-组织-回顾，落到可信的下一步行动。
- **[kanban](skills/efficiency-execution/kanban/SKILL.md)** — 看板：可视化流 + 限制 WIP 的拉动系统。
- **[lean-thinking](skills/efficiency-execution/lean-thinking/SKILL.md)** — 精益思维：价值流与消除浪费（看板/5S 为其工具层）。
- **[pdca](skills/efficiency-execution/pdca/SKILL.md)** — PDCA：Plan–Do–Check/Study–Act 持续改进循环，每圈带明确假设与度量。
- **[pomodoro](skills/efficiency-execution/pomodoro/SKILL.md)** — 番茄工作法：固定专注-短休时间盒节奏（≠深度工作长块）。

### 系统与复杂（11）

冰山、杠杆、临界点、耗散结构，以及 M4 草稿（涌现、基模、因果回路、存量流量、CAS、网络拓扑）。

- **[causal-loop-diagram](skills/systems-complexity/causal-loop-diagram/SKILL.md)** — 因果回路图：带极性的增强/调节回路并标延迟（草稿）。
- **[complex-adaptive-systems](skills/systems-complexity/complex-adaptive-systems/SKILL.md)** — 复杂适应系统：异质适应主体、局部规则与共同演化（草稿）。
- **[dissipative-structures](skills/systems-complexity/dissipative-structures/SKILL.md)** — 耗散结构：远离平衡经涨落过阈值形成新有序，并靠持续耗散维持。
- **[emergence](skills/systems-complexity/emergence/SKILL.md)** — 涌现：宏观模式由微观互动生成，不可零件属性加总（草稿）。
- **[iceberg-model](skills/systems-complexity/iceberg-model/SKILL.md)** — 冰山模型：器物/行为之下分层规范与基本假设，避免只改水面以上。
- **[leverage](skills/systems-complexity/leverage/SKILL.md)** — 杠杆点：小投入撬动大结构改变（Meadows），不是鼓吹财务杠杆。
- **[scale-free-network](skills/systems-complexity/scale-free-network/SKILL.md)** — 无标度网络：度数幂律与枢纽；优先连接与韧性（草稿）。
- **[small-world-network](skills/systems-complexity/small-world-network/SKILL.md)** — 小世界网络：高聚类 + 短路径；少量长程捷径（草稿）。
- **[stock-and-flow](skills/systems-complexity/stock-and-flow/SKILL.md)** — 存量与流量：浴缸式累积与单位一致的速率（草稿）。
- **[system-archetypes](skills/systems-complexity/system-archetypes/SKILL.md)** — 系统基模：增长上限、舍本逐末等可复用反馈故事（草稿）。
- **[tipping-point](skills/systems-complexity/tipping-point/SKILL.md)** — 临界点：临界质量附近的非线性相变，过阈值可快速翻转。

### 宏观经济学理论（30）

宏观经济学经典理论。

- **[ad-as-model](skills/econ-macro-theories/ad-as-model/SKILL.md)** — AD-AS 模型（AD–AS Model）：总需求与总供给共同决定总体物价水平与总产出。
- **[austrian-school](skills/econ-macro-theories/austrian-school/SKILL.md)** — 奥地利学派（Austrian School）：强调主观价值、企业家发现与自发秩序；警惕人为信用扩张扭曲资本结构。
- **[balance-sheet-recession](skills/econ-macro-theories/balance-sheet-recession/SKILL.md)** — 资产负债表衰退（Balance Sheet Recession）：资产泡沫破裂后，企业优先还债最小化负债，即使利率极低也不愿借钱投资。
- **[creative-destruction](skills/econ-macro-theories/creative-destruction/SKILL.md)** — 创造性破坏（Creative Destruction）：创新通过摧毁旧产品、企业与技能，重建更高生产力的结构。
- **[crowding-out-effect](skills/econ-macro-theories/crowding-out-effect/SKILL.md)** — 挤出效应（Crowding Out）：政府借支推高利率或争夺实资，可能挤压私人投资与消费。
- **[endogenous-growth-theory](skills/econ-macro-theories/endogenous-growth-theory/SKILL.md)** — 内生增长理论（Endogenous Growth Theory）：把知识、人力资本与创新投资内生化，使长期增长由经济决策决定。
- **[fisher-equation](skills/econ-macro-theories/fisher-equation/SKILL.md)** — 费雪方程（Fisher Equation / Quantity Theory (MV=PQ)）：MV=PQ：货币量×流通速度≈物价水平×产出；常用于名义锚定直觉。
- **[impossible-trinity](skills/econ-macro-theories/impossible-trinity/SKILL.md)** — 不可能三角（Impossible Trinity (Mundell–Fleming)）：资本自由流动、固定汇率、独立货币政策三者不可兼得，最多选其二。
- **[invisible-hand](skills/econ-macro-theories/invisible-hand/SKILL.md)** — 看不见的手（Invisible Hand）：分散决策在价格信号下可自发协调资源配置，无需中央指挥官。
- **[is-lm-model](skills/econ-macro-theories/is-lm-model/SKILL.md)** — IS-LM 模型（IS–LM Model）：在物价固定的短期，用利率把产品市场（IS）与货币市场（LM）联立求产出。
- **[juglar-cycle](skills/econ-macro-theories/juglar-cycle/SKILL.md)** — 朱格拉周期（Juglar Cycle）：约 7–11 年的中期商业周期，常与固定资本/设备投资波动相关。
- **[keynesianism](skills/econ-macro-theories/keynesianism/SKILL.md)** — 凯恩斯主义（Keynesianism）：有效需求不足时可逆周期用财政/货币拉动支出，避免长期失业均衡。
- **[kitchin-cycle](skills/econ-macro-theories/kitchin-cycle/SKILL.md)** — 基钦周期（Kitchin Cycle）：约 3–5 年（常称约 40 个月）的短周期，主要与库存调整相关。
- **[kondratiev-wave](skills/econ-macro-theories/kondratiev-wave/SKILL.md)** — 康德拉季耶夫长波（Kondratiev Wave）：主张存在约 40–60 年的技术—价格长周期；证据与机制仍争议。
- **[kuznets-curve](skills/econ-macro-theories/kuznets-curve/SKILL.md)** — 库兹涅茨曲线（Kuznets Curve）：经济发展过程中收入不平等可能先升后降——假说，非必然规律。
- **[laffer-curve](skills/econ-macro-theories/laffer-curve/SKILL.md)** — 拉弗曲线（Laffer Curve）：税率从 0 到 100% 时，税收收入先升后降；过高税率可能少收税。
- **[malthusian-trap](skills/econ-macro-theories/malthusian-trap/SKILL.md)** — 马尔萨斯陷阱（Malthusian Trap）：前工业时代技术进步带来的余粮常被人口增长吞掉，人均难持续上升。
- **[modern-monetary-theory](skills/econ-macro-theories/modern-monetary-theory/SKILL.md)** — 现代货币理论（Modern Monetary Theory (MMT)）：主权法币发行国的硬约束是通胀与实资，而非「像家庭一样先收税再花钱」。
- **[monetarism](skills/econ-macro-theories/monetarism/SKILL.md)** — 货币主义（Monetarism）：通胀归根结底是货币现象；政策宜规则化，少搞相机刺激。
- **[multiplier-effect](skills/econ-macro-theories/multiplier-effect/SKILL.md)** — 乘数效应（Multiplier Effect）：一笔自主支出可通过收入—消费链条放大为更大产出变动。
- **[okuns-law](skills/econ-macro-theories/okuns-law/SKILL.md)** — 奥肯定律（Okun's Law）：实际产出增长相对潜在增速越快，失业率往往下降（经验规则，非恒等）。
- **[phillips-curve](skills/econ-macro-theories/phillips-curve/SKILL.md)** — 菲利普斯曲线（Phillips Curve）：短期通胀与失业常呈权衡；长期可能垂直于自然失业率。
- **[purchasing-power-parity](skills/econ-macro-theories/purchasing-power-parity/SKILL.md)** — 购买力平价（Purchasing Power Parity (PPP)）：长期看，汇率应使一篮子货物在两国的购买力大致相当（相对/绝对 PPP）。
- **[rational-expectations](skills/econ-macro-theories/rational-expectations/SKILL.md)** — 理性预期（Rational Expectations）：公众会利用可得信息预判政策，系统性「欺骗」难以持久生效。
- **[ricardian-equivalence](skills/econ-macro-theories/ricardian-equivalence/SKILL.md)** — 李嘉图等价（Ricardian Equivalence）：在严格假定下，政府发债融资与当期征税对私人消费的影响等价。
- **[solow-growth-model](skills/econ-macro-theories/solow-growth-model/SKILL.md)** — 索洛增长模型（Solow Growth Model）：资本积累有递减；长期人均增长主要靠外生技术进步，储蓄率影响水平非永久增速。
- **[supply-side-economics](skills/econ-macro-theories/supply-side-economics/SKILL.md)** — 供给学派（Supply-Side Economics）：通过减税、放松管制等激励生产端，提高潜在产出而非只刺激需求。
- **[taylor-rule](skills/econ-macro-theories/taylor-rule/SKILL.md)** — 泰勒规则（Taylor Rule）：按通胀偏离目标与产出缺口系统设定政策利率的基准规则。
- **[tobins-q](skills/econ-macro-theories/tobins-q/SKILL.md)** — 托宾 Q（Tobin's Q）：企业市值相对资产重置成本的比值，指引投资意愿：Q>1 倾向扩产。
- **[trickle-down-economics](skills/econ-macro-theories/trickle-down-economics/SKILL.md)** — 涓滴经济学（Trickle-Down Economics）：主张先让上层/资本得利，增长红利再向下渗透惠及大众——证据常弱且易被滥用。

### 微观经济学与市场（30）

微观与市场机制。

- **[adverse-selection](skills/econ-micro-markets/adverse-selection/SKILL.md)** — 逆向选择：签约前，信息劣势方更容易吸引到「不利」的交易对手。
- **[asymmetric-information](skills/econ-micro-markets/asymmetric-information/SKILL.md)** — 信息不对称：交易一方比另一方掌握显著更多的关键信息。
- **[barriers-to-entry](skills/econ-micro-markets/barriers-to-entry/SKILL.md)** — 进入壁垒：阻止或拖延新玩家以竞争姿态入场的障碍。
- **[comparative-advantage](skills/econ-micro-markets/comparative-advantage/SKILL.md)** — 比较优势：专注相对成本最低的领域，再通过交易共赢。
- **[consumer-surplus](skills/econ-micro-markets/consumer-surplus/SKILL.md)** — 消费者剩余：愿付价格与实际支付之间的差额总和。
- **[diminishing-marginal-utility](skills/econ-micro-markets/diminishing-marginal-utility/SKILL.md)** — 边际效用递减：消费越多，每多一份带来的满足感通常越低。
- **[diminishing-returns](skills/econ-micro-markets/diminishing-returns/SKILL.md)** — 边际报酬递减：其他投入固定时，再增加某一投入，产出增量终将下降。
- **[economies-of-scale](skills/econ-micro-markets/economies-of-scale/SKILL.md)** — 规模经济：产量扩大时长期平均成本下降。
- **[economies-of-scope](skills/econ-micro-markets/economies-of-scope/SKILL.md)** — 范围经济：多产品一起生产的总成本低于分开生产之和。
- **[equilibrium-price](skills/econ-micro-markets/equilibrium-price/SKILL.md)** — 均衡价格：供需量相等时的市场出清价格。
- **[externality](skills/econ-micro-markets/externality/SKILL.md)** — 外部性：行为对旁观者造成未在市场价格中反映的影响。
- **[general-equilibrium](skills/econ-micro-markets/general-equilibrium/SKILL.md)** — 一般均衡理论：所有市场同时出清的联动均衡分析。
- **[lemons-market](skills/econ-micro-markets/lemons-market/SKILL.md)** — 柠檬市场：质量信息不对称时，劣质品可能驱逐优质品。
- **[monopolistic-competition](skills/econ-micro-markets/monopolistic-competition/SKILL.md)** — 垄断竞争：众多厂商卖差异化产品，有一定定价权又竞争激烈。
- **[monopoly-natural-monopoly](skills/econ-micro-markets/monopoly-natural-monopoly/SKILL.md)** — 垄断与自然垄断：独占供给；若成本结构使一家生产最便宜，称自然垄断。
- **[moral-hazard](skills/econ-micro-markets/moral-hazard/SKILL.md)** — 道德风险：签约后，一方因不承担全部后果而改变隐藏行为。
- **[oligopoly](skills/econ-micro-markets/oligopoly/SKILL.md)** — 寡头市场：少数几家巨头相互盯着定价与产量。
- **[opportunity-cost](skills/econ-micro-markets/opportunity-cost/SKILL.md)** — 机会成本：互斥选项下被放弃的最佳替代价值。
- **[pareto-efficiency](skills/econ-micro-markets/pareto-efficiency/SKILL.md)** — 帕累托最优：若不损害任何人就无法再改善某人境况的状态。
- **[perfect-competition](skills/econ-micro-markets/perfect-competition/SKILL.md)** — 完全竞争：无数小厂商做同质品，人人都是价格接受者。
- **[price-discrimination](skills/econ-micro-markets/price-discrimination/SKILL.md)** — 价格歧视：对成本相同的商品，向不同买家索取不同价格。
- **[price-elasticity](skills/econ-micro-markets/price-elasticity/SKILL.md)** — 供需价格弹性：数量对价格变化的敏感程度。
- **[principal-agent](skills/econ-micro-markets/principal-agent/SKILL.md)** — 委托-代理问题：代理人不完全按委托人利益行事，因目标与信息不同。
- **[producer-surplus](skills/econ-micro-markets/producer-surplus/SKILL.md)** — 生产者剩余：成交价高于卖方边际成本（或最低愿卖价）的差额。
- **[public-goods](skills/econ-micro-markets/public-goods/SKILL.md)** — 公共物品：非排他且非竞争，市场常供给不足。
- **[signaling](skills/econ-micro-markets/signaling/SKILL.md)** — 信号传递：用高成本、可观测行动证明自己的隐藏类型。
- **[supply-and-demand](skills/econ-micro-markets/supply-and-demand/SKILL.md)** — 供需法则：价格由供给与需求共同决定，不是单边意志。
- **[tragedy-of-the-commons](skills/econ-micro-markets/tragedy-of-the-commons/SKILL.md)** — 公地悲剧：人人可取用的竞争性公共资源，终易被耗尽。
- **[transaction-costs-coase](skills/econ-micro-markets/transaction-costs-coase/SKILL.md)** — 交易成本与科斯定理：产权清晰且交易成本足够低时，当事人可谈判解决外部性；否则制度与企业边界成关键。
- **[veblen-effect](skills/econ-micro-markets/veblen-effect/SKILL.md)** — 凡勃伦效应：价格越高越有人买——因炫耀与地位信号。

### 博弈论与策略（31）

博弈论与策略模型。

- **[auction-theory](skills/game-theory-models/auction-theory/SKILL.md)** — 拍卖理论：规则引导出价策略。
- **[backward-induction](skills/game-theory-models/backward-induction/SKILL.md)** — 逆向归纳法：从最后一步倒推最优决策。
- **[bayesian-games](skills/game-theory-models/bayesian-games/SKILL.md)** — 贝叶斯博弈：不完全信息下的信念博弈。
- **[bounded-rationality](skills/game-theory-models/bounded-rationality/SKILL.md)** — 有限理性与满意化：不求最优只求够好。
- **[boxed-pigs](skills/game-theory-models/boxed-pigs/SKILL.md)** — 智猪博弈：小猪搭大猪便车。
- **[centipede-game](skills/game-theory-models/centipede-game/SKILL.md)** — 蜈蚣博弈：理性早停 vs 现实合作。
- **[chicken-game](skills/game-theory-models/chicken-game/SKILL.md)** — 斗鸡博弈：谁先退让谁输，对撞两败俱伤。
- **[cooperative-games](skills/game-theory-models/cooperative-games/SKILL.md)** — 合作博弈与联盟：集体如何分蛋糕。
- **[coordination-game](skills/game-theory-models/coordination-game/SKILL.md)** — 协调博弈：多均衡下倾向选同一个。
- **[core](skills/game-theory-models/core/SKILL.md)** — 核（Core）：任何联盟都无法改进的分配集。
- **[dictator-game](skills/game-theory-models/dictator-game/SKILL.md)** — 独裁者博弈：无拒绝权下的给予。
- **[evolutionary-stable-strategy](skills/game-theory-models/evolutionary-stable-strategy/SKILL.md)** — 演化博弈与 ESS：演化稳定策略不可被入侵。
- **[folk-theorem](skills/game-theory-models/folk-theorem/SKILL.md)** — 无名氏定理：无限重复下合作可持续。
- **[game-theory](skills/game-theory-models/game-theory/SKILL.md)** — 博弈论（入门切片）：参与人/策略/收益、优势策略、纳什直觉、囚徒困境结构示范。
- **[hawk-dove](skills/game-theory-models/hawk-dove/SKILL.md)** — 鹰鸽博弈：攻击与退让的演化权衡。
- **[matching-theory](skills/game-theory-models/matching-theory/SKILL.md)** — 匹配理论（Gale–Shapley）：稳定匹配求婚算法。
- **[mechanism-design](skills/game-theory-models/mechanism-design/SKILL.md)** — 机制设计：逆向设计规则达成目标。
- **[minimax-theorem](skills/game-theory-models/minimax-theorem/SKILL.md)** — 最小最大定理：零和最优防御。
- **[nash-equilibrium](skills/game-theory-models/nash-equilibrium/SKILL.md)** — 纳什均衡：无人愿单方面改变策略的稳定态。
- **[positive-negative-sum-game](skills/game-theory-models/positive-negative-sum-game/SKILL.md)** — 正和/负和博弈：合作创造增量、对抗损耗总量。
- **[prisoners-dilemma](skills/game-theory-models/prisoners-dilemma/SKILL.md)** — 囚徒困境：个体理性导致集体非理性。
- **[repeated-games](skills/game-theory-models/repeated-games/SKILL.md)** — 重复博弈：长期互动催生合作（一报还一报）。
- **[schelling-point](skills/game-theory-models/schelling-point/SKILL.md)** — 谢林点：无沟通时自然汇聚的选项。
- **[shapley-value](skills/game-theory-models/shapley-value/SKILL.md)** — 夏普利值：按边际贡献公平分配。
- **[signaling-games](skills/game-theory-models/signaling-games/SKILL.md)** — 信号博弈：发送方与接收方的信息较量。
- **[stag-hunt](skills/game-theory-models/stag-hunt/SKILL.md)** — 猎鹿博弈：合作收益大，但需要互信。
- **[subgame-perfect-equilibrium](skills/game-theory-models/subgame-perfect-equilibrium/SKILL.md)** — 子博弈精炼均衡：剔除不可信威胁。
- **[travelers-dilemma](skills/game-theory-models/travelers-dilemma/SKILL.md)** — 旅行者困境：追求自身最优反而双输。
- **[trust-game](skills/game-theory-models/trust-game/SKILL.md)** — 信任博弈：先付出赌对方回报。
- **[ultimatum-game](skills/game-theory-models/ultimatum-game/SKILL.md)** — 最后通牒博弈：宁可两败俱伤也要惩罚不公。
- **[zero-sum-game](skills/game-theory-models/zero-sum-game/SKILL.md)** — 零和博弈：一方所得必为另一方所失。

### 行为经济学与偏误（30）

前景理论、启发式与系统偏差。

- **[ambiguity-aversion](skills/behavioral-biases/ambiguity-aversion/SKILL.md)** — 模糊厌恶：更怕未知概率而非已知风险，从而拒绝信息不足但期望可能更好的选项。
- **[anchoring](skills/behavioral-biases/anchoring/SKILL.md)** — 锚定效应：首个数字/印象不当牵引后续判断与谈判报价。
- **[attribution-theory](skills/behavioral-biases/attribution-theory/SKILL.md)** — 归因理论：区分把结果解释为内因（特质/努力）还是外因（情境/运气），并警惕归因偏差。
- **[authority-bias](skills/behavioral-biases/authority-bias/SKILL.md)** — 权威效应：因头衔、制服或专家光环而降低独立核验标准。
- **[availability-heuristic](skills/behavioral-biases/availability-heuristic/SKILL.md)** — 易得性启发：把容易想起、最近看到或生动极端的案例误当成更常见、更可能。
- **[commitment-consistency](skills/behavioral-biases/commitment-consistency/SKILL.md)** — 承诺与一致：小承诺如何升级为大顺从，或用公开承诺对抗现时偏差。
- **[confirmation-bias](skills/behavioral-biases/confirmation-bias/SKILL.md)** — 确认性偏差：按已有信念筛选、记忆与解读证据，低估矛盾信息。
- **[decoy-effect](skills/behavioral-biases/decoy-effect/SKILL.md)** — 诱饵效应：不对称劣势的第三选项被加入，以操纵两选项间的份额。
- **[default-effect](skills/behavioral-biases/default-effect/SKILL.md)** — 默认效应：预设选项（如器官捐赠、养老金、隐私勾选）左右大多数人的选择。
- **[dunning-kruger](skills/behavioral-biases/dunning-kruger/SKILL.md)** — 邓宁-克鲁格效应：表现较差者常高估相对水平；用于校准能力自评。
- **[endowment-effect](skills/behavioral-biases/endowment-effect/SKILL.md)** — 禀赋效应：仅因「已经拥有」就显著抬高估值，阻碍交易与换仓。
- **[framing-effect](skills/behavioral-biases/framing-effect/SKILL.md)** — 框架效应：同一客观结果因表述方式（救活/死亡、折扣/罚款）而改变选择。
- **[gamblers-fallacy](skills/behavioral-biases/gamblers-fallacy/SKILL.md)** — 赌徒谬误：误以为独立随机序列会自我纠错（「该出反面了」）。
- **[hindsight-bias](skills/behavioral-biases/hindsight-bias/SKILL.md)** — 事后聪明偏误：结果揭晓后夸大自己「事先就知道」的程度，扭曲学习与问责。
- **[hot-hand-fallacy](skills/behavioral-biases/hot-hand-fallacy/SKILL.md)** — 热手谬误：把随机或弱相关的连胜当成「状态火热、应加码追击」。
- **[hyperbolic-discounting](skills/behavioral-biases/hyperbolic-discounting/SKILL.md)** — 双曲贴现：对近未来奖励/成本过度敏感，导致时间不一致（计划明天、今晚破功）。
- **[illusion-of-control](skills/behavioral-biases/illusion-of-control/SKILL.md)** — 控制错觉：高估自己对随机或不可控结果的影响力。
- **[law-of-small-numbers](skills/behavioral-biases/law-of-small-numbers/SKILL.md)** — 小数定律：把过小样本的波动当成稳定规律。
- **[loss-aversion](skills/behavioral-biases/loss-aversion/SKILL.md)** — 损失规避：相对参照点，同等得失下损失被加权更重，从而扭曲选择。
- **[mental-accounting](skills/behavioral-biases/mental-accounting/SKILL.md)** — 心理账户：把本可互换的钱/资源分进不同心理抽屉，导致不一致决策。
- **[overconfidence](skills/behavioral-biases/overconfidence/SKILL.md)** — 过度自信：高估知识精度、控制力或相对排名，导致仓位过大或计划过满。
- **[peak-end-rule](skills/behavioral-biases/peak-end-rule/SKILL.md)** — 峰终定律：一段体验的事后评价大致由峰值与结尾主导。
- **[prospect-theory](skills/behavioral-biases/prospect-theory/SKILL.md)** — 前景理论：参照点依赖、价值函数（收益凹/损失凸）与概率加权的风险决策框架。
- **[reciprocity](skills/behavioral-biases/reciprocity/SKILL.md)** — 互惠原理：识别「先给予再索取」如何制造回报压力——用于防操纵或正当合作设计。
- **[representativeness-heuristic](skills/behavioral-biases/representativeness-heuristic/SKILL.md)** — 代表性启发：用「像不像典型故事」代替概率与基率来判断。
- **[scarcity-principle](skills/behavioral-biases/scarcity-principle/SKILL.md)** — 稀缺原理：「限量/倒计时/独家」抬高主观价值，未必反映真实约束。
- **[social-proof](skills/behavioral-biases/social-proof/SKILL.md)** — 社会认同：因「别人都这样」而跟从，尤其在不确定情境。
- **[status-quo-bias](skills/behavioral-biases/status-quo-bias/SKILL.md)** — 现状偏差：仅因「现在如此」就偏好维持，哪怕切换的期望净收益更高。
- **[sunk-cost](skills/behavioral-biases/sunk-cost/SKILL.md)** — 沉没成本：判断要不要继续时，忽略已经发生且不可收回的投入。
- **[survivorship-bias](skills/behavioral-biases/survivorship-bias/SKILL.md)** — 幸存者偏差：只从活下来的样本推断成功法则，失败者已被筛选机制抹去。

### 金融与投资（30）

金融与投资模型。

- **[beta-alpha](skills/finance-investing-models/beta-alpha/SKILL.md)** — β 与 α：把收益拆成市场（或其他因子）暴露 β 与无法被暴露解释的截距 α。
- **[black-scholes](skills/finance-investing-models/black-scholes/SKILL.md)** — 布莱克-斯科尔斯：理解欧式期权定价直觉；关键输入常是隐含波动率。
- **[bubble-cycle](skills/finance-investing-models/bubble-cycle/SKILL.md)** — 泡沫周期：把狂热拆成可检查阶段，对照杠杆、叙事与估值偏离。
- **[cantillon-effect](skills/finance-investing-models/cantillon-effect/SKILL.md)** — 坎蒂隆效应：新增货币/信贷的分配效应——先到者受益、后到者承担价格上行。
- **[capm](skills/finance-investing-models/capm/SKILL.md)** — CAPM：预期收益 = 无风险利率 + β×市场风险溢价；区分可分散与系统风险。
- **[compounding](skills/finance-investing-models/compounding/SKILL.md)** — 复利：评估长期增长是否具备「回报再投入 × 速率可维持 × 时间足够」三条件。
- **[dcf](skills/finance-investing-models/dcf/SKILL.md)** — 贴现现金流：把未来现金流折成今日价值；先写清现金流、折现率与终值假设。
- **[dividend-discount-model](skills/finance-investing-models/dividend-discount-model/SKILL.md)** — 股利贴现模型：把股票看成未来股息的现值（Gordon / 多阶段 DDM）。
- **[duration-convexity](skills/finance-investing-models/duration-convexity/SKILL.md)** — 久期与凸性：用久期衡量债价对利率的一阶敏感，用凸性修正二阶弯曲。
- **[efficient-market-hypothesis](skills/finance-investing-models/efficient-market-hypothesis/SKILL.md)** — 有效市场假说：检验价格是否已反映可用信息、主动战胜市场是否可预期。
- **[fama-french-three-factor](skills/finance-investing-models/fama-french-three-factor/SKILL.md)** — Fama-French 三因子：把超额收益分解为市场、规模（SMB）、价值（HML）暴露。
- **[financial-accelerator](skills/finance-investing-models/financial-accelerator/SKILL.md)** — 金融加速器：解释资产价格与信贷约束的互馈放大。
- **[fisher-effect](skills/finance-investing-models/fisher-effect/SKILL.md)** — 费雪效应：名义利率 ≈ 实际利率 + 预期通胀；统一名义/实际口径。
- **[greater-fool-theory](skills/finance-investing-models/greater-fool-theory/SKILL.md)** — 大傻瓜理论：买入只为卖给下一个愿出更高价的人。
- **[investment-clock](skills/finance-investing-models/investment-clock/SKILL.md)** — 投资时钟：按增长与通胀组合划分四季，映射大类资产战术倾向。
- **[kelly-criterion](skills/finance-investing-models/kelly-criterion/SKILL.md)** — 凯利公式：按胜率与赔率定最优仓位分数；实务常用分数凯利。
- **[limits-to-arbitrage](skills/finance-investing-models/limits-to-arbitrage/SKILL.md)** — 套利限制：解释错误定价为何不迅速消失。
- **[liquidity-preference](skills/finance-investing-models/liquidity-preference/SKILL.md)** — 流动性偏好：理解持币三类动机与利率。
- **[minsky-moment](skills/finance-investing-models/minsky-moment/SKILL.md)** — 明斯基时刻：稳定滋生杠杆与投机，直至再融资断裂的转折。
- **[modern-portfolio-theory](skills/finance-investing-models/modern-portfolio-theory/SKILL.md)** — 现代投资组合理论：用均值–方差框架做分散化与有效前沿。
- **[momentum-reversal](skills/finance-investing-models/momentum-reversal/SKILL.md)** — 动量与反转：组织价格续涨 / 极端回吐的实证规律。
- **[noise-trader-risk](skills/finance-investing-models/noise-trader-risk/SKILL.md)** — 噪音交易者风险：正确也可能因非理性推价而被迫亏钱离场。
- **[pe-pb-valuation](skills/finance-investing-models/pe-pb-valuation/SKILL.md)** — 市盈率 / 市净率：相对估值放到可比组与历史分位中读贵贱。
- **[rebalancing](skills/finance-investing-models/rebalancing/SKILL.md)** — 再平衡：把组合权重纪律化拉回目标（时间或阈值触发）。
- **[risk-parity](skills/finance-investing-models/risk-parity/SKILL.md)** — 风险平价：按风险贡献（而非资金权重）分配资产。
- **[rule-of-72](skills/finance-investing-models/rule-of-72/SKILL.md)** — 72 法则：快速估算复利翻倍年数（心算层，不替代精确复利）。
- **[sharpe-ratio](skills/finance-investing-models/sharpe-ratio/SKILL.md)** — 夏普比率：衡量单位总波动的超额报酬。
- **[stock-bond-seesaw](skills/finance-investing-models/stock-bond-seesaw/SKILL.md)** — 股债跷跷板：风险偏好切换下股与债常反向的经验结构。
- **[value-premium](skills/finance-investing-models/value-premium/SKILL.md)** — 价值溢价：低估值组合长期平均超额（含长回撤）。
- **[yield-curve](skills/finance-investing-models/yield-curve/SKILL.md)** — 收益率曲线：用期限结构读预期、期限溢价与宏观含义。

### 系统与经典效应（30）

系统动力学与经典效应。

- **[barrel-effect](skills/systems-classic-effects/barrel-effect/SKILL.md)** — 木桶效应：系统有效容量由最短板 / 最紧约束决定。
- **[black-swan](skills/systems-classic-effects/black-swan/SKILL.md)** — 黑天鹅：稀有、冲击大、事后可叙事的极端事件。
- **[boiling-frog](skills/systems-classic-effects/boiling-frog/SKILL.md)** — 温水煮青蛙：渐进恶化中的基线麻木（隐喻）。
- **[broken-windows](skills/systems-classic-effects/broken-windows/SKILL.md)** — 破窗效应：小失序信号被放任后诱发更大失序。
- **[butterfly-effect](skills/systems-classic-effects/butterfly-effect/SKILL.md)** — 蝴蝶效应：敏感依赖 / SDIC：微小初值差在非线性系统中放大，长期预报失效。
- **[catfish-effect](skills/systems-classic-effects/catfish-effect/SKILL.md)** — 鲶鱼效应：引入可信竞争刺激以激活惰性群体。
- **[domino-effect](skills/systems-classic-effects/domino-effect/SKILL.md)** — 多米诺骨牌效应：沿耦合链的逐步连锁触发。
- **[entropy-increase](skills/systems-classic-effects/entropy-increase/SKILL.md)** — 熵增定律：孤立系统趋向无序；组织隐喻需划清边界。
- **[feedback-loops](skills/systems-classic-effects/feedback-loops/SKILL.md)** — 反馈回路：增强回路与调节回路的极性与干预。
- **[free-rider-effect](skills/systems-classic-effects/free-rider-effect/SKILL.md)** — 搭便车效应：享受集体收益却少付成本，公共品供给不足。
- **[gray-rhino](skills/systems-classic-effects/gray-rhino/SKILL.md)** — 灰犀牛：高概率大冲击且已在视野内却仍被拖延。
- **[halo-effect](skills/systems-classic-effects/halo-effect/SKILL.md)** — 光环效应：单一突出特质不当外推到整体评价。
- **[hawthorne-effect](skills/systems-classic-effects/hawthorne-effect/SKILL.md)** — 霍桑效应：被观察本身改变行为，污染因果解释。
- **[lock-in-effect](skills/systems-classic-effects/lock-in-effect/SKILL.md)** — 锁定效应：转换成本困住用户或组织。
- **[long-tail](skills/systems-classic-effects/long-tail/SKILL.md)** — 长尾理论：分发成本足够低时，利基需求聚合可观。
- **[matthew-effect](skills/systems-classic-effects/matthew-effect/SKILL.md)** — 马太效应：累积优势使强者愈强、弱者愈弱。
- **[metcalfes-law](skills/systems-classic-effects/metcalfes-law/SKILL.md)** — 梅特卡夫法则：兼容网络潜在连接数近似随节点数平方增长。
- **[murphys-law](skills/systems-classic-effects/murphys-law/SKILL.md)** — 墨菲定律：可能出错且机会足够则终将出错——用于防呆。
- **[pareto-principle](skills/systems-classic-effects/pareto-principle/SKILL.md)** — 二八定律：少数原因贡献多数结果；先度量集中度再分配精力。
- **[parkinsons-law](skills/systems-classic-effects/parkinsons-law/SKILL.md)** — 帕金森定律：工作 / 组织膨胀到填满可用时间与编制。
- **[path-dependence](skills/systems-classic-effects/path-dependence/SKILL.md)** — 路径依赖：历史选择经报酬递增等机制锁住未来方向。
- **[peter-principle](skills/systems-classic-effects/peter-principle/SKILL.md)** — 彼得原理：因胜任而被晋升到不胜任的层级。
- **[projection-effect](skills/systems-classic-effects/projection-effect/SKILL.md)** — 投射效应：以己度人、把自我模型安到他人头上。
- **[pygmalion-effect](skills/systems-classic-effects/pygmalion-effect/SKILL.md)** — 皮格马利翁效应：期望通过对待差异塑造实际表现。
- **[ratchet-effect](skills/systems-classic-effects/ratchet-effect/SKILL.md)** — 棘轮效应：消费 / 待遇 / 标准易升难降。
- **[second-order-thinking](skills/systems-classic-effects/second-order-thinking/SKILL.md)** — 二阶思维：追问“然后呢”：后果的后果与他人反应。
- **[serial-position-effect](skills/systems-classic-effects/serial-position-effect/SKILL.md)** — 系列位置效应：有序信息中开头（首因）与结尾（近因）更易被记住。
- **[stereotyping](skills/systems-classic-effects/stereotyping/SKILL.md)** — 刻板印象：用群体标签替代个体证据。
- **[system-dynamics](skills/systems-classic-effects/system-dynamics/SKILL.md)** — 系统动力学：存量、流量、延迟的动态建模与政策实验。
- **[systems-thinking](skills/systems-classic-effects/systems-thinking/SKILL.md)** — 系统思维：从事件升到行为模式、存量流量、反馈与杠杆点。

---

[English](README.md)
