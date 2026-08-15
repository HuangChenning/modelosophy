# ROADMAP — modelosophy 工作计划

记录项目当前进展：哪些工作已经完整交付，哪些还在待办队列。按主题分组，而不是按时间顺序。

## 已完成

### 项目定位与文档骨架
- README.md / README.zh-CN.md：确立"万物皆模型"定位、双语同步、图示化 hero/mechanism 资源（`assets/readme/`）。
- DESIGN.md：HTML 报告类 Skill 的统一视觉规范。
- CLAUDE.md：Skill 生产流程（cangjie-skill 蒸馏 → internal/skill-creator 官方规范校验两阶段）、行为准则、Git 工作流规则（本地文件，不进 GitHub）。

### Skill 目录规范化
- `skills/` 改为按领域分类：`skills/<category>/<name>/`。
- 原 `skills/sales-company-intel-report/` 迁移至 `skills/Business/sales-company-intel-report/`。
- 输出约定：Skill 生成的报告统一写入 `output/<skill-name>/`（gitignored，不进仓库）。

### ThinkingModels 思维模型库（61 个）
蒸馏自《万物皆模型》100个思维模型书 + 各自真实学科来源，走完 cangjie-skill 五阶段流水线 + skill-creator 官方规范校验。索引见 [`skills/ThinkingModels/README.md`](skills/ThinkingModels/README.md)。

第五批：flow、mece、path-dependence、flywheel、swot、pdca。

第六批（同枝）：prospect-theory、dunning-kruger、fogg-behavior-model、golden-circle、johari-window。

第七批（30 个）：implicit-premises、butterfly-effect、deductive-reasoning、iceberg-model、feynman-technique、pareto-principle、pyramid-principle、redundancy、metacognition、forgetting-curve、tipping-point、leverage、long-tail、spiral-of-silence、serial-position-effect、ladder-of-inference、counterfactual-thinking、peak-end-rule、five-w-one-h、attribution-theory、hook-model、situational-leadership、game-theory、abductive-reasoning、emotional-abc、metcalfes-law、contrarian-and-right、porters-five-forces、economic-moat、long-term-thinking（各 10/10 盲测 + `quick_validate`）。库规模 31→61。

已完成的验证环节：
- 苏格拉底式质疑自检（定稿前强制；审计见本机 `docs/books/wanwu-jie-moxing/socratic-review.md`）
- 盲测与官方 Skill 规范校验；每个 skill 含 `evals/`

## 待办

### 短期：继续扩容思维模型库
从原书剩余卡片中挑选仍能过三重验证者；已拒绝伪科学/撞车项不回炉。研究记录见本机 `docs/books/wanwu-jie-moxing/candidates/`。

### 待观察
- `skills/Business/sales-company-intel-report` 官方 Skill 规范校验 / frontmatter 规范化。
- `huawei-customer-insight`：规格书在 `docs/华为方法论/04-客户洞察Skill需求说明文档.md`，尚未实现。

---

*本文件反映代码仓库的真实状态，只在 `skills/` 目录下有对应产出后才标记"已完成"。研究记录、审计轨迹等本机资料见项目内 `docs/`（不进 GitHub，见 `.gitignore`）。*
