<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="modelosophy — the project name beside a funnel-and-drop distillation mark">
</p>

modelosophy turns centuries of human thinking frameworks into AI Skills an agent can call.

SWOT, first principles, MECE, compound thinking, second-order thinking — each mental model becomes an independent, composable Skill instead of a paragraph in a wiki. An AI agent uses them the way a person would: to break down a problem, build a strategy, or make a decision.

## What's here now

This repository is early. Two kinds of skills exist so far:

- [`skills/Business/sales-company-intel-report`](skills/Business/sales-company-intel-report) — a sales account-research skill that demonstrates the `SKILL.md` + templates + scripts structure this project uses.
- [`skills/ThinkingModels/`](skills/ThinkingModels) — the mental-model library so far: 31 skills (30 from the book plus Socratic questioning), spanning decision costs, biases, systems, strategy tools (SWOT, MECE, PDCA, flywheel), prospect theory / Fogg / Golden Circle / Johari / Dunning–Kruger, and more. Each was re-researched from its actual academic source (not copied from the 《万物皆模型》book's summary cards), passed a Socratic self-check, blind-tested eval cases, and official Skill spec validation. See [`skills/ThinkingModels/README.md`](skills/ThinkingModels/README.md) for the full map.

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

`<category>` groups skills by domain — for example `Business/` for sales and customer-research skills, `ThinkingModels/` for mental-model skills.

Skills that render an HTML report follow the shared visual spec in [`DESIGN.md`](DESIGN.md).

## Limitations

The mental-model library is still early — 31 models are covered so far (30 from the book plus Socratic questioning as a method supplement). Most of the 100 models haven't been touched at all. Skill-authoring conventions may still change as the library grows.

## Contributing a mental model

Have a thinking framework worth distilling? Open a PR that adds a new `skills/<category>/<name>/SKILL.md` following the structure above.

---

[中文](README.zh-CN.md)
