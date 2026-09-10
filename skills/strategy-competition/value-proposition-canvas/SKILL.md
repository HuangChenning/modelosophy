---
name: value-proposition-canvas
description: >
  用价值主张画布（Value Proposition Canvas）帮用户检验产品/功能是否真的匹配某个客户细分的需求：
  先独立列出客户画像（功能性/社会性/情感性任务、痛点、收益），再设计价值地图（产品服务、止痛药、
  增效剂）逐条对应，最后判断是否达成经过验证的"契合"。Use when user says "价值主张画布""Value
  Proposition Canvas""客户到底需要什么""这个功能有没有戳中客户痛点""产品和客户需求匹不匹配"。
  **硬区分 positioning**：要在客户心智里占据一个差异化认知位置 → positioning；要结构化拆解客户
  的具体 jobs/pains/gains 并逐条对应产品能力 → 本模型。**硬区分 business-model-canvas**：要
  描述整个商业模式九宫格 → business-model-canvas；只聚焦某一个客户细分的价值匹配 → 本模型。
  不适用于客户需求尚未被理解或快速变化的场景，也不适用于已有清晰认知定位、只需一句话陈述的场景。
metadata:
  author: modelosophy（蒸馏自 Alexander Osterwalder & Yves Pigneur《Value Proposition
    Design》(2014)，Strategyzer 团队维护与推广）
  version: v1.0
  source: Alexander Osterwalder & Yves Pigneur《Value Proposition Design》(Wiley, 2014)；
    Strategyzer 官方文章 "5 Common Mistakes to Avoid When Using the Value Proposition
    Canvas"；研究审计 docs/books/value-proposition-canvas-framework/
---

# 价值主张画布 Value Proposition Canvas

## 这是什么

**价值主张画布**是一套**结构化验证产品与客户需求是否匹配**的工具：把 Business Model Canvas 中"客户细分"与"价值主张"这两格放大，拆成两个独立模块逐条对应。

| 模块 | 包含内容 | 归属 |
|---|---|---|
| **Customer Profile 客户画像** | Jobs（functional/social/emotional 三类任务）、Pains（痛点）、Gains（期望收益） | 客户身上可观察到的东西，完全在你的直接控制之外 |
| **Value Map 价值地图** | Products & Services（产品/服务）、Pain Relievers（止痛药）、Gain Creators（增效剂） | 你设计进价值主张里、用来应对客户 Jobs/Pains/Gains 的东西，在你的控制范围内 |

它由 Alexander Osterwalder 与 Yves Pigneur 在《Value Proposition Design》(2014) 中正式发布，是《商业模式新生代》Business Model Canvas 的配套深化工具，由 Strategyzer 团队持续维护、培训并输出官方使用规范。

它的核心机制是**先独立观察，再设计对应，最后验证契合（fit）**：只有当 Value Map 里的某个元素被客户实际验证确实解决了 Profile 里的对应项，才算达成 fit；没有验证过的"感觉应该匹配"，画布上要求明确标注为"假设的 fit"而非已验证的 fit。

## 什么时候用

- "帮我理清这个产品到底解决了客户的什么需求"
- "我们做的功能，客户真的在乎吗，有没有遗漏什么痛点"
- 直接说价值主张画布 / Value Proposition Canvas
- 要为宣传手册/官网的"为什么选我们"部分找到真实、可验证的价值主张素材，而不是自说自话

**不要**当主模型：

- 用户要"在客户心智中占据一个差异化认知位置"的一句话定位陈述 → [`positioning`](../positioning/SKILL.md)
- 用户要描述整个商业模式（渠道、成本结构、关键伙伴等九个模块）→ [`business-model-canvas`](../business-model-canvas/SKILL.md)
- 用户要写一段具体的销售文案/广告 → `pas`（`skills/cognitive-thinking-tools/pas/SKILL.md`，若已蒸馏）

## 怎么用（执行步骤）

1. **独立填写 Customer Profile，完全不看自己的产品。** 判据：写下的每一条 Job/Pain/Gain，是否在"假装这家公司不存在"的前提下依然成立？如果某一条只有在提到你的产品时才说得通，说明是在"透过价值主张的镜片"编造需求，必须删除重写——这是官方总结的第一大常见误用。
2. **给每条 Job 标注类型（functional / social / emotional）。** 判据：这句话补上类型标签后是否依然成立？只写 functional jobs（"完成任务本身"）而漏掉 social（"想在他人面前显得怎样"）和 emotional（"想有什么感受"）是常见的不完整。
3. **给每条 Pain 标出严重程度/发生频率，不要只是空泛陈述"客户不喜欢 X"。** 判据：能否追问"这有多严重、多常见"给出一个大致量级？给不出量级的痛点优先级应该降低。
4. **设计 Value Map，逐条对应 Profile 里的具体项，并标注取舍。** 判据：每个 Pain Reliever/Gain Creator 是否能指出它对应 Profile 里的哪一条，而不是笼统地"我们的产品很好用"；同时明确哪些 Jobs/Pains/Gains 是刻意不满足的——试图满足每一条是官方点名的常见误用，聚焦比全覆盖更重要。
5. **标注哪些对应关系是已验证的 fit，哪些还只是假设。** 判据：这条对应关系背后有没有客户访谈、试用反馈或销售数据支撑？没有支撑的必须标"假设"，不能直接当成结论使用；下一步行动应该是设计一个低成本方式去验证这些假设。

