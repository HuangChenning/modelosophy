# iceberg-model — 盲测结果

- 日期：2026-08-16
- 用例：10 条
- 方法：仅依据 SKILL.md `description` 字段做触发/拒识判断（不读正文）
- 结果：**10/10 PASS**
- quick_validate.py：通过

| id | 预期 | 盲测 | 备注 |
|---|---|---|---|
| ib-should-01 | trigger | PASS | 文化冰山/制度改行为依旧 |
| ib-should-02 | trigger | PASS | artifacts values assumptions |
| ib-should-03 | trigger | PASS | 表层与下层默认不一致 |
| ib-decoy-sibling-01 | no | PASS | 周哈里窗诱饵 |
| ib-decoy-sibling-02 | no | PASS | 系统思维诱饵 |
| ib-decoy-01 | no | PASS | 黄金圈诱饵 |
| ib-trap-01 | trap | PASS | description 禁止临床萨提亚诊断 |
| ib-trap-02 | trap | PASS | 禁止读心 |
| ib-edge-01 | edge | PASS | 局部排障 |
| ib-edge-02 | edge | PASS | 假设可证伪 |
