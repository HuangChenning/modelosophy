# implicit-premises — 盲测结果

- 日期：2026-08-16
- 用例：10 条
- 方法：仅依据 SKILL.md `description` 字段做触发/拒识判断（不读正文）
- 结果：**10/10 PASS**
- quick_validate.py：通过

| id | 预期 | 盲测 | 备注 |
|---|---|---|---|
| ip-should-01 | trigger | PASS | “隐含前提”显式命中 |
| ip-should-02 | trigger | PASS | “默认了什么”命中 |
| ip-should-03 | trigger | PASS | “省略的前提”命中 |
| ip-decoy-sibling-01 | no | PASS | 苏格拉底式整体挑毛病 → 兄弟 |
| ip-decoy-sibling-02 | no | PASS | 确认偏差诱饵 |
| ip-decoy-01 | no | PASS | 第一性原理诱饵 |
| ip-trap-01 | trap | PASS | description 排除潜意识诊断 |
| ip-trap-02 | trap | PASS | 闭合≠正确（正文支撑；描述已强调可接受性） |
| ip-edge-01 | edge | PASS | 无论证则不适用 |
| ip-edge-02 | edge | PASS | 多前提并列 |
