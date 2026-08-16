<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="modelosophy —— 项目名旁是漏斗与水滴组成的蒸馏标记">
</p>

modelosophy 把人类千年沉淀的思维模型，转化为 AI 可以直接调用的 Skill。

SWOT、第一性原理、MECE、复利思维、第二序思维……每一个思维模型都成为一个独立、可组合的 Skill，而不是知识库里的一段文字。AI 像人一样使用它们——拆解问题、构建策略、做出决策。

## 项目简介与现状

这个仓库还处于早期阶段。Skill 按领域放在 `skills/<category>/` 下：

- [`skills/business/org-it-intel-report`](skills/business/org-it-intel-report)：与厂商无关的组织 / IT 情报调研 Skill（组织整体情况 + IT 投入与招投标），演示 `SKILL.md` + 模板 + 脚本结构。
- [`skills/thinking-models/`](skills/thinking-models)：现 **50** 个可执行思维模型 Skill（通用推理、战略、学习、领导等）。另有 **19** 个原属本库的 Skill 已迁入下方学科分类。完整索引见 [`skills/thinking-models/README.md`](skills/thinking-models/README.md)。
- 与 `business/` / `thinking-models/` **平级**的六个学科分类（均为**可执行** Skill，不是知识卡壳；大量条目仍为 `v0.x-draft`）：
  - [`econ-macro-theories`](skills/econ-macro-theories) — 宏观理论（**30**）
  - [`econ-micro-markets`](skills/econ-micro-markets) — 微观 / 市场（**30**）
  - [`game-theory-models`](skills/game-theory-models) — 博弈论（**31**）
  - [`behavioral-biases`](skills/behavioral-biases) — 行为经济学与偏误（**30**）
  - [`finance-investing-models`](skills/finance-investing-models) — 金融 / 投资（**30**）
  - [`systems-classic-effects`](skills/systems-classic-effects) — 系统与经典效应（**30**）

早期「9 字段知识卡」方案已废弃为主交付；其中有用字段（提出者、常见误用、记忆钩子等）可吸收进可执行 `SKILL.md`。计划见 [`ROADMAP.md`](ROADMAP.md)。

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

`<category>` 按领域分组——例如 `business/`、`thinking-models/`，以及上述六个经济学 / 偏误 / 系统分类。

输出 HTML 报告的 Skill 需遵循 [`DESIGN.md`](DESIGN.md) 中定义的统一视觉规范。

## 局限性

库仍处于早期：跨分类合计约 **~230** 个可执行模型（`thinking-models/` 50 + 六学科分类约 181 + `business/`）。清单新补条目多为 `v0.x-draft`，尚待压力测试；编写规范仍可能随库扩张调整。

## 贡献一个思维模型

如果你有一个值得蒸馏的思维框架，欢迎按照上面的结构，新增一个 `skills/<category>/<name>/SKILL.md` 并提交 PR。

---

[English](README.md)
