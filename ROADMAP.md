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

**六分类路径**：

| # | 中文 | `category` | 本轮已迁入 |
|---|---|---|---|
| 1 | 宏观经济理论与模型 | `econ-macro-theories` | 0（待新建） |
| 2 | 微观经济与市场机制 | `econ-micro-markets` | `opportunity-cost` |
| 3 | 博弈论与策略模型 | `game-theory-models` | `game-theory` |
| 4 | 行为经济学与认知偏误 | `behavioral-biases` | 9 个（前景/损失/沉没/确认/易得/幸存/邓克/峰终/归因） |
| 5 | 金融与投资模型 | `finance-investing-models` | `compounding` |
| 6 | 系统思维与经典效应 | `systems-classic-effects` | 7 个（蝴蝶/二八/长尾/路径依赖/梅特卡夫/系统思维/系列位置） |

合计迁入 **19**；索引见各 `skills/<category>/README.md`。

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

**Phase 状态**：旧 Phase 1「`skills/Economics/` 知识卡容器壳」**作废并已删除**。本轮 = 迁 19 + 6 分类 README + 文档/链接修复。本轮**不重写**迁入 Skill 正文为 9 字段。

---

## 待办：六分类可执行 Skills 补全

> **需求来源（本机，不进 GitHub）**：`WorkBuddy/.../经济学思维模型Skills生成需求.md`  
> **本阶段状态**：形态与迁入 **已落地**；其余约 **160** 条按可执行 Skill 分批新建。  
> **硬约束**（与 CLAUDE.md 一致）：
> - `SKILL.md` 只落在 `skills/<category>/<name>/`
> - 研究/审计轨迹写本机 `docs/books/<slug>/`（随 `docs/` gitignore，**不进 GitHub**）
> - README「目前的进展」只反映 `skills/` 里真实存在的产出

### 1. 目标与交付形态（已确认 · 修订）

| 项 | 约定 |
|---|---|
| 规模 | 需求清单约 **6×30 ≈ 180** 条主题；每条最终为 **一个可执行 Skill 目录** |
| 粒度 | 可执行决策步骤全文；可吸收原 9 字段中有用信息，**不是**独立知识卡产品 |
| 语言 | 简体中文；术语首次标注英文/人名；通俗 + 生活化例子 |
| **目录** | `skills/<category-slug>/<skill-slug>/`，六分类与 `business/` / `thinking-models/` **平级** |
| **明确不做** | 不做「知识卡容器」主交付；不做 `skills/Economics/` 父目录；不做 `thinking-models/` 内嵌套 Economics |

### 2. Phase 0 / 2 — 按可执行 Skill 分批新建

- **Phase 0**：锁定可执行正文模板；标明哪些原 9 字段项为可选吸收章节
- **Phase 2 Batch A/B**：按分类分批新建缺口条目（宏观从 0 起；其余在已迁种子旁扩展）
- **Phase 2/3**：跨类「相关模型」双向检查；`quick_validate`；根 README 计数同步

### 3. 可选章节（自原 9 字段吸收）

新建/修订可执行 Skill 时，建议在正文中视需要纳入（非另建卡文件）：

| 来源字段 | 吸收方式 |
|---|---|
| 提出者 | 写入「这是什么」或 frontmatter/来源行 |
| 一句话定义 | 开篇短定义（可 ≤30 字作口令） |
| 常见误用 | 独立小节或并入「边界」（**推荐非空**） |
| 记忆钩子 | 文末一句口诀（可选） |
| 经典案例 / 现实应用 | 并入既有「例证」 |
| 相关概念 | 并入「相关模型」并链到真实路径 |

### 4. 本阶段明确不做

- 不恢复 `skills/Economics/` 知识卡壳 / Phase 1 旧容器
- 不以 9 字段卡为主交付；不把本轮已迁 Skill 整篇改写成 9 字段
- 不把护城河 / 五力 / 长线思考强行迁入六分类
- 不一次性新建 ~160 个 Skill（分批）
- 不把研究笔记写入 GitHub 跟踪路径

### 5. 建议的下一执行步

1. Phase 0：锁定可执行 Skill 章节模板（含可选「常见误用 / 记忆钩子」）
2. Batch A：宏观分类先建若干种子；其他类按需求清单补缺口

---

## 待办：其他

### org-it-intel-report 可选硬化
官方 frontmatter / `quick_validate` 等（非阻塞）。

### huawei-customer-insight
规格在本机 `docs/华为方法论/04-客户洞察Skill需求说明文档.md`，尚未实现。

### 《万物皆模型》增量
原书可验证剩余卡片已基本消化；后续仅在三重验证仍通过时增量补漏。与六分类并行时，重叠主题优先落在对应分类可执行 Skill，避免在 `thinking-models/` 再造第二份。
