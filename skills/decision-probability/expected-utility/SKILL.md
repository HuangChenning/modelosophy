---
name: expected-utility
description: >
  用期望效用（expected utility）在结果金额对决策者「不线性」时做选择：EU = Σ pᵢ·u(xᵢ)，
  显式处理风险厌恶、破产与尾部，避免「正 EV 就该上」。Use when user says “期望效用”
  “风险厌恶”“效用函数”“同样期望值为啥我不赌”“St. Petersburg”。**硬区分**：
  风险中性、金额可线性比 → expected-value；仓位公式 → kelly-criterion；
  深度不确定防归零结构 → antifragility。不适用于效用不可言说却硬套精确 u(·)。
metadata:
  author: modelosophy（蒸馏自 von Neumann–Morgenstern 期望效用与决策分析实践；
    区分经典 EV）
  version: v0.x-draft
  source: vNM 期望效用；决策分析；研究审计 docs/books/decision-probability-m2/
---

# 期望效用 Expected Utility

## 这是什么

**期望效用**：当结果要用**效用** \(u(x)\) 而非原始金额 \(x\) 来比较时，选择最大化

\[
\mathrm{EU} = \sum_i p_i\, u(x_i)
\]

的行动。von Neumann–Morgenstern 理论给出：在一组公理下，偏好可用效用的概率加权表示。

**与期望值的硬区分**：EV 假设「一块钱的价值处处相同」（风险中性近似）。现实中，亏损半身家与多赚一笔奖金对效用冲击不对称——此时正 EV 赌局仍可合理拒绝。

## 什么时候用

- "EV 为正但我害怕归零"
- "保险明明负 EV 为啥还买"
- "风险厌恶 / 效用 / 确定性等价"
- 金额跨度大、涉及生存、声誉或流动性约束的不确定选择

**不要**当主模型：

- 小额、可重复、无破产、近似线性 → [`expected-value`](../expected-value/SKILL.md)
- 多阶段决策节点与信息价值 → [`decision-tree`](../decision-tree/SKILL.md)（叶子可用 EU 折叠）
- 要设计「下行有限、从波动获益」的结构 → [`antifragility`](../../learning-growth/antifragility/SKILL.md)
- 重复优势下的最优仓位比例 → [`kelly-criterion`](../../finance-investing-models/kelly-criterion/SKILL.md)

## 怎么用（执行步骤）

1. **确认为何 EV 不够。** 写出非线性来源：破产、最低生活线、凹效用、损失厌恶等。若说不出，先用 EV。
2. **列结果表 \((p_i, x_i)\)。** 与 EV 相同，概率来源标注清楚。
3. **选定效用表达（可粗糙）。** 例如：对数财富、分段（低于阈值极低效用）、或「确定性等价」访谈（「确定拿多少 ≈ 该赌局」）。判据：最坏结局的效用是否被单独钉死为不可接受。
4. **算 EU 或比确定性等价。** 比较行动 A/B 的 EU；展示对 \(u\) 形状的敏感性。
5. **硬约束优先于 EU 排序。** 任何导致不可逆归零/违法/安全事故的分支，直接剔除，不参与平均。
6. **输出「可接受集合」而非假精确最优。** 效用形状不确定时，给稳健可接受行动，而非三位小数 EU 冠军。

## 例证

**圣彼得堡悖论**：EV 无穷的抛硬币赌局，无人愿付巨款——直观推动「边际效用递减 / 效用有界」思想史。揭示：EV 可荒谬，EU 才贴近真实拒绝。

**保险**：保单对保险公司与客户常是负 EV 转移，但客户用 EU（或风险厌恶）购买尾部保护合理。揭示：负 EV ≠ 非理性。

**创业 All-in**：期望回报表漂亮，但失败=家庭资产负债表归零 → EU/硬约束否决；应缩仓或 [`reversible-irreversible`](../reversible-irreversible/SKILL.md) 拆步。

## 什么时候不适用（边界）

- **效用无法稳态表达**：情绪波动极大、多元不可公度目标 → 先多属性拆解或满意化（见 [`bounded-rationality`](../../game-theory-models/bounded-rationality/SKILL.md)）。
- **概率不可校准**：精致 \(u\) 乘垃圾 \(p\) 仍是垃圾 → 先基率/贝叶斯或反脆弱。
- **前景理论情境**：描述性偏差主导时，EU 是规范基准，不是人类实际行为模型 → 参照 [`prospect-theory`](../../behavioral-biases/prospect-theory/SKILL.md)。

## 常见误用

- **用 EU 包装梭哈**：随便画一个凹函数仍接受归零 → 硬约束未生效。
- **与 EV 混称**：口头「期望」实指金额加权 → 走 [`expected-value`](../expected-value/SKILL.md)。
- **精确 \(u(x)=\ln x\) 教条**：无财富数据时假精确 → 用区间与确定性等价。
- **忽略概率来源**：只美化效用曲线。

## 相关模型

- **与[期望值](../expected-value/SKILL.md)**：**硬区分。** 金额近似线性、无出局 → EV；非线性偏好/破产 → EU。
- **与[前景理论](../../behavioral-biases/prospect-theory/SKILL.md)**：前景理论描述人如何扭曲 \(p\) 与价值；EU 是规范选择基准。纠偏时两者对照。
- **与[损失厌恶](../../behavioral-biases/loss-aversion/SKILL.md)**：损失厌恶改变有效价值函数；决策时要显式承认，勿假装风险中性。
- **与[凯利准则](../../finance-investing-models/kelly-criterion/SKILL.md)**：凯利可视为对数效用下的增长最优仓位；本模型更一般，不限于重复下注公式。
- **与[反脆弱](../../learning-growth/antifragility/SKILL.md)**：EU 仍依赖概率模型；模型不可得时改结构设计暴露。

## 记忆钩子

钱的期望 ≠ 你的期望；**先问最坏结局能不能活，再谈平均赚多少。**
