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

### ThinkingModels 思维模型库（第一批 4 个）
蒸馏自《万物皆模型》100个思维模型书 + 各自真实学科来源，走完 cangjie-skill 五阶段流水线 + internal/skill-creator 官方规范校验：

| Skill | 状态 |
|---|---|
| [opportunity-cost](skills/ThinkingModels/opportunity-cost) 机会成本 | v1.0，10/10 盲测通过 |
| [antifragility](skills/ThinkingModels/antifragility) 反脆弱 | v1.0，10/10 盲测通过 |
| [occams-razor](skills/ThinkingModels/occams-razor) 奥卡姆剃刀 | v1.0，10/10 盲测通过 |
| [socratic-questioning](skills/ThinkingModels/socratic-questioning) 苏格拉底式质疑（方法论补充，非原书 100 模型之一） | v1.0，11/11 盲测通过 |

已完成的验证环节：
- 苏格拉底式质疑自检（定稿前强制环节，抓出 3 处概念/逻辑错误并修正，见 `docs/books/wanwu-jie-moxing/socratic-review.md` 本机审计记录）
- 41 条盲测用例（should_trigger / should_not_trigger / edge_case / correctness_trap），独立 sub-agent 盲测 100% 通过
- 官方 Skill 规范校验（`quick_validate.py`），frontmatter 全部合规
- 每个 skill 的 `evals/test-results.md` 已下沉到自己目录

### 研究已完成、尚未构造成 Skill
以下 4 个模型的候选素材研究已在 `docs/books/wanwu-jie-moxing/candidates/`（本机，不进 GitHub）完成，可直接进入 RIA++ 构造阶段：
- 沉没成本（与机会成本互为镜像，是 opportunity-cost 最常见的误触发诱饵）
- 确认性偏差
- 逆向思维
- 第一性原理

## 待办

### 短期：完成研究已就绪的 4 个模型
对沉没成本、确认性偏差、逆向思维、第一性原理逐个执行：
1. RIA++ 构造 SKILL.md（含苏格拉底式质疑自检）
2. Zettelkasten 链接（更新 `skills/ThinkingModels/README.md` 的区分地图，尤其沉没成本 vs 机会成本这对高频混淆）
3. 压力测试用例 + 盲测
4. internal/skill-creator 官方规范校验

### 中期：思维模型库扩容
《万物皆模型》100 个模型中，目前只蒸馏了 4 个（其中 1 个是方法论补充，非原书模型）。按批次继续蒸馏剩余约 92 个，每批次先经三重验证筛选，不追求速度，保证质量红线（真实学科来源重新研究、边界条件不能空缺）。

### 待观察
- `skills/Business/sales-company-intel-report` 是否需要单独走一遍 internal/skill-creator 官方规范校验（当前 frontmatter 同样使用了非标准的 `author`/`version` 顶层字段，尚未按本次 ThinkingModels 的方式修正）。

---

*本文件反映代码仓库的真实状态，只在 `skills/` 目录下有对应产出后才标记"已完成"。研究记录、审计轨迹等本机资料见项目内 `docs/`（不进 GitHub，见 `.gitignore`）。*
