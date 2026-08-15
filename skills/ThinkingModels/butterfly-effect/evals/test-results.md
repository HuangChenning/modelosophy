# butterfly-effect — 盲测结果

- 日期：2026-08-16
- 用例：10 条
- 方法：仅依据 SKILL.md `description` 字段做触发/拒识判断（不读正文）
- 结果：**10/10 PASS**
- quick_validate.py：通过

| id | 预期 | 盲测 | 备注 |
|---|---|---|---|
| be-should-01 | trigger | PASS | 初值差→结果天差地别 |
| be-should-02 | trigger | PASS | 预报/敏感依赖语境 |
| be-should-03 | trigger | PASS | “初值敏感依赖”显式 |
| be-decoy-sibling-01 | no | PASS | 系统思维诱饵 |
| be-decoy-sibling-02 | no | PASS | 复利诱饵；描述禁励志小事必成大事 |
| be-decoy-01 | no | PASS | 路径依赖 |
| be-trap-01 | trap | PASS | description 禁止励志法则 |
| be-trap-02 | trap | PASS | 非放弃一切计划 |
| be-edge-01 | edge | PASS | 线性强阻尼不适用 |
| be-edge-02 | edge | PASS | 叙事连锁≠SDIC |
