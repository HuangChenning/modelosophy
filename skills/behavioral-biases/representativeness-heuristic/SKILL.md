---
name: representativeness-heuristic
description: >
  用代表性启发检查用户是否用“像不像典型故事”代替概率与基率来判断。
  Use when user says “代表性启发”“representativeness”“看起来就像”“典型画像”“忽略基率”
  “工程师概率题”。不适用于确有强诊断性证据且已显式贝叶斯更新的情形。
metadata:
  author: modelosophy（蒸馏自Kahneman & Tversky 代表性启发 / 基率忽视）
  version: v0.x-draft
  source: docs/books/behavioral-biases/representativeness-heuristic/
---

# 代表性启发 Representativeness Heuristic

## 这是什么

**按对象与某个原型/刻板印象的相似程度来判断类别或概率，从而忽视基率、样本量与回归。**

典型表现：读完人格描述就猜职业，却不理该职业人口占比；把“连续上涨”当成“好公司原型”而忽略均值回归。它与可得性启发不同：可得性靠“容易想起”，代表性靠“像不像故事角色”。

## 什么时候用

- 刻板印象式人事/投资标签
- "这不就是当年的 XX 股/人吗"

**不要**当主模型：

- 因为新闻生动就高估频率 → [`availability-heuristic`](../availability-heuristic/SKILL.md)
- 小样本当规律 → [`law-of-small-numbers`](../law-of-small-numbers/SKILL.md)

## 怎么用（执行步骤）

1. **写出原型。** 用户用的“典型画像”是什么？列出相似特征。
2. **强制基率。** 在同类总体中，该类别先验概率是多少？写下来再谈相似度。
3. **拆诊断力。** 特征对类别的似然比是否真高？若特征在各类都常见，相似度几乎无信息。
4. **贝叶斯一句话重估。** 先验 × 证据强度 → 后验直觉；若与“很像所以就是”差距大，判定代表性绑架。

## 例证

**Linda 问题式合取谬误**：更“像”的故事被判更可能——揭示**代表性压过逻辑概率**。

**“像苹果的公司”估值**：叙事相似代替财务基率——揭示投资中的原型思维。

## 什么时候不适用（边界）

- **强信号特征**：DNA、明确资质等，相似度其实是高诊断力证据。
- **纯分类教学**：用原型入门可以，但决策时要补基率。

## 常见误用

- **反刻板=反代表性**：有时刻板印象含真实基率；要检的是“有没有把像当证据并忽略先验”。

## 相关模型

- **与[可得性启发](../availability-heuristic/SKILL.md)**：一个像不像，一个想不想得起。
- **与[小数定律](../law-of-small-numbers/SKILL.md)**：小样本“很像规律”常一起出现。
- **与[确认偏误](../confirmation-bias/SKILL.md)**：选定原型后只收相似证据。

## 记忆钩子

像不像故事，替代不了基率账。

