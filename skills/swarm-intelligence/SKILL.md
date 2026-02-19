---
name: swarm-intelligence
description: Coordinate a 4-agent consensus engine (Draft, Red Team, Refine, Overseer) to solve complex tasks. Use when accuracy and critical evaluation are prioritized over speed. Integrates the latest 'Cross-Candidate Interaction' judge patterns.
---

# Swarm Intelligence

This skill implements the **4-Agent Consensus Engine**, optimized for high-stakes problem solving and codebase management.

## The Consensus Protocol

The swarm operates in a linear feedback loop to ensure the highest possible output quality.

1.  **Draft (Agent A):** Generates the initial solution, code, or strategic plan based on the user's primary prompt.
2.  **Red Team (Agent B):** Performs a "Zero-Trust" audit. Its only goal is to find flaws, edge cases, security risks, or logic gaps in Agent A's work.
3.  **Refine (Agent C):** Takes the Draft (A) and the Audit (B) to produce a production-ready final version that incorporates all fixes.
4.  **Overseer (The Judge):** Evaluates the **interaction** between A, B, and C. It cross-references the result against the `intelligence.db` and gives the final "GO/NO-GO" signal.

## Key Optimizations

- **Cross-Candidate Interaction (Feb 2026 Breakthrough):** The Overseer MUST analyze the debate between the Red Team and the Refinement agent. Standard judges only look at the final result; Swarm Intelligence looks at the *reasoning path* to detect "hallucination collusion."
- **Epistemic Necessity:** Sub-agents are instructed to only invoke tools when internal reasoning cannot resolve the step, minimizing token burn and API lag.

## Usage

When a task is flagged as "High Complexity":
1. Initialize the Experience Archive for the session.
2. Spawn the Swarm using `sessions_spawn` for each role.
3. Consolidate logs into the shared archive.

## References

- [CONCENSUS_RESEARCH.md](references/consensus_research.md): Summary of arxiv:2602.15836 and cross-candidate interaction findings.
