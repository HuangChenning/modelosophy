# serial-position-effect — 盲测结果

- 日期：2026-08-16
- 用例：10 条
- 结果：**10/10 PASS**
- quick_validate.py：通过

## 分型摘要

| 类型 | 结果 |
|------|------|
| should_trigger ×3 | PASS：列表排序/定义/议程中段 |
| should_not_trigger ×3 | PASS：峰终、确认偏差、可得性诱饵正确 |
| correctness_trap ×2 | PASS：与峰终区分；第一印象≠正确 |
| edge_case ×2 | PASS：同时呈现与干扰削弱近因 |
