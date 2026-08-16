---
name: pdca
description: >
  用 PDCA（计划-执行-检查-处理）做持续改进循环：Plan 定假设与度量，Do 小范围执行，Check/Study
  对照学习，Act 标准化或调整后进入下一圈；不是一次性瀑布。Use when user says “PDCA”“戴明环”
  “持续改进”“计划执行检查”“质量循环”“PDSA”。避免只计划不行动、只检查不处理、或把 Act
  变成追责仪式；单次循环解决不了的问题要显式留到下一圈。
metadata:
  author: modelosophy（蒸馏自 Shewhart/Deming PDCA·PDSA
    + 《万物皆模型》PDCA 卡片）
  version: v1.0
  source: docs/books/wanwu-jie-moxing/candidates/batch-5-priority.md
---

# PDCA（戴明环）

## 这是什么

PDCA = **Plan → Do → Check → Act**（Deming 常强调 **Study**，即 PDSA）：用短循环把改进建成组织习惯。Plan 写清目标、现状、根因假说与成功度量；Do 按计划小步试验；Check/Study 用数据对照假说；Act 将有效做法标准化，或修正假说进入下一轮。

它是**学习循环**，不是项目阶段闸门。把 PDCA 做成一年一次的大计划，就失去了“环”的意义。

## 什么时候用

- 质量、运营、个人习惯需要持续改进；
- 改动已做但不知是否有效、也未固化；
- 用户直接说 PDCA / 戴明环 / PDSA。

**不要**当主模型：战略内外盘点（SWOT）；拆分类结构（MECE）；设计增长因果闭环（飞轮）——飞轮可用 PDCA 改进各环，但先有闭环图。

## 怎么用（执行步骤）

1. **Plan：写假说，不是写愿望。** 包含：问题现状基线、拟议改动、预期可观测指标、试验范围与时限。
2. **Do：按范围执行，记下偏离。** 小样本优于大爆炸；执行中的现场笔记供 Study 使用。
3. **Check/Study：对照指标与假说。** 问：结果支持、否定还是不确定？避免只汇报“做完了”。Deming 强调学习，不只是合格检验。
4. **Act：标准化或弃子。** 有效 → 更新标准作业/文档并培训；无效 → 明确停止；未决 → 设计下一圈实验。把未解决问题**显式**放入下一 Plan，不假装本环已完美。
5. **保持环短。** 能一周验证的不拖一季；多环并行时每环有独立度量，避免搅成一锅。

## 例证

**制造质量改进**：缺陷率基线 → 改工艺参数 → 抽检对照 → 写入 SOP。揭示度量与标准化是 Act 的核心。

**个人学习**：计划阅读方法 → 两周试验 → 用测验分数 Study → 保留或更换方法。揭示个人场景同样适用。

**（原书卡片）多轮直至解决**：正确。须强调每环的假说与度量，以及 Act≠惩罚责任人。

## 什么时候不适用（边界）

- **真正的一次性不可逆决策**：用决策树/机会成本；PDCA 适合可迭代域。
- **指标缺失**：先建测量，再转环。
- **把 Check 当审判**：文化一惩罚，数据就假。

## 相关模型

- **与[飞轮](../../strategy-competition/flywheel/SKILL.md)**：飞轮定义推哪一环；PDCA 迭代怎么推。
- **与[系统思维](../../systems-classic-effects/systems-thinking/SKILL.md)**：Check 发现反弹时，升级画回路再 Plan。
- **与[逆向思维](../../cognitive-thinking-tools/inversion/SKILL.md)**：Plan 阶段可用事前验尸列出失败模式。
- **与[双系统](../../thinking-models/dual-process/SKILL.md)**：标准化（Act）把反复验证的做法交给习惯/System 1，节省慢思考。
---
