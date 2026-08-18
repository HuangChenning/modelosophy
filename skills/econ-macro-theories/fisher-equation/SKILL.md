---
name: fisher-equation
description: >
  用货币数量方程 MV=PQ 做货币—名义收入直觉推演，并严格检查 V 与 Y 假设。Use when MV=PQ、货币数量论、
  "印钱是不是一对一变通胀"。不适用于 V 剧烈波动时仍当精确预测式。**注意**：若用户说的是"费雪方程/
  费雪效应"且指名义利率≈实际利率+预期通胀，那是同名但不同的公式，应走
  [fisher-effect](../../finance-investing-models/fisher-effect/SKILL.md)。
metadata:
  author: modelosophy
  version: v0.x-draft
  source: Fisher；货币数量论；V 不稳定文献；研究笔记 docs/books/econ-knowledge-skills/
---

# 货币数量方程 Quantity Theory of Money (MV=PQ)

> **命名提醒**：这条也常被称作"费雪方程"（源自 Irving Fisher 的交易方程 MV=PQ），但英文语境下更常用 "Fisher equation" 特指**另一个**公式——名义利率≈实际利率+预期通胀（i≈r+πᵉ）。那个公式见 [fisher-effect](../../finance-investing-models/fisher-effect/SKILL.md)，本条目只讲 MV=PQ 这一支。

## 这是什么

**MV=PQ：货币量×流通速度≈物价水平×产出；常用于名义锚定直觉。**

提出者/源流：Irving Fisher（货币数量方程传统）。若 V 相对稳定、短期 Y 粘在潜在水平附近，则 M 增长主要映入 P。现实中 V 不稳、Y 可变，故方程是会计恒等+行为假设，不是自动政策机器。

## 什么时候用

用户出现以下意图时启用本 Skill：

- "「货币增速和名义 GDP 对得上吗」"
- "「印钱是不是一对一变通胀」"

**不要**在以下情况套用本模型：

- 泰勒规则利率反应函数主场
- 费雪效应（利率—通胀）若用户明确问名义利率构成——在本 skill 内短辨后可答，但主公式仍 MV=PQ 清单条目

## 怎么用（执行步骤）

每一步给出可操作判据；禁止只换说法重复结论。

1. **写恒等 vs 假设。** MV≡PQ 会计；「V 稳、Y 潜在」才是数量论跃迁。
2. **观察 V 是否漂移。** 金融创新、流动性偏好改变 V。
3. **分短期/长期。** 短期 Y 可动；长期更多进 P（货币主义叙事）。
4. **政策翻译降级。** 方向直觉可用；禁止精密点预测。若问利率与通胀：单列费雪效应 i≈r+πᵉ。

## 例证

**费雪交易方程教学**：揭示名义记账骨架。

**大萧条 V 崩溃**：揭示只盯 M 不够。

**数字支付与 V**：揭示制度改变速度。

## 什么时候不适用（边界）

- **流动性陷阱/QE**：基础货币↑未必进宽货币与支出。
- **供给冲击抬 P**：即便 M 未动。

## 常见误用

- **把恒等当因果**：PQ 也可驱动 M 内生。
- **忽视 V**：机械货币主义。

## 相关模型

- **与[费雪效应](../../finance-investing-models/fisher-effect/SKILL.md)**：同源不同公式——本条目是 MV=PQ（货币—物价）；费雪效应是 i≈r+πᵉ（名义—实际利率）。用户说"费雪方程"但问的是利率，走费雪效应。
- **与[货币主义](../monetarism/SKILL.md)**：政策化数量论。
- **与[MMT](../modern-monetary-theory/SKILL.md)**：对「钱从哪来」叙事冲突——对照用。
- **与[泰勒规则](../taylor-rule/SKILL.md)**：利率工具时代的名义锚操作。
- **与[购买力平价](../purchasing-power-parity/SKILL.md)**：名义量；汇率与货币通胀联动叙事可拼。

## 记忆钩子

票子转得快、货少价就跳——但「转得快」本身会变。
