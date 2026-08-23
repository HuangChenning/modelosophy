---
name: huawei-customer-insight
description: >
  当用户需要分析一家具体客户/公司/企业时使用。包括：
  (1) 客户深度调研与画像分析
  (2) 客户决策链与权力地图梳理
  (3) 竞争格局与差异化切入点分析
  (4) 客户需求分析与 $APPEALS 对标
  (5) 客户分级与价值评估
  触发词：客户洞察、客户分析、客户画像、决策链分析、权力地图、客户分级、$APPEALS、客户需求分析、华为客户分析、MCR、客户业务全景、竞争格局分析
metadata:
  author: modelosophy
  version: v1.0
  category: business
  tags:
    - customer-insight
    - huawei-mcr
    - decision-chain
    - appeals
    - competitive-landscape
---

# 华为客户洞察分析模型 (huawei-customer-insight)

按照华为 MCR（Manage Client Relationship）客户关系管理体系，对指定目标客户进行三维度（业务全景 + 决策链 + 竞争格局）+ 两扩展（客户价值识别 + 需求挖掘）的结构化深度分析，输出标准化客户洞察报告。

---

## 🧭 References 导航表

详细分析框架与工具指南请在对应步骤中查阅相关 reference 文件：

| 阶段 / 维度 | 对应 reference 文件 | 核心内容 |
|------------|-------------------|---------|
| 维度一：客户业务全景 | [`references/business-panorama.md`](references/business-panorama.md) | 六项框架 (战略/架构/经营/流程/痛点/规划) + FAN/PEST/五力 |
| 维度二：客户决策链洞察 | [`references/decision-chain.md`](references/decision-chain.md) | UB/SP/TB/EB 四角色模型 + 权力地图 + 关系 5 级评分 |
| 维度三：竞争格局分析 | [`references/competitive-landscape.md`](references/competitive-landscape.md) | 供应商格局 + 竞争雷达图 + SWOT + 差异化突破口 |
| 扩展：客户价值识别 | [`references/customer-value.md`](references/customer-value.md) | 付费能力/需求潜力/合作粘性三维评估 + S/A/B/C 分级策略 |
| 扩展：客户需求挖掘 | [`references/demand-mining.md`](references/demand-mining.md) | $APPEALS 八维度对标 + 四层需求模型 + SPIN 提问法 |
| 辅助分析工具速查 | [`references/tools-guide.md`](references/tools-guide.md) | 9 大工具 (PEST/五力/SWOT/VRIO/SPAN/FAN/Gartner/雷达图/TAM) |
| 报告 Markdown 模板 | [`assets/report-template.md`](assets/report-template.md) | 标准化客户洞察报告结构模板 |

---

## ⚡ 核心工作流 (Main Workflow)

```
[Step 1: 信息采集与补充] ──> [Step 2: 业务全景] ──> [Step 3: 决策链洞察]
                                                            │
[Step 7: 标准报告输出] <── [Step 6: 分级策略] <── [Step 5: 扩展分析] <── [Step 4: 竞争格局]
```

### Step 1: 客户信息采集与深度判定
1. **收集基础信息**：引导用户提供目标客户名称（必须）、所属行业（必须）、已知背景（营收/规模）、分析目的及已知关键决策人。
2. **搜索补充**：优先通过 WebSearch 补充客户官网、财报、新闻资讯。公开渠道无法确认的信息标记为`[需补充]`，切勿捏造。
3. **分析深度自适应判定**：
   - **快速扫描 (Quick Scan)**：仅有客户名称/简要背景 $\to$ 输出 1-2 页三维度概要 + 分级建议。
   - **标准分析 (Standard)**：有客户名称+行业+基本背景 $\to$ 输出 3-5 页三维度完整 + 两扩展概要。
   - **深度分析 (Deep Dive)**：信息充分或明确要求深度分析 $\to$ 输出 5-10 页全维度完整报告。

### Step 2: 维度一 — 客户业务全景研究
按照 [`references/business-panorama.md`](references/business-panorama.md) 展开：
- 逐项分析：发展战略、组织架构、经营状况(FAN)、业务流程(五力)、核心痛点、未来规划(PEST/Gartner/TAM)。
- 产出“客户生意说明书”，明确标注信息来源（用户提供 / 公开搜索 / 需补充）。

