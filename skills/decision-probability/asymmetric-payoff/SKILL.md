---
name: asymmetric-payoff
description: >
  用不对称回报/风险不对称思维筛选「下行有限、上行开放」或相反的暴露结构，比较左尾与右尾
  而非只看均值。Use when user says “不对称回报”“风险不对称”“上行空间下行有限”
  “asymmetric payoff / convex payoff”。**硬区分**：反脆弱/杠铃结构设计 → antifragility；
  金额期望 → expected-value；效用/破产 → expected-utility；仓位公式 → kelly-criterion。
  不适用于把任何正偏口头标成不对称却不肯画损益轮廓。
metadata:
  author: modelosophy（蒸馏自期权思维与 Taleb 等强调的 payoff asymmetry；
    与 antifragility 互链不复制杠铃专论）
  version: v0.x-draft
  source: 不对称损益 / 期权式暴露；研究审计 docs/books/decision-probability-m2b/
---

# 不对称回报 Asymmetric Payoff

## 这是什么

**不对称回报**：评价行动时，显式比较**上行潜力与下行风险的不对称性**——关注损益函数的形状（凸/凹、有界/无界、触发条件），而不是只比较期望值或「成功率」。典型偏好结构：**下行截断或有界、上行保留期权性**；反之则应警惕。

它是筛选与比较**暴露形状**的透镜；系统化「从波动中获益」的设计细节见反脆弱，本条不复制杠铃专论。

## 什么时候用

- "这个机会是否不对称？下行有限吗"
- "风险不对称 / asymmetric / 凸性收益"
- "期权式思维：最坏多少、最好怎样"
- 创业赌注、谈判条款、研发组合、保险与对冲选择

**不要**当主模型：

- 要设计杠铃/反脆弱组合与限敞口工艺 → [`antifragility`](../../learning-growth/antifragility/SKILL.md)
- 只要算 Σp·x → [`expected-value`](../expected-value/SKILL.md)
- 非线性效用与归零约束主导 → [`expected-utility`](../expected-utility/SKILL.md)
- 重复优势下最优仓位 → [`kelly-criterion`](../../finance-investing-models/kelly-criterion/SKILL.md)

## 怎么用（执行步骤）

1. **画出损益轮廓（payoff sketch）。** 横轴情景/状态，纵轴盈亏；标出最坏、中位、最好。判据：他人能据此重画。
2. **钉死下行：有界还是可归零/可负债？** 写清法律责任、杠杆、声誉连锁。无界下行默认危险。
3. **钉死上行：封顶还是开放？路径依赖？** 期权到期、竞争跟进、容量约束会切掉上行。
4. **与代价比对。** 为这不对称付出的权利金/时间/机会成本是否可接受（链 [`opportunity-cost`](../../econ-micro-markets/opportunity-cost/SKILL.md)）。
5. **检查隐蔽对称化。** 合同、清算、平台规则是否在压力下把「有限下行」变成无限？
6. **决策规则。** 优先保留/购买正不对称；对负不对称要求更高补偿或拒绝；规模用限损而非均值诱惑。

## 例证

**早期股权 vs 工薪加杠杆炒币**：前者下行常以投入为限、上行开放；后者常对称或更糟。揭示：**形状先于故事**。

**保险**：付小额权利金，买断左尾。揭示：负 EV 可因不对称仍合理（并接 EU）。

**「稳赚」高杠杆策略**：口头不对称，实为左尾肥大。揭示：必须画轮廓验真伪。

## 什么时候不适用（边界）

- **无法描述情景轴**：先澄清状态再谈形状。
- **纯公平博弈且可重复小注**：EV/凯利可能更直接。
- **道德/法律禁止的不对称**：转嫁伤害给他人不算有效策略。

## 常见误用

- **口头「不对称」无轮廓**：口号。
- **与反脆弱混称**：反脆弱是系统对波动的反应设计；本模型先鉴别单笔暴露形状。
- **忽略权利金与隐性负债**：假有限下行。
- **用成功率替代尾部**：70% 小赢 vs 30% 爆仓仍可能很糟。

## 相关模型

- **与[反脆弱](../../learning-growth/antifragility/SKILL.md)**：**硬区分/连用。** 本模型筛 payoff 形状；反脆弱讲如何构造从波动获益的系统（含杠铃）。要「怎么建」走反脆弱；要「这笔划不划算的形状」走本模型。
- **与[期望值](../expected-value/SKILL.md)**：EV 压成一个数；不对称要求看分布形状。正 EV + 负不对称可拒绝。
- **与[期望效用](../expected-utility/SKILL.md)**：EU 用效用编码对尾部的态度；不对称先把尾部形状摆上台面。
- **与[凯利准则](../../finance-investing-models/kelly-criterion/SKILL.md)**：形状可接受后，重复下注用凯利定尺寸。
- **与[可逆与不可逆决策](../reversible-irreversible/SKILL.md)**：不可逆常放大下行不对称，需更重审查。

## 记忆钩子

先画最坏与最好；**均值再好看，左尾无界也不碰。**
