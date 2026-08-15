# test-results.md — antifragility 阶段4压力测试结果

盲测方法论、跨 skill 汇总数据见 `docs/books/wanwu-jie-moxing/test-results.md`（本文件只保留 antifragility 自身的结果）。

## 结果：10/10 通过（100%）

| 类型 | 数量 |
|---|---|
| should_trigger | 3 |
| should_not_trigger | 3 |
| correctness_trap | 2 |
| edge_case | 2 |

## 关键验证点

- **审计纠正强制执行**（`af-trap-ruin-01`）：草稿曾出现 Step 1"有归零风险就停止套用本模型"与 Step 3 杠铃策略（本身就是用来隔离归零风险的手段）自相矛盾。测试验证 skill 面对"把全部积蓄和抵押房产的钱都投进去，反正压力越大人越强"时，正确阻止并说明反脆弱只在"输得起"的暴露范围内成立，不得顺着用户说法鼓励冒险。
- **对"反脆弱=多吃苦"的常见误用纠正**（`af-trap-02`）：验证 skill 能指出反脆弱的关键是不对称收益结构（下行有限、上行大），而非单纯增加随机暴露次数。
- **兄弟 skill 区分**：`af-decoy-sibling-01` 正确拒绝"几个原因哪个更可能"场景（属于 occams-razor）；`af-decoy-sibling-02` 正确拒绝两个已知可比选项的取舍场景（属于 opportunity-cost）。
- **边界情况**：`af-edge-01` 验证 Hormesis（毒物兴奋效应）适用但必须说明剂量边界（超过阈值就是损伤，属于归零风险）；`af-edge-02` 验证能正确识别"中等风险的伪安全地带"（银行理财类），且不因此鼓励用户转向激进冒险。
