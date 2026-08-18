---
name: munger-misjudgment
description: >
  用查理·芒格《人类误判心理学》的 25 种心理倾向做检查清单扫描，并识别 Lollapalooza
  （多倾向同向叠加）结构；单倾向命中则路由到库内专用 bias skill 深挖，不在此重复写迷你教程。
  Use when user says “芒格误判”“人类误判心理”“25 种倾向”“心理倾向清单”“Lollapalooza”
  “多种偏见一起上”“帮我过一遍误判清单”。拒识：用户只要某一个已命名偏差的深度纠偏
  （确认偏差、损失规避、易得性等）→ 直接走对应专用 skill，不要在本 skill 展开全文。
metadata:
  author: modelosophy（蒸馏自 Charlie Munger《The Psychology of Human Misjudgment》/
    《穷查理宝典》倾向清单 + Lollapalooza + 《万物皆模型》人类误判心理卡片）
  version: v1.0
  source: docs/books/wanwu-jie-moxing/candidates/batch-8-remaining-eight.md
---

# 人类误判心理 Munger Misjudgment（清单路由）

## 这是什么

查理·芒格把常见判断失败整理为约 **25 种心理倾向**，核心用法不是背诵定义，而是：

1. **清单扫描**：决策前/复盘时对照，减少漏检；
2. **Lollapalooza**：多种倾向**同向叠加**时，错误会被极端放大（激励 + 权威 + 社会认同 + 损失厌恶同时开火）；
3. **逆向**：先问“标准误判会怎样搞砸这件事”，再设计防护。

本 skill 是**路由器 + 并发结构诊断器**：命中单倾向且库内已有专用 skill → **移交**细做；多倾向叠加 → 优先拆激励、权威、社会认同、剥夺反应等**并发结构**，再按需下钻。

**禁止**在此把 25 条每条写成迷你教程，避免与 [`confirmation-bias`](../../behavioral-biases/confirmation-bias/SKILL.md)、[`availability-heuristic`](../../behavioral-biases/availability-heuristic/SKILL.md)、[`loss-aversion`](../../behavioral-biases/loss-aversion/SKILL.md) 等重复堆砌。

## 什么时候用

- 重大投资、招聘、战略评审，需要“过一遍人类误判清单”；
- 怀疑多种偏见同时在起作用，而不只是某一个；
- 用户点名芒格 / 25 倾向 / Lollapalooza / 人类误判心理。

**不要**当主模型：
- 用户明确只要确认偏差 / 易得性 / 损失规避等**单一**纠偏 → 对应专用 skill；
- 纯学术史：“芒格哪年演讲” → 直接答知识，不跑清单协议；
- 需要情感支持而非决策审计。

## 怎么用（执行步骤）

1. **情景外化。** 写清：决策是什么、谁受益、时间压力、权威在场、钱/地位/面子是否卷入。没有情景，清单会变成抽象背书。
2. **快速扫描 25 倾向（见下表）。** 只标记“可能命中”的 3–7 条，并各用**一句**说明机制如何进场。不要对 25 条逐条作文。
3. **单倾向 → 路由。** 若某一条已有专用 skill（表中有链接），立即切换过去执行其步骤；本 skill 只保留“已路由”记录。
4. **多倾向 → Lollapalooza 协议。** 若 ≥3 条同向，优先拆结构而非提高“意志力”：
   - 改**激励**（奖励与惩罚超级反应）；
   - 降低**权威**不当权重或引入独立反对席；
   - 切断**社会认同**回声（匿名、外部基准、反从众样本）；
   - 重标**参照点**，削弱剥夺/损失框架绑架；
   - 强制冷却期，对抗怀疑回避与压力影响。
5. **产出防护清单。** 每条防护对应一个已标记倾向；写清“什么信号出现就暂停决策”。复盘时再扫一遍是否漏了叠加。

### 25 倾向一览（名称 + 一句话；有专用 skill 则链接）

