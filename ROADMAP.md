# ROADMAP — modelosophy 工作计划

记录项目当前进展：哪些工作已经完整交付，哪些还在待办队列。按主题分组，而不是按时间顺序。

## 已完成

### 项目定位与文档骨架
- README.md / README.zh-CN.md：确立"万物皆模型"定位、双语同步、图示化 hero/mechanism 资源（`assets/readme/`）。
- DESIGN.md：HTML 报告类 Skill 的统一视觉规范。
- CLAUDE.md：Skill 生产流程（cangjie-skill 蒸馏 → internal/skill-creator 官方规范校验两阶段）、行为准则、Git 工作流规则（本地文件，不进 GitHub）。

### Skill 目录规范化
- `skills/` 改为按领域分类：`skills/<category>/<name>/`。
- 原 `skills/sales-company-intel-report/` 迁入 `skills/business/`，并去品牌重命名为 `org-it-intel-report`（组织 IT 情报报告）。
- 输出约定：Skill 生成的报告统一写入 `output/<skill-name>/`（gitignored，不进仓库）。

### thinking-models 思维模型库（现 **25** 个）
蒸馏自《万物皆模型》100个思维模型书 + 各自真实学科来源，走完 cangjie-skill 五阶段流水线 + skill-creator 官方规范校验。索引见 [`skills/thinking-models/README.md`](skills/thinking-models/README.md)。

曾累计 69 个（含苏格拉底式质疑）；其中 **19** 个与经济学/行为/系统效应明确对应的可执行 Skill 已于 2026-08-16 **物理迁出**至六分类；另 **25** 个按名录第七–十二类再迁出（见「已完成：名录对账与第七–十二类迁入」）。`thinking-models/` 原路径已删除，不留 stub。

批次史（路径以迁出前为准）：第五–八批等仍记于 git 历史；迁出清单见各分类 README。

已完成的验证环节：
- 苏格拉底式质疑自检（定稿前强制；审计见本机 `docs/books/wanwu-jie-moxing/socratic-review.md`）
- 盲测与官方 Skill 规范校验；每个 skill 含 `evals/`

### 已完成：六分类迁入（可执行 Skill，平级目录）

**决策锁定（2026-08-16）**：

| 项 | 约定 |
|---|---|
| 主交付 | **可执行 Skill**（何时用 / 怎么用 / 边界 / 相关模型），与 `thinking-models/` 同形态 |
| 目录 | **6 个分类与 `business/`、`thinking-models/` 平级**（**无** `skills/Economics/` 父目录） |
| 知识卡 | **废弃**「9 字段知识卡容器」作为主交付；有用字段（提出者、常见误用、记忆钩子等）可**吸收进**可执行 `SKILL.md` |
| 迁移动作 | ROADMAP 复用表「明确对应」条目 **整目录 `git mv`**；`thinking-models/` **原路径删除**（不留 stub） |
| 不迁（六分类轮） | 当时「仅部分相关」：`economic-moat`、`porters-five-forces`、`long-term-thinking` 仍留 `thinking-models/`；其中前两者已在**名录扩充分类轮**迁入 `strategy-competition/` |

**六分类路径（Batch A/B 补全后实际数量，2026-08-16 对账）**：

| # | 中文 | `category` | 含 `SKILL.md` 子目录数 | 备注 |
|---|---|---|---|---|
| 1 | 宏观经济理论与模型 | `econ-macro-theories` | **30** | 全部新建 draft |
| 2 | 微观经济与市场机制 | `econ-micro-markets` | **30** | 含迁入 `opportunity-cost` |
| 3 | 博弈论与策略模型 | `game-theory-models` | **31** | 30 专条 + 迁入总论 `game-theory` |
| 4 | 行为经济学与认知偏误 | `behavioral-biases` | **30** | 含迁入 9 个 |
| 5 | 金融与投资模型 | `finance-investing-models` | **30** | 含迁入 `compounding` |
| 6 | 系统思维与经典效应 | `systems-classic-effects` | **30** | 含迁入 7 个 |

