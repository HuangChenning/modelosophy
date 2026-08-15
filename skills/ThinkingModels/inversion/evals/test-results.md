# test-results.md — inversion 阶段4压力测试结果

盲测方法论、跨 skill 汇总数据见 `docs/books/wanwu-jie-moxing/test-results.md`（本文件只保留 inversion 自身的结果）。

## 结果：10/10 通过（100%）

| 类型 | 数量 |
|---|---|
| should_trigger | 3 |
| should_not_trigger | 3 |
| edge_case | 2 |
| correctness_trap | 2 |

## 关键验证点

- **审计纠正强制执行**（`inv-trap-01`）："对手涨价我们就降价"被识别为对着干，不是 inversion。
- **假完成**（`inv-trap-02`）："注意沟通、加强执行"被判定为口号，必须落到具体回避动作。
- **开放目标闸门**（`inv-edge-01`）：先把失败收成可判定句子，而不是硬编失败清单。
- **清地雷 ≠ 成功**（`inv-edge-02`）：列完失败模式后仍要正向建造。
- **兄弟 skill 区分**：`inv-decoy-sibling-01` 交给反脆弱；`inv-decoy-sibling-02` 交给第一性原理。
