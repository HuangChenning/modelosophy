---
name: small-world-network
description: >
  用小世界网络（Watts–Strogatz）理解高聚类 + 短平均路径的结构：少量「长程捷径」如何剧烈缩短分隔并改变传播。
  Use when user says “小世界”“六度分隔”“聚类高但路径短”“small world”“捷径边”。
  **硬区分**：无标度强调枢纽度数幂律；小世界强调聚类与短路径共存。不适用于把任何病毒式传播都叫小世界。
metadata:
  author: modelosophy（蒸馏自 Watts & Strogatz 小世界模型与网络科学教学）
  version: v0.x-draft
  source: Watts–Strogatz small-world；网络科学；研究审计 docs/books/systems-complexity-m4/
---

# 小世界网络 Small-World Network

## 这是什么

**小世界网络**：相对规则网络，节点仍保持**高聚类**（朋友的朋友也常互识），但因存在少量**长程随机边（捷径）**，**平均路径长度**变得很短（接近随机网）。经典参照：Watts–Strogatz 在环上重连边的模型；日常隐喻「六度分隔」。

## 什么时候用

- "为什么加几条跨部门桥就通了"
- "小世界 / small world / 捷径 / 六度"
- 传播、协作、谣言在「圈内密、圈间偶有桥」的结构

**不要**当主模型：
- 枢纽度幂律、抗攻击脆弱 → [`scale-free-network`](../scale-free-network/SKILL.md)
- 网络效应价值计量 → [`metcalfes-law`](../../systems-classic-effects/metcalfes-law/SKILL.md)
- 路径锁定标准战 → [`path-dependence`](../../systems-classic-effects/path-dependence/SKILL.md) / [`lock-in-effect`](../../systems-classic-effects/lock-in-effect/SKILL.md)

## 怎么用（执行步骤）

1. **画/估局部聚类。** 社区内边是否很密？判据：能指出团块。
2. **测或估平均路径。** 跨团沟通要几跳？判据：有「很长」的痛点故事或数据。
3. **找或设计捷径。** 跨团角色、旋转岗位、弱连接引入。判据：捷径两端落在不同高聚类团。
4. **评估传播双刃剑。** 捷径加速创新也加速风险/谣言。判据：列出要加速与要阻挡的流。
5. **干预后复测。** 路径是否缩短？聚类是否被破坏过度（变成过度随机、信任下降）？

## 例证

**科研合作**：实验室内密合作 + 会议带来的跨机构弱连接 → 小世界式知识扩散。

**公司部门墙**：加「联络人/章节制」等于加捷径，常比全员大会更有效。

**（原书卡片）**：六度是通俗说法；以聚类+短路径结构为准。

## 什么时候不适用（边界）

- **极小完全图**：无需小世界语言。
- **关键是度数枢纽**：转无标度。
- **无图结构的纯内容问题**：先内容策略。

## 常见误用

- **有传播=小世界**：可能是无标度枢纽驱动。
- **无限加捷径**：聚类/规范被冲掉。
- **与梅特卡夫混用**：梅特卡夫谈价值随规模；小世界谈拓扑形状。

## 相关模型

- **与[无标度网络](../scale-free-network/SKILL.md)**：**硬区分。** 短路径+高聚类 → 小世界；幂律枢纽 → 无标度。可重叠但问题不同。
- **与[梅特卡夫定律](../../systems-classic-effects/metcalfes-law/SKILL.md)**：价值/规模；本模型是结构。
- **与[涌现](../emergence/SKILL.md)**：短路径上的传播模式常是涌现现象。
- **与[反馈回路](../../systems-classic-effects/feedback-loops/SKILL.md)**：网络上的传播可再画回路；先定拓扑再定回路。
- **与[网络拓扑](../network-topology/SKILL.md)**：拓扑是度量入口；已确认高聚类+短路径再用本专条。

## 记忆钩子

团内要密，团间要有几座桥——桥是捷径，也是双刃剑。

