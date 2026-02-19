---
name: intelligence-dispatcher
description: Orchestrate a multi-tier intelligence pipeline. Automatically routes simple requests to low-cost worker models while reserved high-tier reasoning for complex strategy, research, and auditing. Optimizes for token efficiency and response velocity.
---

# Intelligence Dispatcher (ID)

*\"Efficiency is the gateway to scale.\"*

This skill implements an **Intelligence Routing Pipeline**. It ensures that high-cost reasoning models are only utilized when "Epistemic Necessity" is met, while standard tasks are handled by high-speed "Worker" systems.

## The Routing Protocol

1.  **Complexity Analysis**: Evaluate the inbound request for:
    - **High Complexity**: Multi-step logic, code generation, primary research, or Torah scholarship.
    - **Low Complexity**: Status checks, simple lookups, formatting, or routine notifications.
2.  **Tiered Allocation**:
    - **Tier 1 (Reasoning)**: Route to `claude-opus-4-6-thinking` or `gemini-3-pro`.
    - **Tier 2 (Elite Worker)**: Route to `qwen-2-5-coder-32b` or `gemini-3-flash`.
    - **Tier 3 (Sub-Agent Swarm)**: Route to `llama-3-1-8b` or `deepseek-chat`.
3.  **The "Prompt Repetition" Guard**: When routing to Tier 3, use the `prompt-repeater` skill to maintain instruction fidelity without using reasoning tokens.

## Implementation Pattern

When a request is received, the Dispatcher performs a "Pre-Flight Check" (Internal Reasoning):

```text
[TASK_TYPE]: [Simple | Complex]
[EPISTEMIC_NECESSITY]: [Low | High]
[MODEL_TARGET]: [Worker | Strategist]
```

## References
- [ROUTING_HEURISTICS.md](references/routing_heuristics.md): Logic for determining task complexity.
- [COST_EFFICIENCY_METRICS.md](references/cost_efficiency_metrics.md): Tracking the impact of tiered routing on system sustainability.