合计：迁入种子 **19** + 分批新建补齐至上表；索引见各 `skills/<category>/README.md`。名录扩充分类轮后 `thinking-models/` 为 **25**（护城河/五力已迁 `strategy-competition/`；`long-term-thinking` 仍留）。

**本轮 `git mv` 清单（`thinking-models/` → 目标；原路径已删）：**

```
opportunity-cost          → skills/econ-micro-markets/opportunity-cost
game-theory               → skills/game-theory-models/game-theory
prospect-theory           → skills/behavioral-biases/prospect-theory
loss-aversion             → skills/behavioral-biases/loss-aversion
sunk-cost                 → skills/behavioral-biases/sunk-cost
confirmation-bias         → skills/behavioral-biases/confirmation-bias
availability-heuristic    → skills/behavioral-biases/availability-heuristic
survivorship-bias         → skills/behavioral-biases/survivorship-bias
dunning-kruger            → skills/behavioral-biases/dunning-kruger
peak-end-rule             → skills/behavioral-biases/peak-end-rule
attribution-theory        → skills/behavioral-biases/attribution-theory
compounding               → skills/finance-investing-models/compounding
butterfly-effect          → skills/systems-classic-effects/butterfly-effect
pareto-principle          → skills/systems-classic-effects/pareto-principle
long-tail                 → skills/systems-classic-effects/long-tail
path-dependence           → skills/systems-classic-effects/path-dependence
metcalfes-law             → skills/systems-classic-effects/metcalfes-law
systems-thinking          → skills/systems-classic-effects/systems-thinking
serial-position-effect    → skills/systems-classic-effects/serial-position-effect
```

**Phase 状态**：旧 Phase 1「`skills/Economics/` 知识卡容器壳」**作废并已删除**。迁入轮 = 迁 19 + 6 分类 README + 文档/链接修复（**不重写**迁入 Skill 正文为 9 字段）。随后 Batch A/B 已将六分类补至上表数量。

### 已完成：Phase 0 — 可执行 Skill 正文模板

模板已锁定（2026-08-16）：

- 说明与字段吸收表：[`skills/_templates/README.md`](skills/_templates/README.md)
- 可复制正文：[`skills/_templates/EXECUTABLE_SKILL.md`](skills/_templates/EXECUTABLE_SKILL.md)

要点：章节顺序固定（这是什么 → 何时用 → 怎么用 → 例证 → 边界 → **常见误用** → 相关模型 → 可选记忆钩子）；原 9 字段不另建卡，按表吸入上述章节；`business/` 调研类 Skill 不适用本模板。

---

## 已完成：六分类 Batch A/B 补全（接近 30/类）

**对账日**：2026-08-16（分支 `feature/batch-fill-six-categories`）。

| `category` | 实际数量 | 对照预期 |
|---|---|---|
| `econ-macro-theories` | 30 | ✓ 30 |
| `econ-micro-markets` | 30 | ✓ 30 |
| `game-theory-models` | 31 | ✓ 31（30 专条 + `game-theory`） |
| `behavioral-biases` | 30 | ✓ 30 |
| `finance-investing-models` | 30 | ✓ 30 |
| `systems-classic-effects` | 30 | ✓ 30 |
| `thinking-models`（对照） | 25 | 名录扩充分类轮后再迁出 25；护城河/五力已迁战略类 |

- Phase 0 模板已在本分支：[`skills/_templates/EXECUTABLE_SKILL.md`](skills/_templates/EXECUTABLE_SKILL.md)
- 根 README / README.zh-CN 六分类计数与上表一致
- 新建 draft 抽查含「怎么用」「常见误用」；**迁入的 19 个旧稿**已增量补「常见误用」（见 Phase 3）

---

## 待办：六分类后处理与 Phase 3