## 例证

**Strategyzer 官方案例（框架维护方自述实践）**：多个使用画布的团队最初把 Customer Profile 写成"客户需要更快的处理速度、更低的价格"，完全是从自己产品功能反推出来的；改用"忘掉产品、像人类学家一样观察客户"的方法后，发现真正驱动购买决策的 emotional job 是"不想在同事面前显得落后于行业趋势"，这条 job 原方案完全没有对应设计。揭示 Customer Profile 与 Value Map 顺序颠倒会让画布沦为自我验证的形式主义。

**B2B SaaS 定价页常见案例（跨公司交叉验证的行业实践）**：多家 SaaS 公司在使用画布梳理定价页文案时发现，技术评审者（practitioner）关心的 Pain 是"配置复杂、上线慢"，而采购决策者（economic buyer）关心的 Gain 是"降低总拥有成本、便于审计"——同一产品需要在 Value Map 里为同一 Customer Profile 的不同角色设计不同的 Pain Reliever/Gain Creator 组合，揭示"客户"往往不是单一角色，画布填写前需要先明确具体是哪一类客户。

## 什么时候不适用（边界）

- **客户需求尚未被理解或快速变化**：画布的前提是"能相对稳定地观察到客户的 jobs/pains/gains"，如果目标客户群体本身还在快速演变、或团队对客户几乎一无所知 → 应先做探索性客户访谈/民族志研究积累素材，再回来用画布结构化，而不是凭空填格子。
- **已有清晰认知定位、只需一句话陈述**：如果目的只是"用一句话说清楚我们在客户心智中和竞品的差异"，画布的详细拆解反而是过度工程 → 改用 [`positioning`](../positioning/SKILL.md)。
- **需要描述整个商业模式的资源配置**：渠道、成本结构、关键伙伴关系等九宫格其余七个模块不在本画布覆盖范围内 → 改用 [`business-model-canvas`](../business-model-canvas/SKILL.md)。
- **一次性头脑风暴，无后续验证计划**：画布强调"fit"必须经过验证，如果团队只打算填一次就存档、不打算做客户验证 → 画布的核心价值（区分已验证与假设）无法体现，退化为普通的功能清单。

## 常见误用

- **透过价值主张的镜片写 Customer Profile**：只列自己产品解决的 jobs/pains/gains，画布必然显示"完美契合"，因为从一开始就是循环论证 → 回到步骤 1，假装不知道自己在卖什么。
- **一张画布混装多个客户细分**：不同角色的 jobs/pains/gains 互相打架，导致 Value Map 谁也对不上 → 按客户细分拆成多张独立画布。
- **只写 functional jobs，漏掉 social/emotional jobs**：价值主张显得"技术上对但没人在乎" → 回到步骤 2，逐条补类型标签。
- **试图满足每一个 job/pain/gain**：Value Map 铺得又宽又浅，没有真正聚焦的杀手级卖点 → 回到步骤 4，明确哪些是刻意不做的。
- **把"假设的 fit"当成"已验证的 fit"直接使用**：宣传手册/销售话术里写进了从未验证过的客户需求，一旦被客户当面质疑就站不住 → 回到步骤 5，标注验证状态，未验证的先去做验证。

## 相关模型

- **与[Positioning](../positioning/SKILL.md)**：**硬区分。** positioning 回答"在客户心智的认知阶梯上占据哪一个差异化位置"，产出是一句话定位陈述；本模型回答"客户到底有哪些具体的 jobs/pains/gains，我们的产品分别用什么应对、有没有遗漏"，产出是结构化拆解与验证状态。用户说"我们该怎么定位/差异化认知点是什么"→ positioning；说"产品到底戳中了客户的什么需求，有没有遗漏"→ 本模型。两者可以配合：先用本模型找到真正打动客户的 jobs/pains/gains，再提炼成 positioning 的一句话陈述。
- **与[Business Model Canvas](../business-model-canvas/SKILL.md)**：BMC 是九宫格描述整个商业模式（含渠道、成本结构、关键伙伴等）；本模型只是把 BMC 中"客户细分"+"价值主张"这两格单独放大做深度验证，是 BMC 的补充细化工具而非替代品。用户说"整个商业模式怎么画"→ business-model-canvas；说"具体到某个客户细分，我们的价值主张对不对"→ 本模型。
- **与 PAS/FAB/StoryBrand SB7**（`skills/cognitive-thinking-tools/`，若已蒸馏）：本模型产出的是"经过验证的客户需求与产品对应关系"这一素材，PAS/FAB/SB7 负责把这份素材写成具体的文案/说明/叙事——本模型在上游做需求验证，它们在下游做表达，不是同一层级的工具。

## 记忆钩子

先假装不知道自己在卖什么，看清客户真正要什么；再回头设计产品，去接住那些真实的需求。
