# ROADMAP — modelosophy 工作计划

记录项目当前进展：哪些工作已经完整交付，哪些还在待办队列。按主题分组，而不是按时间顺序。

## 已完成

### 项目定位与文档骨架
- README.md / README.zh-CN.md：确立"万物皆模型"定位、双语同步、图示化 hero/mechanism 资源（`assets/readme/`）。
- DESIGN.md：HTML 报告类 Skill 的统一视觉规范。
- CLAUDE.md：Skill 生产流程（cangjie-skill 蒸馏 → internal/skill-creator 官方规范校验两阶段）、行为准则、Git 工作流规则（本地文件，不进 GitHub）。

### Skill 目录规范化
- `skills/` 改为按领域分类：`skills/<category>/<name>/`。
- 原 `skills/sales-company-intel-report/` 迁入 `skills/Business/`，并去品牌重命名为 `org-it-intel-report`（组织 IT 情报报告）。
- 输出约定：Skill 生成的报告统一写入 `output/<skill-name>/`（gitignored，不进仓库）。

### ThinkingModels 思维模型库（69 个）
蒸馏自《万物皆模型》100个思维模型书 + 各自真实学科来源，走完 cangjie-skill 五阶段流水线 + skill-creator 官方规范校验。索引见 [`skills/ThinkingModels/README.md`](skills/ThinkingModels/README.md)。

第五批：flow、mece、path-dependence、flywheel、swot、pdca。

第六批（同枝）：prospect-theory、dunning-kruger、fogg-behavior-model、golden-circle、johari-window。

第七批（30 个）：implicit-premises、butterfly-effect、deductive-reasoning、iceberg-model、feynman-technique、pareto-principle、pyramid-principle、redundancy、metacognition、forgetting-curve、tipping-point、leverage、long-tail、spiral-of-silence、serial-position-effect、ladder-of-inference、counterfactual-thinking、peak-end-rule、five-w-one-h、attribution-theory、hook-model、situational-leadership、game-theory、abductive-reasoning、emotional-abc、metcalfes-law、contrarian-and-right、porters-five-forces、economic-moat、long-term-thinking（各 10/10 盲测 + `quick_validate`）。库规模 31→61。

第八批（原书剩余 8 个）：process-replication、negentropy、expected-value、critical-thinking、dissipative-structures、munger-misjudgment、gaslighting、dual-goal-list（各 10/10 盲测 + `quick_validate`）。库规模 61→69（原书模型 60→68 + socratic）。

已完成的验证环节：
- 苏格拉底式质疑自检（定稿前强制；审计见本机 `docs/books/wanwu-jie-moxing/socratic-review.md`）
- 盲测与官方 Skill 规范校验；每个 skill 含 `evals/`

---

## 待办：经济学与经典效应知识 Skills（新计划）

> **需求来源（本机，不进 GitHub）**：`WorkBuddy/.../经济学思维模型Skills生成需求.md`  
> **本阶段状态**：目录与交付形态**已确认**（见下）；本文件已写死决策。**尚未**创建 `skills/Economics/` 目录、尚未大规模新建 180 张卡片。  
> **硬约束**（与 CLAUDE.md 一致）：
> - `SKILL.md` 只落在 `skills/<category>/<name>/`
> - 研究/审计轨迹写本机 `docs/books/<slug>/`（随 `docs/` gitignore，**不进 GitHub**）
> - README「目前的进展」只反映 `skills/` 里真实存在的产出

### 1. 目标与交付形态（已确认）

| 项 | 约定 |
|---|---|
| 规模 | **6 分类 × 每类 30 条 = 180** 张知识卡片 |
| 粒度 | 统一结构的「知识卡片」，非百科长文、也非现有 ThinkingModels 的「可执行决策步骤」全文 |
| 语言 | 简体中文；术语首次标注英文/人名；通俗 + 每条至少 1 个生活化例子 |
| **目录根** | **`skills/Economics/`**（与 `Business/`、`ThinkingModels/` **并列**） |
| **交付形态** | **恰好 6 个文件夹 = 6 类**；每类一个**容器 Skill**（`SKILL.md` + 该类 30 张知识卡） |
| **明确不做** | **不做** 180 个独立顶层 Skill 目录；**不做** `ThinkingModels/Economics/` 嵌套；**不物理搬迁** ThinkingModels 现有可执行 Skill |

**与现有 ThinkingModels 的定位差异（必须写进计划，避免重复劳动）：**

