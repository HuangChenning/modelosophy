# long-tail — 盲测结果

- 日期：2026-08-16
- 用例：10 条
- 结果：**10/10 PASS**
- quick_validate.py：通过

## 分型摘要

| 类型 | 结果 |
|------|------|
| should_trigger ×3 | PASS：成本门槛/发现/聚合路径齐全 |
| should_not_trigger ×3 | PASS：二八、幸存者、飞轮诱饵未误触发 |
| correctness_trap ×2 | PASS：纠正“叛逆二八”与“上架即卖”神话 |
| edge_case ×2 | PASS：高履约与无发现机制边界成立 |