> **需求来源（本机，不进 GitHub）**：`WorkBuddy/.../经济学思维模型Skills生成需求.md`  
> **本阶段状态**：形态与迁入 **已落地**；**Phase 0 模板已锁定**；**Batch A/B 数量目标已达成**（见上表）；链接抽查 / evals 最小集 / 19 旧稿「常见误用」/ 根 README 全量索引已收拢至 `feature/phase3-readme-consolidate`。  
> **硬约束**（与 CLAUDE.md 一致）：
> - `SKILL.md` 只落在 `skills/<category>/<name>/`
> - 研究/审计轨迹写本机 `docs/books/<slug>/`（随 `docs/` gitignore，**不进 GitHub**）
> - README「目前的进展」只反映 `skills/` 里真实存在的产出
> - 新建 Skill **复制** [`skills/_templates/EXECUTABLE_SKILL.md`](skills/_templates/EXECUTABLE_SKILL.md)

### 1. 目标与交付形态（已确认 · 修订）

| 项 | 约定 |
|---|---|
| 规模 | 需求清单约 **6×30 ≈ 180** 条主题；每条最终为 **一个可执行 Skill 目录**（数量目标已基本达成） |
| 粒度 | 可执行决策步骤全文；可吸收原 9 字段中有用信息，**不是**独立知识卡产品 |
| 语言 | 简体中文；术语首次标注英文/人名；通俗 + 生活化例子 |
| **目录** | `skills/<category-slug>/<skill-slug>/`，六分类与 `business/` / `thinking-models/` **平级** |
| **模板** | [`skills/_templates/`](skills/_templates/)（Phase 0 已锁定） |
| **明确不做** | 不做「知识卡容器」主交付；不做 `skills/Economics/` 父目录；不做 `thinking-models/` 内嵌套 Economics |

### 2. Phase 进度

- [x] **Phase 0**：锁定可执行正文模板 + 9 字段吸收约定 → [`skills/_templates/`](skills/_templates/)
- [x] **Batch A**：每类优先补缺口（宏观从 0 起；其余在已迁种子旁扩展）
- [x] **Batch B**：补到接近需求 30/类（上表对账通过）
- [x] **Phase 3**：分类 README 定稿复核（双向建议见下已完成子项）
  - [x] **相关模型链接抽查**（2026-08-16，`feature/phase3-link-audit`）：`skills/**/SKILL.md` + 各分类 `README.md` 共 **1337** 条相对 `SKILL.md` 链接；死链 / 错误分类路径 / 标签–slug 不一致 **0**（无可修复项）。残留见下「链接审计残留」
  - [x] **可选 evals 最小集**（2026-08-16，`feature/phase3-evals`）：六分类 **181/181** 均有 `evals/test-prompts.json`；新建 draft 补 **132** 条（各约 5 case，对齐宏观样例）；迁入旧稿原有 evals 保留。`quick_validate` 跨类抽查 10/10 通过。**未**做完整盲测；draft 仍 `v0.x-draft`
  - [x] **迁入 19 旧稿「常见误用」**（2026-08-16，`feature/phase3-misuse-backfill` → 收拢）：在「什么时候不适用」与「相关模型」之间补 `## 常见误用`（3–4 条）；`version` 仍为 `v1.0`
  - [x] **根 README 全量 Skill 索引**（2026-08-16，`feature/readme-all-skills-index` → 收拢）：双语根 README 列出仓库内可执行 Skill（约 **232** 条链接量级）
  - [x] **相关模型双向补链**（2026-08-16，`feature/phase3-bidirectional-links`）：对约 **423** 条单向边做优先级筛选（同分类 / 名录易混对 / 迁入种子↔新建稿），**不**机械对称；补反向引用 **149** 条（含一句分流判据）。残留单向边约 **274**（同分类约 **92**，跨类约 **182**）。跳过：弱相关、单向总论→专条且专条侧已足够、对向已有等价分流文案、枢纽节点过密（≥11 链且非易混）等
  - [x] **分类 README 定稿复核**（2026-08-16，`feature/phase3-category-readme-review`）：14 个分类 README 与磁盘 `SKILL.md` 一一对应；统一 mattpocock 列表；补兄弟分流；`thinking-models` 已迁出表路径抽查通过；根 catalog 无漏无幽灵（未大改）

