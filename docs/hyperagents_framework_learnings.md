# Hyperagents Framework Learnings (From Implementation + Reading)

This note captures practical lessons from building and operating the Hyperagent-style scaffold in `prototypes/hyperagent_lab`.

## 1) Why this matters

We implemented a local-first `hyperagent_lab` that preserves the **control flow shape** of Hyperagents while intentionally avoiding broad production assumptions.

Observed value:
- deterministic, testable loop behavior with no mandatory external network
- explicit replay and checkpoint handling for reproducibility
- safe defaults for local experimentation before plugging real model backends

---

## 2) What we learned by reading the reference design

### A. Baseline loop expectations are specific

The reference flow is less “randomly mutate forever” and more a **two-stage paper-like protocol**:
- choose parent
- propose meta edits
- propose task edits (or mutate config)
- run staged eval first, then full eval as needed
- keep lineage and validity semantics tight

A near-match is possible even when implementation is scaffolded, but explicit knobs (`baseline`, `checkpoint`, `resume`) are necessary.

### B. Official-like parity needs argument compatibility

In practice, users expect both old + new CLI shapes. A compatibility-safe pattern:
- keep legacy args (`--generations`) for continuity
- add canonical paper args (`--max_generation`, `--eval_samples`, `--eval_workers`, `--run_baseline`, `--resume_from`, `--baseline_checkpoint`, `--replay_workspace`, `--skip_staged_eval`)

This dramatically improves usability and lowers friction when switching from prototype to reference-style behavior.

### C. Reproducibility is a first-class feature

Hyperagents-style workflows break quickly if replay semantics are fuzzy. Deterministic checkpointing + copy-on-replay workspace is essential:
- checkpoint validation (`checkpoint exists`)
- replay start from checkpoint row
- optionally write output to isolated workspace
- preserve original workspace lineage

---

## 3) What we learned by running it in this repository

### A. The loop truly self-adjusts — but in a constrained way

With the sample benchmark, behavior changed across generations in:
- `meta.strategy` (e.g., moved toward `target_hard_cases`)
- `meta.error_tolerance` (numeric tuning)
- occasional `task.behavior` changes

So “improvement” here means **controller/config adaptation**, not model retraining.

### B. Toy tasks saturate quickly

On small datasets, raw task score can plateau while meta score still moves. That is expected:
- no external uncertainty in the solver
- deterministic local transforms
- limited problem diversity

Don’t overinterpret short runs as convergence failure; treat as bounded utility from fixed-task scaffolds.

### C. Patch safety is critical

Applying diffs as text has edge cases; robust behavior needs:
- staged write into workspace
- compile/gate checks pre- and post-apply
- rollback on failure
- clear lineage logging of `valid_parent`

---

## 4) What this scaffold is (and is not)

### Is:
- local-first optimization loop
- config-space self-improvement engine
- safe compatibility layer (`TaskAgent.forward`, `MetaAgent.forward`, CLI shapes)
- evidence-rich artifact system (`archive.jsonl`, `model.patch.diff`, per-gen outputs)

### Is not (yet):
- a complete Hyperagents production clone
- a universal file-mutating OS agent
- a replacement for explicit deployment/migration tooling

---

## 5) Operational recommendations

1. Start with `standard`/`no_selfimprove` on a dry workspace.
2. Verify patch validity + rollback path on every run.
3. Use `--baseline_checkpoint` + `--replay_workspace` before any risky extension.
4. Only then enable external backends (`orchestrator` / LLM)
5. Keep a strong eval signal: staged/full split, and clear “best gen” metric definitions.

---

## 6) Suggested next doc hooks

- add a `paper_mode_compat.md` matrix mapping each CLI flag against reference behavior
- add one migration-domain task set and evaluator for “realistic refactor tasks”
- log benchmark protocol in a dedicated results notebook under `research/`

---

## 7) Where to find the artifacts

- `prototypes/hyperagent_lab/engine.py`
- `prototypes/hyperagent_lab/hyperagents_bridge.py`
- `prototypes/hyperagent_lab/run_meta_agent.py`
- `tests/test_hyperagent_lab_paper_mode.py`
- `output/hyperagent_paper_mode_v2/` (verification artifacts and checks)

## 8) Core paper reference

Primary source: **Hyperagents: LLMs can improve themselves by improving training data** (2026)
- arXiv: https://arxiv.org/abs/2603.19461
- PDF: https://arxiv.org/pdf/2603.19461.pdf