| | ThinkingModels（已有） | Economics 知识 Skills（新建） |
|---|---|---|
| 单位 | 一模型一 Skill | 一分类一 Skill，内含 30 张卡片 |
| 主用途 | 触发后按步骤帮用户**决策/拆解** | 查阅、讲解、举例、串相关概念 |
| 核心结构 | 这是什么 / 何时用 / 怎么用 / 边界 / 相关模型 | 9 字段知识卡片（见下） |
| 重叠处理 | **路径不动**，保留可执行 Skill | 卡片摘要 +「可执行深潜」互链；**不删除、不 `git mv`** ThinkingModels 原件 |

### 2. 已确认：6 个 `category-slug`（中英文）

按需求文档第三节分类命名，slug 为 kebab-case；**路径一一对应，不再变更**：

| # | 中文名 | 英文名（含义） | `category-slug` | 目标路径 | 条目数 |
|---|---|---|---|---|---|
| 1 | 宏观经济理论与模型 | Macroeconomic Theories & Models | `econ-macro-theories` | `skills/Economics/econ-macro-theories/` | 30 |
| 2 | 微观经济与市场机制 | Microeconomics & Market Mechanisms | `econ-micro-markets` | `skills/Economics/econ-micro-markets/` | 30 |
| 3 | 博弈论与策略模型 | Game Theory & Strategy Models | `game-theory-models` | `skills/Economics/game-theory-models/` | 30 |
| 4 | 行为经济学与认知偏误 | Behavioral Economics & Cognitive Biases | `behavioral-biases` | `skills/Economics/behavioral-biases/` | 30 |
| 5 | 金融与投资模型 | Finance & Investing Models | `finance-investing-models` | `skills/Economics/finance-investing-models/` | 30 |
| 6 | 系统思维与经典效应 | Systems Thinking & Classic Effects | `systems-classic-effects` | `skills/Economics/systems-classic-effects/` | 30 |

目标目录树（**仅规划示意；本阶段不创建空目录**，等用户启动 Phase 0 / Phase 1 再落地）：

```
skills/Economics/                          # 与 Business、ThinkingModels 并列
  README.md                                # Phase 1 再建：分类地图 + 与 ThinkingModels 互链说明
  econ-macro-theories/
    SKILL.md                               # 容器 Skill：触发 + 使用说明 + 本类 30 卡索引
    references/cards/                      # 本类 30 张知识卡（或 cards.md / 分文件，Phase 0 定模板后统一）
    evals/                                 # 后处理阶段再补齐
  econ-micro-markets/
    SKILL.md
    references/cards/
    evals/
  game-theory-models/
    SKILL.md
    references/cards/
    evals/
  behavioral-biases/
    SKILL.md
    references/cards/
    evals/
  finance-investing-models/
    SKILL.md
    references/cards/
    evals/
  systems-classic-effects/
    SKILL.md
    references/cards/
    evals/
```

完整 180 条清单以需求文档第三节为准（本 ROADMAP 不重复粘贴全文，避免双源漂移）。

### 3. 目录决策（已写死）与迁移策略

#### 已确认路径：`skills/Economics/<category-slug>/`

与现有 `Business/`、`ThinkingModels/` **并列**，理由（决策依据，备忘）：

1. 交付物是「知识卡片容器」，与 ThinkingModels「一模型一可执行 Skill」产品形态不同，并列比嵌套更清晰。
2. 符合仓库约定 `skills/<category>/<name>/`，不把 SKILL 放进 `docs/`。
3. 避免把 6 个大容器塞进 `ThinkingModels/`，冲淡现有模型索引与防误触发图。

#### 已否决

| 方案 | 状态 |
|---|---|
| `skills/ThinkingModels/Economics/<slug>/` 嵌套 | **否决**（相对路径脆、语义混杂） |
| 180 个独立顶层 Skill 目录（每卡一目录） | **否决**（与需求「一分类一 Skill」及仓库可维护性冲突） |

#### 迁移 / 互链策略（ThinkingModels ↔ Economics）

**原则：内容复用，路径不迁；可执行 Skill 留在 ThinkingModels；Economics 卡片与之互链。**

1. **不物理搬迁**已通过盲测的 ThinkingModels Skill（如 `opportunity-cost`、`sunk-cost`）——避免打断相对链接与 eval。
2. 在 Economics 对应卡片中：写入 9 字段卡片正文；「相关概念」链到同库其他卡片；另加一行「可执行深潜」指向现有 `skills/ThinkingModels/<slug>/SKILL.md`（或仓库相对路径）。
3. 仅当某条目**只适合知识卡片、从未做成独立 Skill**时，才新建卡片（绝大多数情况）。
4. 现有 `game-theory` 是「入门切片」可执行 Skill，**不等于**分类三的 30 张卡片；分类三在 `skills/Economics/game-theory-models/` 新建容器，并在相关概念里互链，禁止把 30 条硬塞进现有 `game-theory/SKILL.md`。

