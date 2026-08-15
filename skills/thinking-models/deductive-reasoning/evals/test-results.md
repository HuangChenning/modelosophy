# deductive-reasoning — 盲测结果

- 日期：2026-08-16
- 用例：10 条
- 方法：仅依据 SKILL.md `description` 字段做触发/拒识判断（不读正文）
- 结果：**10/10 PASS**
- quick_validate.py：通过

| id | 预期 | 盲测 | 备注 |
|---|---|---|---|
| dr-should-01 | trigger | PASS | 三段论/必然推出 |
| dr-should-02 | trigger | PASS | 大前提小前提 + 有效/可靠 |
| dr-should-03 | trigger | PASS | 从条款演绎 |
| dr-decoy-sibling-01 | no | PASS | 第一性原理诱饵 |
| dr-decoy-sibling-02 | no | PASS | 苏格拉底诱饵 |
| dr-decoy-01 | no | PASS | 隐含前提诱饵（缺腿前提） |
| dr-trap-01 | trap | PASS | description 排除侦探式归纳/猜真相 |
| dr-trap-02 | trap | PASS | 有效≠可靠 |
| dr-edge-01 | edge | PASS | 归纳≠演绎 |
| dr-edge-02 | edge | PASS | 规范前提另辩 |