### Step 3: 维度二 — 客户决策链洞察
按照 [`references/decision-chain.md`](references/decision-chain.md) 展开：
- 划分决策链四角色：**EB（决策者）**、**TB（把关者）**、**SP（建议者）**、**UB（使用者）**。
- 分析每角色的利益诉求（业务+个人）、决策权重、沟通风格（控制/分析/倡导/亲切）、马斯洛需求与关系状态 (-1 到 3 分)。
- 绘制权力地图，识别显性与隐性决策影响线。

### Step 4: 维度三 — 竞争格局分析
按照 [`references/competitive-landscape.md`](references/competitive-landscape.md) 展开：
- 梳理现有供应商格局与份额估算、合作历史、客户抱怨信号。
- 构建竞争雷达图打分与 SWOT 优劣势对标。
- 划分阵地并识别差异化切入点（如：边缘突破、服务响应差异化、技术代差）。

### Step 5: 扩展维度分析（标准/深度分析时执行）
- **客户价值识别**：参阅 [`references/customer-value.md`](references/customer-value.md)，进行付费能力(FAN)、需求潜力(TAM/SAM/SOM)、合作粘性(VRIO) 三维评估。
- **客户需求挖掘**：参阅 [`references/demand-mining.md`](references/demand-mining.md)，进行 $APPEALS 八维度打分对标 + 四层需求（显性/隐性/战略/生态）拆解。

### Step 6: 客户分级与资源策略建议
- 按 **S/A/B/C** 标准完成客户分级建议（S 级战略 / A 级伙伴 / B 级价值 / C 级长尾）。
- 匹配资源策略（如：S 级配备“铁三角”团队 AR/SR/FR + 高层赞助人饱和攻击）。

### Step 7: 生成标准化客户洞察报告
- 复制并使用 [`assets/report-template.md`](assets/report-template.md) 结构模板，填充分析结论。
- 附录全量标明信息来源清单与待补充项。

---

## 🚫 常见误用 (Common Misuses)

- **误用 1：与通用企业情报报告混淆**
  - *纠正*：通用企业情报报告（如 `org-it-intel-report`）侧重于泛化的组织架构与 IT 招投标公开信息搜集；本模型侧重于 **华为 MCR 销售攻坚体系**，必须包含 UB/SP/TB/EB 决策链权力地图与 $APPEALS 八维度竞争对标。
- **误用 2：以为 EB 决策者打通就可以忽视 TB 把关者与 SP 建议者**
  - *纠正*：在 B2B 大单攻坚中，TB（采购/合规）具备一票否决权，SP（技术架构师）决定技术规范；忽视 TB 会导致合同卡在法务合规，忽视 SP 会导致技术标失分。四角色必须全面覆盖。
- **误用 3：将信息缺失处自行捏造填补**
  - *纠正*：无法通过搜索或用户输入确认的信息（如内部暗流、未公开政治关系），必须明确标注`[需补充]`，严禁虚构。

---

## ⚠️ 边界条件 (Boundary Conditions)

- **不做实时数据接口调用**：本 Skill 不直接对接真实 CRM 系统或付费数据 API，依赖公开搜索或用户提供。
- **不做泛化的公司战略规划**：本 Skill 围绕“针对具体客户进行攻坚分析”这一单一场景，不替代针对自身的 BLM 或五看三定战略规划。

---

## 🔗 相关模型 (Related Models)

- **与[org-it-intel-report](../org-it-intel-report/SKILL.md)**：`org-it-intel-report` 用于快速抓取企业的公开 IT 架构与招投标情报；本模型用于针对重点客户进行深入的 MCR 决策链、竞争雷达与 $APPEALS 攻坚分析。
- **与[swot](../../strategy-competition/swot/SKILL.md)**：SWOT 用于分析整体优劣势；本模型将其收敛应用于竞争格局分析环节。
- **与[porters-five-forces](../../strategy-competition/porters-five-forces/SKILL.md)**：波特五力用于行业结构分析；本模型在业务全景研究中用于评估客户价值链压力。
- **与[vrio](../../strategy-competition/vrio/SKILL.md)**：VRIO 用于评估不可替代性；本模型在客户价值识别中用于评估合作粘性与替换壁垒。
