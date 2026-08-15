<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="modelosophy —— 项目名旁是漏斗与水滴组成的蒸馏标记">
</p>

modelosophy 把人类千年沉淀的思维模型，转化为 AI 可以直接调用的 Skill。

SWOT、第一性原理、MECE、复利思维、第二序思维……每一个思维模型都成为一个独立、可组合的 Skill，而不是知识库里的一段文字。AI 像人一样使用它们——拆解问题、构建策略、做出决策。

## 项目简介与现状

这个仓库还处于早期阶段。目前有两类 Skill：

- [`skills/Business/sales-company-intel-report`](skills/Business/sales-company-intel-report)：一个销售侧客户情报调研 Skill，用来演示本项目采用的 `SKILL.md` + 模板 + 脚本 结构。
- [`skills/ThinkingModels/`](skills/ThinkingModels)：思维模型库目前 14 个 Skill，包括机会成本、沉没成本、决策树、10/10/10、反脆弱、奥卡姆剃刀、确认性偏差、易得性启发、六顶思考帽、逆向思维、第一性原理、马斯洛需求层次、系统思维、苏格拉底式质疑。每个都按真实学科来源重新研究（而非照抄《万物皆模型》原书卡片），经过苏格拉底式质疑自检、盲测用例验证、以及官方 Skill 规范校验。SWOT、PDCA、MECE、复利思维、第二序思维等其余模型尚未蒸馏，研究进度见 [`skills/ThinkingModels/README.md`](skills/ThinkingModels/README.md)。

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

`<category>` 按领域给 Skill 分组——例如 `Business/` 用于销售与客户调研类 Skill，`ThinkingModels/` 用于思维模型类 Skill。

输出 HTML 报告的 Skill 需遵循 [`DESIGN.md`](DESIGN.md) 中定义的统一视觉规范。

## 局限性

思维模型库仍处于早期，目前覆盖 14 个模型（原书 13 个 + 方法论补充苏格拉底式质疑）。100 个模型里大多数还没开始蒸馏。随着库的扩张，Skill 的编写规范仍可能调整。

## 贡献一个思维模型

如果你有一个值得蒸馏的思维框架，欢迎按照上面的结构，新增一个 `skills/<category>/<name>/SKILL.md` 并提交 PR。

---

[English](README.md)
