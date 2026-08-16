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

### thinking-models 思维模型库（现 **50** 个）
蒸馏自《万物皆模型》100个思维模型书 + 各自真实学科来源，走完 cangjie-skill 五阶段流水线 + skill-creator 官方规范校验。索引见 [`skills/thinking-models/README.md`](skills/thinking-models/README.md)。

曾累计 69 个（含苏格拉底式质疑）；其中 **19** 个与经济学/行为/系统效应明确对应的可执行 Skill 已于 2026-08-16 **物理迁出**至与 `business/`、`thinking-models/` 平级的 6 个分类目录（`thinking-models/` 原路径已删除）。见下文「已完成：六分类迁入」。

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
| 不迁 | 「仅部分相关」：`economic-moat`、`porters-five-forces`、`long-term-thinking` 仍留 `thinking-models/` |

**六分类路径（Batch A/B 补全后实际数量，2026-08-16 对账）**：

| # | 中文 | `category` | 含 `SKILL.md` 子目录数 | 备注 |
|---|---|---|---|---|
| 1 | 宏观经济理论与模型 | `econ-macro-theories` | **30** | 全部新建 draft |
| 2 | 微观经济与市场机制 | `econ-micro-markets` | **30** | 含迁入 `opportunity-cost` |
| 3 | 博弈论与策略模型 | `game-theory-models` | **31** | 30 专条 + 迁入总论 `game-theory` |
| 4 | 行为经济学与认知偏误 | `behavioral-biases` | **30** | 含迁入 9 个 |
| 5 | 金融与投资模型 | `finance-investing-models` | **30** | 含迁入 `compounding` |
| 6 | 系统思维与经典效应 | `systems-classic-effects` | **30** | 含迁入 7 个 |

合计：迁入种子 **19** + 分批新建补齐至上表；索引见各 `skills/<category>/README.md`。`thinking-models/` 仍为 **50**（`economic-moat` / `porters-five-forces` / `long-term-thinking` **未迁**）。

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
| `thinking-models`（对照） | 50 | 仍约 50；护城河/五力/长线未迁 |

- Phase 0 模板已在本分支：[`skills/_templates/EXECUTABLE_SKILL.md`](skills/_templates/EXECUTABLE_SKILL.md)
- 根 README / README.zh-CN 六分类计数与上表一致
- 新建 draft 抽查含「怎么用」「常见误用」；**迁入的 19 个旧稿**多数尚缺「常见误用」章节（可选后处理）

---

## 待办：六分类后处理与 Phase 3

> **需求来源（本机，不进 GitHub）**：`WorkBuddy/.../经济学思维模型Skills生成需求.md`  
> **本阶段状态**：形态与迁入 **已落地**；**Phase 0 模板已锁定**；**Batch A/B 数量目标已达成**（见上表）。  
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
- [ ] **Phase 3**：跨类「相关模型」双向检查；`quick_validate` 抽查；根 README 定稿复核
- [ ] **可选 evals 后处理**：对新建 draft 补 `evals/` / 官方规范校验；迁入旧稿增量补「常见误用」

### 3. 本阶段明确不做

- 不恢复 `skills/Economics/` 知识卡壳 / Phase 1 旧容器
- 不以 9 字段卡为主交付；不把本轮已迁 Skill 整篇改写成 9 字段（仅新建按模板；旧稿可选增量补「常见误用 / 钩子」）
- 不把护城河（`economic-moat`）/ 五力（`porters-five-forces`）/ 长线思考（`long-term-thinking`）强行迁入六分类
- 不一次性新建大批量 Skill（数量目标已达成；后续仅增量）
- 不把研究笔记写入 GitHub 跟踪路径

### 4. 建议的下一执行步

1. **Phase 3**：跨类「相关模型」双向检查 → `quick_validate` 抽查 → 根 README / 分类 README 定稿复核  
2. **或** 并行：skill-creator / evals 后处理（新建 draft 的 `evals/`、迁入 19 条补「常见误用」）

---

## 待办：其他

### org-it-intel-report 可选硬化
官方 frontmatter / `quick_validate` 等（非阻塞）。

### huawei-customer-insight
规格在本机 `docs/华为方法论/04-客户洞察Skill需求说明文档.md`，尚未实现。

### 《万物皆模型》增量
原书可验证剩余卡片已基本消化；后续仅在三重验证仍通过时增量补漏。与六分类并行时，重叠主题优先落在对应分类可执行 Skill，避免在 `thinking-models/` 再造第二份。