### 3. 本阶段明确不做

- 不恢复 `skills/Economics/` 知识卡壳 / Phase 1 旧容器
- 不以 9 字段卡为主交付；不把本轮已迁 Skill 整篇改写成 9 字段（仅新建按模板；旧稿可选增量补「钩子」等）
- 不把长线思考（`long-term-thinking`）强行迁入六分类；护城河/五力已按名录迁入 `strategy-competition/`（非六分类）
- 不一次性新建大批量 Skill（数量目标已达成；后续仅增量）
- 不把研究笔记写入 GitHub 跟踪路径

### 4. 链接审计残留（不自动改正文）

- 单向「相关模型」边：基线约 **423** → 本轮补反向后约 **274**（同分类 ~92 / 跨类 ~182）。策略见上「相关模型双向补链」；**仍不强制**全库对称。
- 本轮跳过原则：非兄弟/非易混的弱相关边；专条已指向总论且总论侧不必回链的单向；对向已有未链但等价的分流说明；单文件相关节已很密（≥11）且非高优先级易混对。
- `business/org-it-intel-report` 无「相关模型」节：调研类 Skill，预期如此。
- ~~护城河 / 五力 / 长线仍留 `thinking-models/`~~：护城河 / 五力已于名录扩充分类轮迁入 `strategy-competition/`；`long-term-thinking` 仍留 `thinking-models/`（名录无精确对应专条）。

### 5. 建议的下一执行步

1. **Phase 3 剩余**：残留单向「相关模型」边可按需再扫（分类 README 与双向补链均已完成；非阻塞）  

2. **可选**：evals 盲测加厚（非阻塞）
3. **名录第七–十二类**：见下文「待办：名录扩充分类」——本轮已建壳 + 迁入种子；缺口 Skill 按批新建

---

## 已完成：名录对账与第七–十二类迁入（2026-08-16）

> **需求来源（本机，不进 GitHub）**：`WorkBuddy/.../思维模型分类名录.md`（**12 类 × 约 30 条 ≈ 360 主题**；含跨类重复标注）。  
> **分支**：`feature/catalog-roadmap-and-migrate`。  
> **本轮范围**：ROADMAP 写入名录待办 + 新建 6 个分类壳 + 明确对应 Skill **物理 `git mv`**；**不**批量新建缺口正文。

**决策锁定**：

| 项 | 约定 |
|---|---|
| 主交付 | **可执行 Skill**（与六分类 / `thinking-models/` 同形态） |
| 目录 | 名录 1–6 **复用**既有六分类 slug；7–12 **新建**平级 `skills/<category-slug>/`（**无**大一统父目录） |
| 迁移动作 | 名录有明确同主题且已在 `thinking-models/`（或可判定归属）→ **整目录 `git mv`**；原路径删除 |
| 不迁 | 名录无精确对应、易误塞的杂项（如 `dual-process`、`long-term-thinking`、`munger-misjudgment` 等）仍留 `thinking-models/` |
| 重复项 | 名录自注「与第六类重复」等 → **不**再建第二份；ROADMAP 标「已有@既有路径」 |

**本轮 `git mv`（`thinking-models/` → 目标；原路径已删）**：

```
first-principles, occams-razor, inversion, mece, pyramid-principle,
six-thinking-hats, critical-thinking, golden-circle
  → skills/cognitive-thinking-tools/

expected-value, decision-tree
  → skills/decision-probability/

feynman-technique, flow, metacognition, forgetting-curve, antifragility
  → skills/learning-growth/

porters-five-forces, flywheel, economic-moat, swot
  → skills/strategy-competition/

eisenhower-matrix, pdca
  → skills/efficiency-execution/

iceberg-model, leverage, tipping-point, dissipative-structures
  → skills/systems-complexity/
```

