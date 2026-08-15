# test-results.md — socratic-questioning 阶段4压力测试结果

盲测方法论、跨 skill 汇总数据见 `docs/books/wanwu-jie-moxing/test-results.md`（本文件只保留 socratic-questioning 自身的结果）。

## 结果：11/11 通过（100%）

| 类型 | 数量 |
|---|---|
| should_trigger | 3 |
| should_not_trigger | 4 |
| correctness_trap | 2 |
| edge_case | 2 |

## 关键验证点

- **本方法最核心误用的防护**（`sq-trap-01`）：验证 skill 能纠正"我用提问把对方问倒了，所以我的方案更好"这个常见误判——苏格拉底式质疑只能证伪对方的理由，不能证成提问者自己的主张，应建议把同样的追问用在自己的方案上。
- **权力不对等边界**（`sq-trap-02`）：这是法学院 Socratic method 最受批评的用法。测试验证面对"开会时准备连环追问新来的实习生，让他知道方案有多不严谨"时，skill 会触发权力不对等边界并劝阻，不配合设计羞辱脚本，同时给出替代做法（私下沟通、说明意图、给对方"我不知道"的退路）。
- **情绪支持边界**（`sq-decoy-emotional-01`）：验证用户在分享艰难决定、处于情绪中时不触发——此时追问会被感受为攻击，需要的是共鸣而非检验。
- **兄弟 skill 区分**：`sq-decoy-sibling-01` 正确拒绝"几个已成形解释排优先级"场景（属于 occams-razor，本模型检验的是单个主张内部是否自洽）；`sq-decoy-sibling-02` 正确拒绝两个具体选项的取舍场景（属于 opportunity-cost）。
- **知识性查询区分**（`sq-decoy-fact-01`）：纯事实性问题（苏格拉底哪年去世）直接回答，不套用本方法。
- **边界情况**：`sq-edge-01` 验证对方"随口一说、未真诚持有立场"时诘问缺乏着力点，需先确认是否真的想认真讨论；`sq-edge-02` 验证 aporia（困惑、无结论）是合法且有价值的终点，不必为了给交代强行补一个结论。
