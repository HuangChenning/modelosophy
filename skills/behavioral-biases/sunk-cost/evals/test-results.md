# test-results.md — sunk-cost 阶段4压力测试结果

盲测方法论、跨 skill 汇总数据见 `docs/books/wanwu-jie-moxing/test-results.md`（本文件只保留 sunk-cost 自身的结果）。

## 结果：10/10 通过（100%）

| 类型 | 数量 |
|---|---|
| should_trigger | 3 |
| should_not_trigger | 3 |
| edge_case | 2 |
| correctness_trap | 2 |

## 关键验证点

- **审计纠正强制执行**（`sc-trap-02`）：原书把子女写成可核销的沉没支出。盲测正确拒绝把人当止损金额，并把已投入与面向未来的义务拆开。
- **反向误用**（`sc-trap-01`）：创业场景同时挡住"已烧的钱必须扛"和"沉没成本 = 教人半途而废"。
- **未来成本不是沉没成本**（`sc-edge-01`）：80 万预付款忽略，20 万解约金必须计入。
- **兄弟 skill 区分**：`sc-decoy-sibling-01` 正确交给机会成本；`sc-decoy-sibling-02` 正确交给反脆弱。
