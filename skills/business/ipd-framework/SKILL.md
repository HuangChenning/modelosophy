---
name: ipd-framework
description: >
  华为 IPD (Integrated Product Development) 集成产品开发体系。用于指导企业建立以市场为导向、
  将产品开发作为投资管理的研发流程，包含 PDT 跨部门团队、六大阶段（概念/计划/开发/验证/发布/生命周期）及 DCP 商业决策与 TR 技术评审双轨机制。
  触发词：IPD、集成产品开发、PDT团队、DCP评审、TR评审、产品开发流程、阶段门、CHARTER、研发投资管理
metadata:
  author: modelosophy
  version: v1.0
  category: business
  tags:
    - product-development
    - integrated-product-development
    - huawei-ipd
    - r-and-d
---

# 华为 IPD 集成产品开发体系 (ipd-framework)

IPD (Integrated Product Development) 是华为研发管理的核心骨干流程。其根本思想在于**“把产品开发当作一项商业投资来管理”**，打破传统“研发闭门造车”的弊端。通过市场驱动的端到端流程、PDT 跨部门联合团队，以及 DCP (商业决策评审) 与 TR (技术评审) 的双轨关卡管控，降低研发投资风险、缩短上市周期 (TTM)。

---

## ⚡ IPD 架构：六阶段与双轨评审 (Workflow & Gates)

```
阶段：[1. 概念] ──> [2. 计划] ──> [3. 开发] ──> [4. 验证] ──> [5. 发布] ──> [6. 生命周期]
评审：   CDCP           PDCP                                 ADCP
        (概念决策)      (计划决策)                           (上市决策)
技术： TR1/TR2         TR3           TR4/TR5         TR6
```

### 1. 生命周期六大阶段
1. **概念阶段 (Concept)**：深入分析市场与客户需求，完成初步商业可行性评估，拟定 CHARTER（产品开发任务书）。
2. **计划阶段 (Planning)**：制定详细产品定义、总体架构方案、商业计划书与开发进度资源配比（确保“做正确的事”）。
3. **开发阶段 (Development)**：跨部门团队协同进行详细设计、样品制造、原型集成与功能实现。
4. **验证阶段 (Validation)**：开展全面测试（可靠性、环境试验、Beta 客户试用），确保产品质量与技术指标达标。
5. **发布阶段 (Release)**：协调市场推广、销售渠道培训、批量生产备货，实现产品商业上市。
6. **生命周期管理阶段 (Life Cycle Management)**：上市后持续版本维护、成本优化、服务支持，直至最终退市。

---

## 🚦 DCP 商业决策与 TR 技术评审双轨机制

IPD 严格区分“商业投资决策”与“技术质量审查”：

| 评审类型 | 评审全称 | 主责团队 | 核心评估标准 | 决定结果 |
|---------|---------|---------|-------------|---------|
| **DCP 决策评审** | Decision Check Point | **IPMT (投资决策委员会)** | 商业财务 ROI、市场空间、投资风险 | 项目继续 (Go)、终止 (Kill)、重定向 (Redirect) |
| **TR 技术评审** | Technical Review | **ITRAB / 技术专家组** | 架构合理性、技术成熟度、质量与可制造性 | 技术过关允许进入下一开发阶段 |

- **主要 DCP 点**：CDCP（概念决策）、PDCP（计划决策/正式立项投资）、ADCP（可可获得性/上市发布决策）。
- **主要 TR 点**：TR1（需求与架构）、TR2（需求到设计）、TR3（总体设计）、TR4（模块验证）、TR5（系统集成）、TR6（样品测试）。

---

## 👥 PDT 跨部门产品开发团队 (Product Development Team)

打破部门墙，组建以产品成功为目标的强矩阵团队：
- **PDT 经理**：对产品的商业成功（营收、毛利、上市时间）负总责。
- **跨部门代表**：研发代表、市场代表、制造代表、采购代表、服务代表、财务代表。

---

## 🚫 常见误用 (Common Misuses)

- **误用 1：把 IPD 搞成纯研发部门内部的工程技术流程**
  - *纠正*：IPD 的核心是**市场驱动与商业投资**。如果只有研发人员参与，没有市场、采购、制造、财务代表的共同加入，这就退化成了传统的研发技术打磨。
- **误用 2：混淆 DCP 商业评审与 TR 技术评审**
  - *纠正*：DCP 由高层组成的投资委员会 (IPMT) 审查“赚不赚钱/要不要投资”；TR 由技术专家评审“技术成熟度过不过关”。不能用技术评审替代商业决策。
- **误用 3：僵化套用所有 TR 节点导致流程臃肿**
  - *纠正*：IPD 强调“裁切与裁剪规则 (Tailoring)”。对于成熟产品小改型或轻量迭代，应按规范裁剪 TR 节点，避免官僚化。

---

## ⚠️ 边界条件 (Boundary Conditions)

- **不适用于无实体/无软件产品研发的纯服务交付**：IPD 针对的是产品与解决方案开发；纯运维或咨询服务走 ITR/LTC 流程。
- **不替代前瞻性基础科学研究**：前瞻性技术探索（如实验室基础算法研发）走预研流程（0-1 探索），预研成熟后再通过 CHARTER 转入 IPD 正式产品立项。

---

## 🔗 相关模型 (Related Models)

- **与[dste-framework](../dste-framework/SKILL.md)**：DSTE 的 SP 规划决定产品线投资方向；IPD 是承接这些产品线投资落地的研发主业务流。
- **与[ltc-framework](../ltc-framework/SKILL.md)**：IPD 负责把产品研发并上市 (Release)；LTC 负责把发布的产品卖给客户并变现 (Lead to Cash)。
- **与[agile-iteration](../../efficiency-execution/agile-iteration/SKILL.md)**：敏捷迭代侧重于开发阶段 (Development) 内部的小步快跑与 Sprint；IPD 负责端到端产品投资、阶段门与商业成功。