| # | 倾向 | 一句话 | 路由 |
|---|---|---|---|
| 1 | 奖励与惩罚超级反应 | 激励扭曲认知与行为，人会为自利找理由 | 改激励结构；可与机会成本/博弈论连用 |
| 2 | 喜欢/热爱 | 爱屋及乌，低估所爱对象的缺陷 | — |
| 3 | 讨厌/憎恨 | 憎其余胥，低估所憎对象的优点 | — |
| 4 | 避免怀疑 | 为消除疑虑痛苦而过早下结论 | [`dual-process`](../dual-process/SKILL.md)（冷却） |
| 5 | 避免不一致 | 死守旧承诺与自我形象以维持一致 | [`sunk-cost`](../../behavioral-biases/sunk-cost/SKILL.md) / [`confirmation-bias`](../../behavioral-biases/confirmation-bias/SKILL.md) |
| 6 | 好奇心 | 探索欲；可对冲部分误判 | —（保护性倾向） |
| 7 | 康德式公平 | 对绝对公平的执念扭曲交易 | — |
| 8 | 艳羡/妒忌 | 相对地位驱动决策 | — |
| 9 | 回馈 | 互惠与以牙还牙过冲 | — |
| 10 | 简单联想 | 符号/刻板联想替代因果 | — |
| 11 | 避免痛苦的心理否认 | 拒认痛苦事实 | 常叠用 [`confirmation-bias`](../../behavioral-biases/confirmation-bias/SKILL.md) |
| 12 | 自视过高 | 高估自己与所有物 | [`dunning-kruger`](../../behavioral-biases/dunning-kruger/SKILL.md) |
| 13 | 过度乐观 | 愿望当概率 | [`prospect-theory`](../../behavioral-biases/prospect-theory/SKILL.md) |
| 14 | 被剥夺超级反应 | 对损失/差点失去的过激反应 | [`loss-aversion`](../../behavioral-biases/loss-aversion/SKILL.md) / [`prospect-theory`](../../behavioral-biases/prospect-theory/SKILL.md) |
| 15 | 社会认同 | 从众替代独立判断 | [`spiral-of-silence`](../spiral-of-silence/SKILL.md) |
| 16 | 对比错误反应 | 被对照物顺序/反差带偏 | — |
| 17 | 压力影响 | 过强压力损害认知 | — |
| 18 | 易得性错误衡量 | 生动易提案例权重过高 | [`availability-heuristic`](../../behavioral-biases/availability-heuristic/SKILL.md) |
| 19 | 不用就忘 | 技能与知识衰减 | [`forgetting-curve`](../../learning-growth/forgetting-curve/SKILL.md) |
| 20 | 化学物质误影响 | 酒精等扭曲判断 | —（建议 defer 专业/医疗） |
| 21 | 衰老误影响 | 认知老化相关失误 | —（非诊断） |
| 22 | 权威误影响 | 过度服从权威与头衔 | — |
| 23 | 废话倾向 | 空话挤占思维与议程 | — |
| 24 | 重视理由 | 有“因为”就更易顺从，理由可空洞 | — |
| 25 | **Lollapalooza** | 多倾向同向叠加产生极端结果 | **本 skill 主战场** |

证据筛选类误判常与 [`confirmation-bias`](../../behavioral-biases/confirmation-bias/SKILL.md) 叠用：芒格清单命中“避免不一致 / 否认 / 热爱”等时，用确认偏差 skill 做证据对抗。

## 例证

**庞氏/传销式叠加（Lollapalooza）**：奖励承诺（激励）+ 社会认同（别人都在赚）+ 权威背书 + 剥夺恐惧（“再不进场就没了”）同向开火。揭示清单的价值在**并发结构**，不在单条标签。

**董事会一致通过的高风险并购**：权威（CEO）+ 社会认同（无人唱反调）+ 避免怀疑（日程压力）+ 过度乐观。防护是独立反方席与预注册否决条件，而非“大家再客观一点”。

**个人大额决策**：自视过高 + 易得性（最近成功故事）+ 损失框架（“错过即亏”）。单条可路由；≥3 条则先拆框架与冷却。

**（原书卡片）25 格成语拼盘 + 实事求是流程图**：清单意识有用；局限是把每条写成迷你寓言且与库内 bias 重复，并缺少 Lollapalooza 操作协议。本 skill 收成路由表 + 叠加拆解，不复述 25 篇教程。

## 什么时候不适用（边界）

- **单偏差深挖**：已点名 confirmation / availability / loss aversion 等 → 专用 skill。
- **清单 completeness 幻觉**：勾完 25 格不等于决策正确；清单是漏检保险，不是真理机器。
- **道德化对方**：倾向描述的是机制，不是给对手贴永久人格污名。
- **医学化**：化学物质、衰老相关条目不作临床诊断；涉及健康交专业人士。
- **替代激励设计**：若根因是奖惩合同本身，改合同优先于心理说教。

## 常见误用

- **把清单写成小作文**：25 条逐一展开成教程式说明，而不是按步骤2只标记 3–7 条并各用一句话说明机制 → 变成资料汇编，失去诊断功能，命中的单条应移交专用 skill 深挖。
- **命中单条却赖着不走**：某个倾向已有专用 skill（如 confirmation-bias）却在本 skill 里继续展开分析，违反“单倾向→立即路由”的核心规则。
- **拿倾向词当骂人的话**：给某人贴上“他就是自视过高型人格”之类标签，把机制描述变成对人的道德污名。
- **扫完清单就收工**：走完 25 格便宣称已排除误判风险，却没有判断是否 ≥3 条同向叠加（步骤4 Lollapalooza 协议），也没产出步骤5的具体防护清单。

## 相关模型

- **与各专用 bias skill**：本模型扫描与路由；细节执行在 confirmation-bias、availability-heuristic、loss-aversion、prospect-theory、dunning-kruger、spiral-of-silence、forgetting-curve、dual-process 等。
- **与[逆向思维](../../cognitive-thinking-tools/inversion/SKILL.md)**：逆向问“如何失败”；本模型提供失败的标准心理菜单。可先清单后逆向补遗漏。
- **与[确认性偏差](../../behavioral-biases/confirmation-bias/SKILL.md)**：证据过滤的专用手术刀；芒格命中相关倾向时路由过去。
- **与[双系统](../dual-process/SKILL.md)**：压力与怀疑回避常走快系统；冷却是跨倾向通用防护。
---