合计迁入 **25**；`thinking-models/` 现 **25**；全库 Skill 数仍 **232**（仅搬家）。

---

## 待办：名录扩充分类（第七–十二类 + 与既有六分类对账）

> **硬约束**（与 CLAUDE.md / 六分类一致）：
> - `SKILL.md` 只落在 `skills/<category>/<name>/`
> - 分类目录小写 kebab-case
> - 研究/审计轨迹写本机 `docs/books/<slug>/`（**不进 GitHub**）
> - 新建复制 [`skills/_templates/EXECUTABLE_SKILL.md`](skills/_templates/EXECUTABLE_SKILL.md)；本阶段缺口标 `v0.x-draft`
> - README「目前的进展」只反映 `skills/` 真实存在的产出

### 1. 目标与交付形态

| 项 | 约定 |
|---|---|
| 规模 | 名录 **12 类**；每类约 30 主题；最终每条一个可执行 Skill（跨类重复合并，实际目录数 < 360） |
| 粒度 | 可执行决策步骤全文；非知识卡容器 |
| 语言 | 简体中文；术语首次标注英文/人名 |
| **目录** | 见下表；与 `business/` / `thinking-models/` **平级** |
| **模板** | [`skills/_templates/`](skills/_templates/) |
| **明确不做** | 不为名录再建同义父目录；不把无关 Skill 硬塞错类；本轮不填满新建正文；不把研究笔记写入 GitHub |

### 2. 分类 slug 与现有库关系

| # | 名录中文 | `category` | 与现有库 | 本轮状态 |
|---|---|---|---|---|
| 1 | 宏观经济理论与模型 | `econ-macro-theories` | **复用**六分类 | 名录 30 条 **已有** |
| 2 | 微观经济与市场机制 | `econ-micro-markets` | **复用** | 名录 30 条 **已有** |
| 3 | 博弈论与策略模型 | `game-theory-models` | **复用**（另含总论 `game-theory`） | 名录 30 条 **已有** |
| 4 | 行为经济学与认知偏误 | `behavioral-biases` | **复用** | 名录 30 条 **已有** |
| 5 | 金融与投资模型 | `finance-investing-models` | **复用** | 名录 30 条 **已有** |
| 6 | 系统思维与经典效应 | `systems-classic-effects` | **复用** | 名录 30 条 **已有**（首因/近因→`serial-position-effect`；网络效应→`metcalfes-law`） |
| 7 | 认知与思维工具 | `cognitive-thinking-tools` | **新建**；迁入 8 | 现 **28**（M1 新建 9 + 剩余补齐 11）；名录专条已齐（二阶/SWOT 仍@他类） |
| 8 | 决策与概率 | `decision-probability` | **新建**；迁入 2 | 现 **13**（M2 新建 11）；部分 **已有@他类**；余待新建 |
| 9 | 学习与成长 | `learning-growth` | **新建**；迁入 5 | 现 **11**（M3 新建 6）；余 **待新建** |
| 10 | 战略与竞争 | `strategy-competition` | **新建**；迁入 4 | 现 **10**（M3 新建 6）；余 **待新建** |
| 11 | 效率与执行 | `efficiency-execution` | **新建**；迁入 2 | 现 **9**（M3 新建 7）；余 **待新建** |
| 12 | 系统与复杂 | `systems-complexity` | **新建**；迁入 4；与第六类互补 | 现 **11**（种子 4 + M4 新建 7）；与第六类重复项只互链 |

### 3. 分批里程碑（建议）