#### 主要风险

| 风险 | 影响 | 缓解 |
|---|---|---|
| README / 索引链接失效 | 用户找不到模型 | Phase 1 只新增 `Economics/`，不改 ThinkingModels 路径；同步更新根 README 一句 + `skills/Economics/README.md` |
| 相关模型相对路径 | 跨 category `../` 易写错 | 统一用 `skills/ThinkingModels/<slug>/SKILL.md` 形式写清；Phase 3 脚本/人工抽查 |
| 双重触发 | 用户说「机会成本」同时命中两套 | ThinkingModels description 保持决策场景；Economics Skill description 强调「讲解/查阅/举例」；在双方「相关」节写清分流判据 |
| 形态混用 | 把 9 字段卡片写成可执行长文或反之 | Phase 0 字段模板锁死；样例 Top 10 经用户确认风格后再扩量 |
| 跨类重复 | 如「搭便车」既像微观又像系统效应 | 严格按需求第三节归属；验收勾选「无跨类重复」 |

### 4. 已有 → 应归属哪一分类（映射表）

下列为需求 180 条中，仓库 **已有可复用种子**（ThinkingModels slug → 需求条目）。「可迁移」= 可蒸馏进 Economics 卡片并互链，**不是**本阶段立刻 `git mv`。

#### 分类一 · 宏观经济理论与模型 — 可复用 **0**

（当前无对应独立 Skill。）

#### 分类二 · 微观经济与市场机制 — 可复用 **~2**

| 需求条目 | 现有 slug | 处理建议 |
|---|---|---|
| 机会成本 | `opportunity-cost` | 卡片摘要 + 链到可执行 Skill |
| 进入壁垒（部分相关） | `economic-moat`、`porters-five-forces` | 护城河/五力作「相关概念」；**不**把五力整篇等同于进入壁垒卡片 |

其余 28 条待新建（供需、弹性、柠檬市场、科斯定理等）。

#### 分类三 · 博弈论与策略模型 — 可复用 **~1（局部）**

| 需求条目 | 现有 slug | 处理建议 |
|---|---|---|
| 囚徒困境、纳什均衡等（入门覆盖） | `game-theory` | 保留可执行切片；30 条卡片在 `game-theory-models` 新建；入门条目可复用其例证 |

其余约 28–29 条（拍卖、机制设计、夏普利值、匹配理论等）待新建。

#### 分类四 · 行为经济学与认知偏误 — 可复用 **~9**

| 需求条目 | 现有 slug | 处理建议 |
|---|---|---|
| 前景理论 | `prospect-theory` | 卡片 + 互链 |
| 损失厌恶 | `loss-aversion` | 同上 |
| 沉没成本谬误 | `sunk-cost` | 同上 |
| 确认偏误 | `confirmation-bias` | 同上 |
| 可得性启发 | `availability-heuristic` | 同上 |
| 幸存者偏差 | `survivorship-bias` | 同上 |
| 达克效应 | `dunning-kruger` | 同上 |
| 峰终定律 | `peak-end-rule` | 同上 |
| 基本归因错误 | `attribution-theory` | 卡片收窄到 FAE；可执行 Skill 保留更广归因框架 |

其余约 21 条待新建（锚定、心理账户、框架、双曲贴现、西奥迪尼原则等）。

> 相邻但**不在**本分类 30 条清单内、勿强行迁入：`dual-process`（双系统，可作相关概念）。

#### 分类五 · 金融与投资模型 — 可复用 **~1**

| 需求条目 | 现有 slug | 处理建议 |
|---|---|---|
| 复利效应 | `compounding` | 卡片 + 互链 |

其余 29 条待新建（EMH、CAPM、DCF、明斯基、凯利等）。

#### 分类六 · 系统思维与经典效应 — 可复用 **~8–10**

