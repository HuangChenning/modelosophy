# test-results.md — confirmation-bias 阶段4压力测试结果

盲测方法论、跨 skill 汇总数据见 `docs/books/wanwu-jie-moxing/test-results.md`（本文件只保留 confirmation-bias 自身的结果）。

## 结果：10/10 通过（100%）

| 类型 | 数量 |
|---|---|
| should_trigger | 3 |
| should_not_trigger | 3 |
| edge_case | 2 |
| correctness_trap | 2 |

## 关键验证点

- **审计纠正强制执行**（`cb-trap-01`）：原书"取中间值"被明确拒绝——真和假的中点仍然不是真。
- **过度纠正**（`cb-trap-02`）：禁止把纠偏做成"只收集反对意见"；正例检验不总是非理性。
- **需要支持时停用**（`cb-edge-01`）：用户明确只要鼓励，正确拒绝套用。
- **预注册闸门**（`cb-edge-02`）：写不出改主意条件时停在 step 2，不空转找证据。
- **兄弟 skill 区分**：`cb-decoy-sibling-01` 交给奥卡姆剃刀；`cb-decoy-sibling-02` 交给苏格拉底式质疑。