- [x] **M0**：名录写入 ROADMAP + 6 个新分类 README 壳 + 25 条物理迁移 + 链接/根 README 对账  
- [x] **M1（首批）**：第七类优先缺口已建 9 条（`five-whys` / `scqa` / `theory-of-constraints` / `triz` / `hypothesis-testing` / `structured-thinking` / `lateral-thinking` / `logic-tree` / `star-method`，均 `v0.x-draft`）
- [x] **M1（第七类剩余）**：补齐 11 条（`analogical-thinking` / `abstraction-ladder` / `cross-validation-thinking` / `backward-goal` / `thought-experiment` / `diamond-six-steps` / `octopus-diagram` / `concept-map` / `mind-map` / `decision-matrix` / `pros-cons-list`，均 `v0.x-draft` + 最小 evals）；类内现 **28**；二阶思维/SWOT 仍为已有@他类不重复建  
- [x] **M2（首批）**：第八类高价值新建 11 条（`bayesian-updating` / `grey-thinking` / `reversible-irreversible` / `mvp` / `red-team` / `pre-mortem` / `ooda-loop` / `planning-fallacy` / `scenario-planning` / `expected-utility` / `base-rate`，均 `v0.x-draft`）；类内现 **13**；沉没/机会成本/凯利/满意化/临界/杠铃 **只互链不复制**；名录其余条仍待新建  
- [x] **M3（首批）**：第九–十一类已建 draft（学习 +6→11；战略 +6→10；效率 +7→9；`deep-work` 落学习类）。分支 `feature/m3-learning-strategy-efficiency`；其余名录条仍待新建  
- [x] **M4（首批）**：第十二类新建 7 条（`emergence` / `system-archetypes` / `causal-loop-diagram` / `stock-and-flow` / `complex-adaptive-systems` / `small-world-network` / `scale-free-network`，均 `v0.x-draft`）；类内现 **11**；路径依赖/锁定/网络效应/熵增/反馈等仍@`systems-classic-effects` 只互链  
- [x] **M5**：跨类相关模型抽查 + 分类 README 定稿；可选 evals 最小集（见 Phase 3 子项；双向建议仍可选残留）  

### 4. 条目状态速查（第七–十二类）

状态约定：`已有@path` = 仓库已有可执行 Skill；`待新建` = 尚无专条（括号内为建议 slug）；`已有@他类` = 主题已在其他分类，本类不重复建。

#### 七、`cognitive-thinking-tools`

| 名录 | 状态 |
|---|---|
| 第一性原理 | 已有@`cognitive-thinking-tools/first-principles` |
| 奥卡姆剃刀 | 已有@`…/occams-razor` |
| 逆向思维 | 已有@`…/inversion` |
| 二阶思维 | 已有@他类 `systems-classic-effects/second-order-thinking`（名录可合并） |
| MECE | 已有@`…/mece` |
| 金字塔原理 | 已有@`…/pyramid-principle` |
| 六顶思考帽 | 已有@`…/six-thinking-hats` |
| 5Why 分析法 | 已有@`cognitive-thinking-tools/five-whys`（`v0.x-draft`；勿与 `five-w-one-h` 混淆） |
| 结构化思维 | 已有@`…/structured-thinking`（`v0.x-draft`） |
| 批判性思维 | 已有@`…/critical-thinking` |
| 水平思考 | 已有@`…/lateral-thinking`（`v0.x-draft`） |
| 类比思维 | 已有@`…/analogical-thinking`（`v0.x-draft`） |
| 抽象阶梯 | 已有@`…/abstraction-ladder`（`v0.x-draft`；≠ `ladder-of-inference`） |
| 黄金圈法则 | 已有@`…/golden-circle` |
| SCQA 框架 | 已有@`…/scqa`（`v0.x-draft`） |
| STAR 法则 | 已有@`…/star-method`（`v0.x-draft`） |
| SWOT 分析 | 已有@他类 `strategy-competition/swot`（战略主条；认知场景互链） |
| 交叉验证 | 已有@`…/cross-validation-thinking`（`v0.x-draft`） |
| 反向目标 | 已有@`…/backward-goal`（`v0.x-draft`） |
| 思维实验 | 已有@`…/thought-experiment`（`v0.x-draft`） |
| 菱形六步法 | 已有@`…/diamond-six-steps`（`v0.x-draft`） |
| TOC 约束理论 | 已有@`…/theory-of-constraints`（`v0.x-draft`） |
| TRIZ 发明原理 | 已有@`…/triz`（`v0.x-draft`） |
| 八爪鱼图 / 概念图 / 思维导图 / 逻辑树 | 已有@`…/octopus-diagram` / `concept-map` / `mind-map` / `logic-tree`（均 `v0.x-draft`） |
| 决策矩阵 / 优劣势清单 / 假设检验 | 均已有@`…/decision-matrix` · `pros-cons-list` · `hypothesis-testing`（`v0.x-draft`；矩阵/利弊与第八类决策树在相关模型分流） |