| 需求条目 | 现有 slug | 处理建议 |
|---|---|---|
| 蝴蝶效应 | `butterfly-effect` | 卡片 + 互链 |
| 帕累托法则 | `pareto-principle` | 同上 |
| 长尾理论 | `long-tail` | 同上 |
| 路径依赖 | `path-dependence` | 同上 |
| 网络效应 | `metcalfes-law` | 梅特卡夫作网络效应的量化启发式卡片；可单独或合并表述时在「常见误用」写清 n² 局限 |
| 反馈回路 / 系统动力学 | `systems-thinking` | 可拆成需求中的两张卡片，内容从现有 Skill 蒸馏 |
| 首因效应 / 近因效应 | `serial-position-effect` | 一张可执行 Skill → **两张**卡片 |
| 二阶思维（部分相关） | `long-term-thinking` | 相关概念互链；卡片按「然后呢」定义写，避免与长线思考完全等同 |
| 锁定效应（部分相关） | `economic-moat`、`path-dependence` | 相关概念，不整篇替代 |

相邻勿强行等同清单条目：`antifragility`（≠黑天鹅）、`tipping-point`、`leverage`、`flywheel`——可作相关概念，不占 30 席。

#### 映射汇总

| 分类 | 需求条数 | 已有可复用种子（约） | 待新建卡片（约） |
|---|---|---|---|
| 1 宏观 | 30 | 0 | 30 |
| 2 微观 | 30 | 2 | 28 |
| 3 博弈论 | 30 | 1（局部） | 29 |
| 4 行为 | 30 | 9 | 21 |
| 5 金融 | 30 | 1 | 29 |
| 6 系统效应 | 30 | 8–10 | 20–22 |
| **合计** | **180** | **~21** | **~159** |

另需新建 **恰好 6 个** 容器 Skill 壳（上表 6 路径下的 `SKILL.md` + `references/cards/`），现有 ThinkingModels **全部保留、不搬迁**。

### 5. 知识卡片必含字段检查项

需求规定每张卡片 **9 字段**（缺一不可；「常见误用」不得为空）：

| # | 字段 | 验收要点 |
|---|---|---|
| 1 | 名称 | 中文名 + 常见别名/英文名 |
| 2 | 提出者 | 学派/人名及年代 |
| 3 | 一句话定义 | ≤30 字 |
| 4 | 原理机制 | 为什么会这样，2–4 句 |
| 5 | 经典案例 | 1 个学术史/历史经典案例 |
| 6 | 现实应用 | 1–2 个当代商业/投资/职场/生活应用 |
| 7 | 常见误用 | **强制非空**——与百科拉开差距的关键 |
| 8 | 相关概念 | 指向本库其他**确实存在**的条目 |
| 9 | 记忆钩子 | 一句口诀/比喻 |

#### 现有 ThinkingModels `SKILL.md` 常见缺口（相对上述 9 字段）

现有结构多为：这是什么 / 什么时候用 / 怎么用 / 例证 / 边界 / 相关模型。对照 9 字段时常见缺口：

| 9 字段 | 现有常见情况 |
|---|---|
| 提出者 | 常散落在 frontmatter/`这是什么`，**无独立字段** |
| 一句话定义 ≤30 字 | 常有长定义，缺「一眼口令」 |
| 原理机制 | 有，但与「怎么用」步骤缠在一起 |
| 经典案例 vs 现实应用 | 「例证」常混在一起，未拆栏 |
| 常见误用 | 多在「边界」或步骤脚注，**很少单独成栏** |
| 相关概念 | 有「相关模型」，但是 Skill 链接而非卡片名网络 |
| 记忆钩子 | **普遍缺失** |

→ Phase 0 / Phase 2：新建卡片用统一模板；从现有 Skill 蒸馏时**补齐**提出者、误用栏、记忆钩子，而不是整文件复制。

### 6. 缺失条目 — 待新建清单（按优先级分批）

**总策略（与需求第四节一致）**：先每类 **Top 10 打样** → 用户确认文风 → 再补到每类 30。

#### Batch A — 样例打样（6×10 = 60）优先

每类取需求清单 **前 10 条**（宏观：看不见的手…奥肯定律；微观：供需法则…范围经济；博弈：囚徒困境…信号博弈；行为：前景理论…小数定律；金融：EMH…市盈率/市净率；系统：蝴蝶效应…温水煮青蛙）。其中已有种子的条目优先蒸馏，加快打样。

#### Batch B — 补全到 180（每类再 +20）

按分类缺口从大到小：**宏观 30 → 金融 29 → 博弈 ~29 → 微观 28 → 系统 ~21 → 行为 21**（可并行多 Agent，但同一分类内相关概念链接需最后统一过一遍）。

#### Batch C — 网络一致性

- 相关概念双向检查（只指向存在条目）
- 与 ThinkingModels 可执行 Skill 的分流说明写进各容器 `SKILL.md`
- 抽查 10 条事实准确性（需求验收）

