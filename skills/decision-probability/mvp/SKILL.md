---
name: mvp
description: >
  用最小可行性产品（MVP）以最小成本获得关于关键假设的真实学习信号，避免把「简陋版全家桶」
  当成验证。Use when user says “MVP”“最小可行”“先做一版验证”“lean startup”“别过度建设”。
  **硬区分**：可逆门分型 → reversible-irreversible；对抗节奏 → ooda-loop；完整实验设计/证伪 →
  hypothesis-testing。不适用于安全关键系统用「最小」省略防护。
metadata:
  author: modelosophy（蒸馏自 Eric Ries Lean Startup 的 MVP 学习导向定义 + Frank Robinson 术语起源
    讨论；强调 validated learning 而非“先丑后美”）
  version: v0.x-draft
  source: Lean Startup / MVP 实践文献；研究审计 docs/books/decision-probability-m2/
---

# 最小可行性产品 MVP

## 这是什么

**MVP（Minimum Viable Product）**：能用**最小投入**测试关键商业/产品假设、并产生**可决策学习**的最小制品或体验——可以是 Concierge、假门（fake door）、落地页、手工交付，不一定是可扩展软件。

核心不是「做小一点的完整产品」，而是：**哪条假设最危险，就用最省的方式打那条假设**。若「MVP」做完后你仍不知道假设真假，它就不是 MVP，只是缩水发布。

## 什么时候用

- "先做个 MVP 验证需求"
- "别把资源砸进没人要的功能"
- "lean / 最小可行 / 假门测试"
- 不确定性高、可逆或可拆成可逆前缀的产品与服务探索

**不要**当主模型：

- 只问门可不可逆、还没设计试验 → [`reversible-irreversible`](../reversible-irreversible/SKILL.md)
- 要写可证伪指标与对照 → 连用 [`hypothesis-testing`](../../cognitive-thinking-tools/hypothesis-testing/SKILL.md)
- 军事/对抗周期速度 → [`ooda-loop`](../ooda-loop/SKILL.md)
- 品牌/合规要求完整合格交付的场景（医疗器械等）→ 监管路径优先

## 怎么用（执行步骤）

1. **写下最危险假设（leap of faith）。** 一条句：若假，整条业务叙事崩。判据：团队同意「这条错了就停」。
2. **定义成功/失败学习信号。** 事前写阈值（如「100 访问、≥10% 付费意向」）。禁止上线后再解释「其实也算成功」。
3. **枚举候选试验，选信息量/成本比最高者。** 落地页、Wizard of Oz、原型访谈、限量预售……判据：能否在时间盒内得到信号。
4. **砍掉与假设无关的完整性。** 每加一个功能，问「它改变对假设的学习吗？」否 → 删。
5. **执行、测、记录，再决定 pivot/persevere/stop。** 决策必须引用第 2 步阈值，不引用沉没工时。
6. **若要加码，重评门型与下一假设。** 新假设新 MVP；禁止「既然做了就做全」。

## 例证

**Dropbox 视频演示**：未建完整同步前用视频测需求热度。揭示：MVP 可以是演示，学习的是需求假设。

**Concierge MVP**：先人工交付服务流程，验证付费意愿与流程，再自动化。揭示：可行性含「愿付」与「可交付」，不单是代码。

**反例：缩水全家桶**：把路线图功能各做 20%，无单一假设、无阈值——上线后仍不知用户要什么。揭示：小 ≠ Viable-for-learning。

## 什么时候不适用（边界）

- **安全/隐私/生命相关最小省略**：防护不是「非核心功能」。
- **平台信任已建立、边际功能明确**：继续 MVP 仪式会拖慢交付 → 常规迭代即可。
- **不可逆大规模承诺**：不能用 MVP 掩盖单向门（如全员迁移无回滚）。

## 常见误用

- **MVP = 简陋完整版**：未钉假设 → 重做步骤 1–2。
- **用虚荣指标**：下载量无行为 → 换学习指标。
- **沉没成本加码**：「都做了就做完」→ [`sunk-cost`](../../behavioral-biases/sunk-cost/SKILL.md)。
- **与快速试错口号等同**：无假设无阈值的乱动不是 MVP。

## 相关模型

- **与[可逆与不可逆决策](../reversible-irreversible/SKILL.md)**：先确认试验反悔成本可接受，再 MVP。
- **与[假设检验](../../cognitive-thinking-tools/hypothesis-testing/SKILL.md)**：MVP 是假设检验的产品形态。
- **与[计划谬误](../planning-fallacy/SKILL.md)**：完整版工期易乐观；MVP 用学习范围对抗范围膨胀。
- **与[机会成本](../../econ-micro-markets/opportunity-cost/SKILL.md)**：过度建设的代价是未做的验证与其他投注。
- **与[反脆弱](../../learning-growth/antifragility/SKILL.md)**：小暴露试错符合下行有限；但勿在归零域「试」。

## 记忆钩子

MVP 的 V 是 **Viable for learning**，不是 Viable as a tiny final product。
