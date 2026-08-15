<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="modelosophy — the project name beside a funnel-and-drop distillation mark">
</p>

modelosophy turns centuries of human thinking frameworks into AI Skills an agent can call.

SWOT, first principles, MECE, compound thinking, second-order thinking — each mental model becomes an independent, composable Skill instead of a paragraph in a wiki. An AI agent uses them the way a person would: to break down a problem, build a strategy, or make a decision.

## What's here now

This repository is early. Skills are grouped by domain under `skills/<category>/`:

- [`skills/business/org-it-intel-report`](skills/business/org-it-intel-report) — a vendor-neutral org / IT intelligence skill (organization overview + IT investment & procurement), demonstrating the `SKILL.md` + templates + scripts structure this project uses.
- [`skills/thinking-models/`](skills/thinking-models) — **50** executable mental-model skills (general reasoning, strategy, learning, leadership, etc.). Another **19** formerly here were moved into the domain categories below. See [`skills/thinking-models/README.md`](skills/thinking-models/README.md).
- Six domain categories **peer to** `business/` / `thinking-models/` (executable skills, not knowledge-card shells):
  - [`econ-macro-theories`](skills/econ-macro-theories) — macro theories (seeds TBD)
  - [`econ-micro-markets`](skills/econ-micro-markets) — micro / markets (e.g. opportunity cost)
  - [`game-theory-models`](skills/game-theory-models) — game theory
  - [`behavioral-biases`](skills/behavioral-biases) — behavioral economics & biases (9 skills)
  - [`finance-investing-models`](skills/finance-investing-models) — finance / investing (e.g. compounding)
  - [`systems-classic-effects`](skills/systems-classic-effects) — systems & classic effects (7 skills)

Useful fields from an earlier “9-field card” draft (author, misuse, memory hook, …) may be absorbed into executable `SKILL.md` sections; cards are **not** the primary deliverable. Plan: [`ROADMAP.md`](ROADMAP.md).

## How it works

<p align="center">
  <img src="./assets/readme/mechanism.svg" width="100%" alt="Three-stage diagram: model, distill, reuse">
</p>

A mental model is first **named as a pattern** (model), then **reduced to its operating steps** (distill) as a `SKILL.md`, then **called by any agent** that reads the skills directory (reuse).

## Usage

Each skill lives in its own directory under `skills/<category>/<name>/` with a `SKILL.md` that an agent (such as Claude Code) reads to learn what the skill does and how to invoke it.

```bash
git clone https://github.com/HuangChenning/modelosophy.git
# or copy a single skill into your own project
cp -r modelosophy/skills/<category>/<name> your-project/skills/<name>
```

Skills that generate reports write them to `output/<skill-name>/`; that directory is local-only and is not tracked in this repository.

## Repository layout

```text
skills/<category>/<name>/SKILL.md      what the skill does, when to use it
skills/<category>/<name>/references/   supporting methodology and reference material
skills/<category>/<name>/scripts/      generation or automation scripts, if any
skills/<category>/<name>/assets/       templates the skill renders into
```

`<category>` groups skills by domain — for example `business/`, `thinking-models/`, and the six econ / bias / systems categories above.

Skills that render an HTML report follow the shared visual spec in [`DESIGN.md`](DESIGN.md).

## Limitations

The library is still early — about **69** executable models exist across categories (50 in `thinking-models/` + 19 migrated). Remaining book / economics checklist items will be added as executable skills in batches. Conventions may still change as the library grows.

## Contributing a mental model

Have a thinking framework worth distilling? Open a PR that adds a new `skills/<category>/<name>/SKILL.md` following the structure above.

---

[中文](README.zh-CN.md)
