---
name: scale-free-network
description: >
  用无标度网络（scale-free，Barabási–Albert 等）理解度数幂律与枢纽：增长+优先连接如何产生 hub，以及抗随机故障/惧目标打击的特性。
  Use when user says “无标度”“幂律度数”“枢纽节点”“优先连接”“scale-free”“hub”。
  **硬区分**：小世界强调聚类与短路径；无标度强调 hub 度数分布。不适用于无度数证据却宣称无标度。
metadata:
  author: modelosophy（蒸馏自 Barabási–Albert 优先连接与网络科学无标度讨论；注意实证争议时仍用 hub 思维可操作）
  version: v0.x-draft
  source: Barabási–Albert；网络科学 hub/幂律；研究审计 docs/books/systems-complexity-m4/
---

# 无标度网络 Scale-Free Network

## 这是什么

**无标度网络**：节点度数分布近似**幂律**——多数节点度数低，少数**枢纽（hub）**度数极高。经典生成机制：**增长** + **优先连接**（新边更可能连到已有高连边节点）。操作含义：系统对**随机故障较韧**，对**蓄意打击枢纽较脆**；传播可经 hub 极速放大。

实证中「严格无标度」常有争议——**有无可观测 hub 与胖尾**往往比标签更重要。

## 什么时候用

- "是不是就几个关键节点撑着"
- "无标度 / 幂律度分布 / hub / 优先连接"
- 平台、航线、引文、供应链关键供应商

**不要**当主模型：
- 只要短路径+社区聚类 → [`small-world-network`](../small-world-network/SKILL.md)
- 网络效应定价/价值 → [`metcalfes-law`](../../systems-classic-effects/metcalfes-law/SKILL.md)
- 标准锁定 → [`lock-in-effect`](../../systems-classic-effects/lock-in-effect/SKILL.md)

## 怎么用（执行步骤）

1. **找候选 hub。** 谁被最多边依赖（度数、流量、依赖声明）？判据：列出 top 枢纽与依据。
2. **检查胖尾信号。** 是否「少数承担大部分连接」？无数据则用依赖访谈近似，并标注不确定。
3. **解释生成机制。** 是否存在优先连接（马太）与持续增长？判据：能说明 hub 如何越来越强。
4. **韧性设计。** 随机冗余 vs 保护/分散枢纽；避免单枢纽单点。判据：写出「去掉 top1/top3 会怎样」。
5. **传播与干预。** 要加速则借 hub；要抑制则隔离/降载 hub，而非只切边缘节点。
6. **警惕马太强化。** 政策是否在无意识喂养优先连接？需要时可引入多样性挂钩。

## 例证

**航空网络**：少数枢纽机场；天气/关闭枢纽冲击全局。揭示：惧目标打击。

**开源依赖**：左垫层库成 hub；供应链安全要审 hub。

**（原书卡片）**：避免只说「幂律很酷」；落到 hub 清单与韧性。

## 什么时候不适用（边界）

- **度数均匀的小团队网**：不必硬贴无标度。
- **无连接数据且无法近似**：先补依赖图。
- **纯内容质量问题**：拓扑模型帮不上。

## 常见误用

- **无数据喊无标度**：改为 hub 假设并验证。
- **与小世界互换**：问题不同。
- **只加枢纽不减压**：制造更脆系统。

## 相关模型

- **与[小世界网络](../small-world-network/SKILL.md)**：**硬区分。** 见上。
- **与[梅特卡夫定律](../../systems-classic-effects/metcalfes-law/SKILL.md)**：价值规模；本模型是度数异质结构。
- **与[马太效应](../../systems-classic-effects/matthew-effect/SKILL.md)**：优先连接是马太在网络上的机制。
- **与[锁定效应](../../systems-classic-effects/lock-in-effect/SKILL.md)**：hub 平台常伴随锁定；锁定专攻切换成本。

## 记忆钩子

先找那几个被所有人连的 hub——随机坏几个叶子往往无感，打掉 hub 才会地震。

