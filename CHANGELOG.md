# Changelog

本文档记录 **modelosophy** 仓库级显著变更。

格式大致遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

> **说明**
>
> - 各 Skill 的 `metadata.version`（`v1.0` / `v0.x-draft`）是 **Skill 级**版本，与本文件的仓库级节点独立。`v1.0` 表示过了触发向盲测，**不等于**内容事实已核验。
> - 本仓库尚未打 git tag / 发布 GitHub Release；下列日期对应合并里程碑。
> - 更细的审计轨迹与待办见 [`ROADMAP.md`](ROADMAP.md)。

## [Unreleased]

### Added

- 全库剩余 **280** 个草稿级 Skill 补齐完整 `evals/test-prompts.json` 评估集（每项 $\ge 10$ 条测试用例，包含应触发/不应触发/边界/2条以上正确性陷阱）。

### Changed

- 全库 **280** 个草稿 Skill 全部完成 Socratic 自检、盲测用例拓展与 `quick_validate.py` 结构校验，正式从 `v0.x-draft` 升阶至 **`v1.0`**。
- **全库 `v1.0` 覆盖率达成 100%**（**372/372** 个 Skill 均为 `v1.0`，草稿降至 0）。
- 运行 `python3 internal/skill-creator/scripts/audit_repo_skills.py .`，372 个 Skill 0 违规、0 脚手架泄漏、0 模板缺失。
- 同步全量更新根目录双语 README（`README.md` 与 `README.zh-CN.md`）、14 项分类 README、`ROADMAP.md` 及 `CHANGELOG.md` 的计数与状态。

---

## [2026-08-19] — 内容正确性审计闭环（全库 350）

### Fixed

- 第二轮内容正确性审查：覆盖此前未审的 7 个分类，连同补漏共修复约 **47** 处实质问题（路由表错误、理论冲突未点破、孤立/封闭系统术语、引用张冠李戴、伪精确数字等）
- 第三轮：纠正「未读缺口」被夸大的问题；核完剩余 3 个金融文件 + 完整 `business/org-it-intel-report`；当时库内全部 **350** 个 `SKILL.md` 已跨三轮读过（本轮无新增内容修复）

### Changed

- 双语 README 改写：明确拆分 **v1.0（70）** vs **v0.x-draft（280）**，并澄清盲测只验触发、不验事实
- `ROADMAP.md` 记录三轮审计覆盖表与方法论结论（`v1.0` ≠ 已核事实）

---

## [2026-08-18] — 全库结构审计与机械修复

### Fixed

- 清除 `econ-macro-theories` **30** 个文件中泄漏的批量脚手架说明
- 修正 `business/org-it-intel-report` frontmatter（`author`/`version` 归入 `metadata`）
- 为 **50** 个 Skill 补齐模板强制的「常见误用」章节
- 抽样内容修复：`capm` Unicode 下标、`anchoring` 实验细节、`fisher-equation` vs `fisher-effect` 命名区分

### Added

- 可复用结构审计脚本：`internal/skill-creator/scripts/audit_repo_skills.py`（本地工具链；仓库 `.gitignore` 仍忽略 `internal/`）

---

## [2026-08-17] — 名录扩充分类批次，合计达到 350

### Added

- `learning-growth` 批次（+12 → 23）
- `strategy-competition` 批次（+12 → 24）
- `efficiency-execution` 批次（+12 → 21）
- `systems-complexity` 批次 M4b（+12 → 23）
- 库规模定格为 **350** 个可执行 Skill

### Changed

- 同步根 README / ROADMAP / 分类 README 计数，对齐 **350**

---

## [2026-08-16] — 学科域铺满、Phase 3 与 M1–M4 名录扩充

### Added

- 六个学科分类补至约 **30**/类
- Phase 3 打磨与全库 Skill README 索引
- 目录路线图与 **25** 个模型迁入新分类
- M1 `cognitive-thinking-tools`（→ 28）
- M2 / M2b `decision-probability`（→ 24）
- M3 learning / strategy / efficiency 填充（+19）
- M4 `systems-complexity`（+7 → 11）
- strategy：McKinsey 7S + GE–McKinsey matrix（+2）

### Changed

- Phase 3 分类 README 审阅
- Phase 3 相关模型双向链接

---

## [2026-08-15] — 立项、ThinkingModels 初库与分类规范化

### Added

- 项目定位、双语 README、`DESIGN.md`、`ROADMAP.md`
- 首批 Business + ThinkingModels（4 个种子：opportunity-cost、antifragility、occams-razor、socratic-questioning）
- ThinkingModels 扩至 **14**（含沉没成本、确认偏误、逆向、第一性原理等）
- 再增 6 个（库 **14 → 20**）
- batch 5–7 扩展（约 **20 → 61**）
- ThinkingModels batch 8：补齐剩余 8 个模型

### Changed

- `sales-company-intel-report` → `org-it-intel-report`，去掉厂商品牌表述
- 锐化 batch7-E 模型区分地图
- 经济学域拆分、分类目录名小写化

---

## 维护约定

1. **合入 `main` 的变更**：写入对应日期节点（或新建日期节点），只记调整内容。
2. **Unreleased**：尚未合入 `main` 的变更写在此节；合入后挪到带日期的章节。
3. **分类**：优先使用 `Added` / `Changed` / `Fixed` / `Removed` / `Deprecated`。
4. **首次打 tag 时**：可将最近一个稳定里程碑标为 `0.1.0`（或团队约定版本）。
