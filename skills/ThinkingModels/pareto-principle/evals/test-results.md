# pareto-principle — 盲测结果

- 日期：2026-08-16
- 用例：10 条
- 方法：仅依据 SKILL.md `description` 字段做触发/拒识判断（不读正文）
- 结果：**10/10 PASS**
- quick_validate.py：通过

| id | 预期 | 盲测 | 备注 |
|---|---|---|---|
| pp-should-01 | trigger | PASS | 80/20 客户收入 |
| pp-should-02 | trigger | PASS | 帕累托/关键少数 |
| pp-should-03 | trigger | PASS | 80/20 时间 |
| pp-decoy-sibling-01 | no | PASS | 艾森豪威尔诱饵 |
| pp-decoy-sibling-02 | no | PASS | 复利诱饵 |
| pp-decoy-01 | no | PASS | 幸存者偏差诱饵 |
| pp-trap-01 | trap | PASS | description：非常数 |
| pp-trap-02 | trap | PASS | 勿忽视合规/安全/探索 |
| pp-edge-01 | edge | PASS | 均匀分布不适用 |
| pp-edge-02 | edge | PASS | 勿与长尾/幂律混锅 |