#### 八、`decision-probability`

| 名录 | 状态 |
|---|---|
| 期望值思维 | 已有@`decision-probability/expected-value` |
| 贝叶斯更新 | 已有@`…/bayesian-updating`（`v0.x-draft`；≠ `bayesian-games`） |
| 决策树 | 已有@`…/decision-tree` |
| 概率论思维 | 待新建（`probability-thinking`；可与基率/贝叶斯互链，避免空壳总论） |
| 灰度认知 | 已有@`…/grey-thinking`（`v0.x-draft`） |
| 可逆与不可逆决策 | 已有@`…/reversible-irreversible`（`v0.x-draft`） |
| 杠铃策略 / 反脆弱相关 | 部分已有@他类 `learning-growth/antifragility`（杠铃专条可后续拆或互链） |
| 满意化原则 | 已有@他类 `game-theory-models/bounded-rationality`（有限理性与满意化；不复制） |
| 最小可行性产品 | 已有@`…/mvp`（`v0.x-draft`） |
| 快速试错 | 待新建（`rapid-experimentation`；与 MVP/OODA 分流） |
| 奥兹冒险 | 待新建（`oz-principle` / accountability；确认名录原意后再建） |
| 风险不对称 / 不对称回报 | 待新建或并入反脆弱互链（`asymmetric-payoff`） |
| 凯利准则 | 已有@他类 `finance-investing-models/kelly-criterion` |
| 蒙特卡洛模拟 | 待新建（`monte-carlo`） |
| 敏感性分析 | 待新建（`sensitivity-analysis`；决策树步骤已含部分） |
| 情景规划 | 已有@`…/scenario-planning`（`v0.x-draft`） |
| 预验式回顾 | 并入@`…/pre-mortem`（与事前验尸同法；不另建） |
| 红队思维 | 已有@`…/red-team`（`v0.x-draft`） |
| 事前验尸 | 已有@`…/pre-mortem`（`v0.x-draft`） |
| 决策日志 | 待新建（`decision-journal`） |
| 沉没成本（决策视角） | 已有@他类 `behavioral-biases/sunk-cost`（互链，不复制） |
| 机会成本（决策视角） | 已有@他类 `econ-micro-markets/opportunity-cost` |
| 阈值效应 | 待新建（`threshold-effect`；注意与临界点分流） |
| 临界质量 | 已有@他类 `systems-complexity/tipping-point` |
| 复盘四步法 | 待新建（`after-action-review`） |
| OODA 循环 | 已有@`…/ooda-loop`（`v0.x-draft`） |
| 计划谬误 | 已有@`…/planning-fallacy`（`v0.x-draft`） |
| 损失函数 | 待新建（`loss-function`；与期望效用分流） |
| 风险溢价 | 待新建或互链金融类（`risk-premium`） |
| （增补）期望效用 / 基率 | 已有@`…/expected-utility` · `base-rate`（`v0.x-draft`；名录未单列但与 EV/贝叶斯硬区分需要） |

#### 九、`learning-growth`

