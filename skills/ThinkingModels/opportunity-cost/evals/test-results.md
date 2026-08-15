# test-results.md — opportunity-cost 阶段4压力测试结果

盲测方法论、跨 skill 汇总数据见 `docs/books/wanwu-jie-moxing/test-results.md`（本文件只保留 opportunity-cost 自身的结果）。

## 结果：10/10 通过（100%）

| 类型 | 数量 |
|---|---|
| should_trigger | 3 |
| should_not_trigger | 4 |
| edge_case | 2 |
| correctness_trap | 1 |

## 关键验证点

- **审计纠正强制执行**（`oc-trap-01`）：原书卡片把机会成本算成"两个选项的差值"，导致"选对了机会成本为负"的错误结论。测试验证 skill 正确纠正为"机会成本恒为正，等于被放弃的最佳替代选项本身的价值；净收益 = 实际选择的价值 − 机会成本"。
- **兄弟 skill 区分**：`oc-decoy-sibling-01` 正确拒绝"已经投入这么多不甘心"场景（属于沉没成本，尚未蒸馏）；`oc-decoy-sibling-02` 正确拒绝"几个原因哪个更可能"场景（属于 occams-razor，选项是解释而非行动）。
- **范围边界**：`oc-decoy-01` 正确拒绝选项尚未成形的探索阶段；`oc-decoy-02` 正确区分"知识查询"与"决策辅助"。
- **边界情况**：`oc-edge-01` 验证反事实对比（"如果当年……"）会触发但必须先排除不现实选项；`oc-edge-02` 验证选项风险不对等时不能直接做价值减法，需先做风险调整。
