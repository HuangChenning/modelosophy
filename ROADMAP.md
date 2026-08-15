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

### ThinkingModels 思维模型库（14 个）
蒸馏自《万物皆模型》100个思维模型书 + 各自真实学科来源，走完 cangjie-skill 五阶段流水线 + skill-creator 官方规范校验：

| Skill | 状态 |
|---|---|
| [opportunity-cost](skills/ThinkingModels/opportunity-cost) 机会成本 | v1.0，10/10 盲测通过 |
| [sunk-cost](skills/ThinkingModels/sunk-cost) 沉没成本 | v1.0，10/10 盲测通过 |
| [decision-tree](skills/ThinkingModels/decision-tree) 决策树 | v1.0，10/10 盲测通过 |
| [ten-ten-ten](skills/ThinkingModels/ten-ten-ten) 10/10/10 | v1.0，10/10 盲测通过 |
| [antifragility](skills/ThinkingModels/antifragility) 反脆弱 | v1.0，10/10 盲测通过 |
| [occams-razor](skills/ThinkingModels/occams-razor) 奥卡姆剃刀 | v1.0，10/10 盲测通过 |
| [confirmation-bias](skills/ThinkingModels/confirmation-bias) 确认性偏差 | v1.0，10/10 盲测通过 |
| [availability-heuristic](skills/ThinkingModels/availability-heuristic) 易得性启发 | v1.0，10/10 盲测通过 |
| [six-thinking-hats](skills/ThinkingModels/six-thinking-hats) 六顶思考帽 | v1.0，10/10 盲测通过 |
| [inversion](skills/ThinkingModels/inversion) 逆向思维 | v1.0，10/10 盲测通过 |
| [first-principles](skills/ThinkingModels/first-principles) 第一性原理 | v1.0，10/10 盲测通过 |
| [maslow-hierarchy](skills/ThinkingModels/maslow-hierarchy) 马斯洛需求层次 | v1.0，10/10 盲测通过 |
| [systems-thinking](skills/ThinkingModels/systems-thinking) 系统思维 | v1.0，10/10 盲测通过 |
| [socratic-questioning](skills/ThinkingModels/socratic-questioning) 苏格拉底式质疑（方法论补充） | v1.0，11/11 盲测通过 |

已完成的验证环节：
- 苏格拉底式质疑自检（定稿前强制环节；各批抓出的原书错误见 `docs/books/wanwu-jie-moxing/socratic-review.md`）
- 141 条盲测用例，独立 sub-agent 盲测通过
- 官方 Skill 规范校验（`quick_validate.py`），frontmatter 全部合规
- 每个 skill 的 `evals/test-results.md` 已下沉到自己目录

## 待办

### 短期：01–18 中本轮未构造的 5 个
直觉（与 #20 卡尼曼重复）、非 SR、升维、笛卡尔（暂缓）、万物联系。研究记录已在本机 `candidates/batch-01-18-remaining.md`。

### 中期：思维模型库扩容
《万物皆模型》100 个模型中，目前蒸馏了 13 个原书模型 + 1 个方法论补充。按批次继续蒸馏剩余约 80+ 个，每批次先经三重验证筛选。原书 19–100 连阶段 0 通读都还没做完。

### 待观察
- `skills/Business/sales-company-intel-report` 是否需要单独走一遍官方 Skill 规范校验（当前 frontmatter 同样使用了非标准的 `author`/`version` 顶层字段，尚未按 ThinkingModels 的方式修正）。
- `huawei-customer-insight`：规格书在 `docs/华为方法论/04-客户洞察Skill需求说明文档.md`，尚未实现。

---

*本文件反映代码仓库的真实状态，只在 `skills/` 目录下有对应产出后才标记"已完成"。研究记录、审计轨迹等本机资料见项目内 `docs/`（不进 GitHub，见 `.gitignore`）。*