| 名录 | 状态 |
|---|---|
| 费曼技巧 | 已有@`learning-growth/feynman-technique` |
| 心流理论 | 已有@`…/flow` |
| 元认知 | 已有@`…/metacognition` |
| 艾宾浩斯遗忘曲线 | 已有@`…/forgetting-curve` |
| 反脆弱 | 已有@`…/antifragility` |
| 刻意练习 / 间隔重复 / 成长型思维 / 一万小时 / 深度工作 / ZPD | 已有@`learning-growth/*`（M3 `v0.x-draft`） |
| 其余学习法扩展 | 待新建 |

#### 十、`strategy-competition`

| 名录 | 状态 |
|---|---|
| 波特五力 | 已有@`strategy-competition/porters-five-forces` |
| 飞轮效应 | 已有@`…/flywheel` |
| 护城河 | 已有@`…/economic-moat` |
| SWOT（战略视角） | 已有@`…/swot` |
| 长尾战略 | 已有@他类 `systems-classic-effects/long-tail`（战略用法互链） |
| 蓝海 / 第二曲线 / 颠覆式创新 / BCG / OKR / VRIO | 已有@`strategy-competition/*`（M3 `v0.x-draft`） |
| GE 九宫 / 七S 等 | 待新建（`ge-mckinsey-matrix`、`mckinsey-7s` 等） |

#### 十一、`efficiency-execution`

| 名录 | 状态 |
|---|---|
| 艾森豪威尔矩阵 | 已有@`efficiency-execution/eisenhower-matrix` |
| PDCA 循环 | 已有@`…/pdca` |
| 80/20 时间法 | 已有@他类 `systems-classic-effects/pareto-principle`（时间用法互链） |
| 深度工作法 | 已有@他类 `learning-growth/deep-work`（主条；本类互链） |
| 番茄 / GTD / 看板 / 敏捷迭代 / 关键路径 / 精益 / 5S | 已有@`efficiency-execution/*`（M3 `v0.x-draft`） |
| 其余效率法扩展 | 待新建 |

#### 十二、`systems-complexity`

| 名录 | 状态 |
|---|---|
| 冰山模型 | 已有@`systems-complexity/iceberg-model` |
| 杠杆点 | 已有@`…/leverage` |
| 临界点与相变 | 已有@`…/tipping-point` |
| 耗散结构（自组织相关种子） | 已有@`…/dissipative-structures` |
| 路径依赖 / 锁定 / 网络效应 / 熵增 / 反馈回路 | 已有@他类 `systems-classic-effects/*`（名录注明可合并；**不**迁入本类） |
| 涌现 | 已有@`…/emergence`（`v0.x-draft`） |
| 系统基模 | 已有@`…/system-archetypes`（`v0.x-draft`） |
| 因果回路图 | 已有@`…/causal-loop-diagram`（`v0.x-draft`） |
| 存量与流量 | 已有@`…/stock-and-flow`（`v0.x-draft`） |
| 复杂适应系统 | 已有@`…/complex-adaptive-systems`（`v0.x-draft`） |
| 小世界网络 | 已有@`…/small-world-network`（`v0.x-draft`） |
| 无标度网络 | 已有@`…/scale-free-network`（`v0.x-draft`） |

### 5. 本阶段明确不做

- 不新建与六分类同义的父目录或第二套宏观/微观/博弈等目录  
- 不把 `thinking-models/` 剩余杂项（无精确名录对应）强行塞进第七–十二类  
- 不为「决策视角 / 战略视角」重复主题复制第二份 `SKILL.md`（互链即可）  
- 本轮不批量撰写待新建条目正文；不把 `docs/` 研究笔记提交 GitHub  

---

## 待办：其他

### org-it-intel-report 可选硬化
官方 frontmatter / `quick_validate` 等（非阻塞）。

### huawei-customer-insight
规格在本机 `docs/华为方法论/04-客户洞察Skill需求说明文档.md`，尚未实现。

### 《万物皆模型》增量
原书可验证剩余卡片已基本消化；后续仅在三重验证仍通过时增量补漏。与学科分类并行时，重叠主题优先落在对应分类可执行 Skill，避免在 `thinking-models/` 再造第二份。