### 7. 分阶段里程碑

#### Phase 0 — 字段审计与模板锁定（**下一步**）

- [x] 确认目录方案：`skills/Economics/<category-slug>/`，恰好 6 文件夹；不做 180 顶层 Skill；不嵌套进 ThinkingModels（**2026-08-16 用户确认，已写死本节**）
- [ ] 固化 9 字段 Markdown 模板（二级标题或表格二选一，全库统一；卡文件落点：`references/cards/`）
- [ ] 抽查 5–8 个现有相关 ThinkingModels Skill，列出「可复用段落 / 必须重写字段」清单，写入本机 `docs/books/econ-knowledge-skills/`（**不进 GitHub**）
- [ ] 产出 1 张样例卡（建议：机会成本）供文风锚点

**退出标准**：模板 + 样例卡经用户确认。

#### Phase 1 — 创建 6 容器目录与 Skill 壳（不搬迁旧 Skill）

- [ ] 创建 `skills/Economics/` + 上表 6 个 `category-slug` 目录 + 各 `SKILL.md`（触发语、索引表、与 ThinkingModels 分流）
- [ ] 创建 `skills/Economics/README.md`（分类地图；链到 ThinkingModels 重叠项）
- [ ] **不** `git mv` ThinkingModels 现有目录
- [ ] 根 README / README.zh-CN 增加一句「Economics 知识 Skills：规划中 / Phase x」（有真实目录后再写「已有 N」）

**退出标准**：6 个空壳可被 Agent 触发到正确分类；链接无 404。

#### Phase 2 — 补建缺失卡片

- [ ] Batch A：每类 Top 10（优先复用映射表种子）
- [ ] 用户确认风格后 Batch B 补全至 180
- [ ] 每张卡 9 字段完整；常见误用非空；至少 1 个生活化例子
- [ ] 蒸馏审计留在 `docs/books/econ-knowledge-skills/`（候选、苏格拉底自检、拒绝项）——**不进 GitHub**

**退出标准**：6×30 齐全、无跨类重复条目名。

#### Phase 3 — 校验与文档同步

- [ ] `skill-creator` / `quick_validate` 对 6 个容器 Skill 做官方规范校验；补 `evals/`（触发分类、查卡、误用讲解等）
- [ ] 相关概念存在性检查 + 抽查 10 条事实
- [ ] 更新 `skills/Economics/README.md`、根双语 README「目前的进展」
- [ ] 更新本 ROADMAP：本大节从「待办」移入「已完成」的条件 = `skills/Economics/` 下 6 个 Skill 均有完整 30 卡

**退出标准**：需求第五节验收清单全部勾选。

### 8. 本阶段明确不做

- 不创建 `skills/Economics/` 下 6 个空目录（等用户说开始 Phase 0 / 实施）
- 不开始 180 卡大规模生成；**不做** 180 个独立顶层 Skill 目录
- 不物理迁移 ThinkingModels 目录
- 不 commit / push / PR（除非用户另行要求）
- 不把研究笔记写入 GitHub 跟踪路径

### 9. 建议的下一执行步（已确认形态）

**已确认**：`skills/Economics/` 下恰好 **6 文件夹** = 6 类容器 Skill（见 §2），卡片互链 ThinkingModels，旧 Skill 不搬迁。

**下一步 → Phase 0**：

1. 锁死 9 字段 Markdown 模板 + 卡文件约定（`references/cards/`）
2. 写 1 张样例卡（建议：机会成本）→ 你确认文风
3. 再开 Batch A / Phase 1（建 6 壳目录）

---


## 其他待办（原有）

### 短期：继续扩容思维模型库
原书可验证剩余卡片已基本消化；后续仅在三重验证仍通过时增量补漏。研究记录见本机 `docs/books/wanwu-jie-moxing/candidates/`。与 Economics 知识库并行时，优先避免与 180 清单重复造「第二个可执行 Skill」——重叠项改为 Economics 卡片 + 保留原 ThinkingModels。

### 待观察
- `skills/Business/org-it-intel-report` 官方 Skill 规范校验 / frontmatter 规范化。
- `huawei-customer-insight`：规格书在 `docs/华为方法论/04-客户洞察Skill需求说明文档.md`，尚未实现。

---

*本文件反映代码仓库的真实状态，只在 `skills/` 目录下有对应产出后才标记"已完成"。研究记录、审计轨迹等本机资料见项目内 `docs/`（不进 GitHub，见 `.gitignore`）。*
