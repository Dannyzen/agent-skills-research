# Swarm Consensus & Cross-Candidate Interaction

**Sources:** 
- arxiv:2602.15836 (MAC-AMP)
- New 2026 findings on LLM Judges in Multi-Agent systems.

## The Judge Problem
Research reveals that when multiple agents collaborate, standard "Judge" models often fail because they only see the end product. If the agents collude on a mistake, the judge misses it.

## The Fix: Cross-Candidate Interaction
For a multi-agent system to be truly robust, the judge must witness the **interaction process**:
- It must see the Red Team's critique.
- It must see how the Refiner addressed each specific critique.
- If the Refiner ignored a valid flaw, the Judge must trigger a "Recalculate" loop.

## Metrics
Systems using this "Interactive Oversight" show a **40%+ reduction in logic errors** in complex coding and molecular design tasks compared to linear one-shot generation.
