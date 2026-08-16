# test-results.md — first-principles 阶段4压力测试结果

盲测方法论、跨 skill 汇总数据见 `docs/books/wanwu-jie-moxing/test-results.md`（本文件只保留 first-principles 自身的结果）。

## 结果：10/10 通过（100%）

| 类型 | 数量 |
|---|---|
| should_trigger | 3 |
| should_not_trigger | 3 |
| edge_case | 2 |
| correctness_trap | 2 |

首轮盲测 `fp-edge-02` 把本模型当了主技能（用户要挑毛病、结论已写好）。按技能自己的相关模型，主技能应是苏格拉底式质疑。已收紧 description 与"什么时候用"后复测通过：本模型只作辅助检查起点标签。

## 关键验证点

- **审计纠正强制执行**（`fp-trap-01`）："从第一性原理推出来的一定比专家对"被拒绝；起点仍是假设，推出来必须检验。
- **不是材料账**（`fp-trap-02`）：组织问题改用"明天都同意换做法还挡着什么"，不硬找大宗商品价格。
- **重建不等于颠覆**（`fp-edge-01`）：现有结构碰巧是硬约束，算成功应用。
- **挑毛病不抢主技能**（`fp-edge-02`）：主技能走苏格拉底式质疑。
- **兄弟 skill 区分**：`fp-decoy-sibling-01` 交给逆向思维；`fp-decoy-sibling-02` 交给奥卡姆剃刀；日常纪要模板被门禁挡住。
