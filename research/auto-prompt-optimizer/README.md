# Auto-Prompt Optimizer: The "Living Charter" Engine

This project is a sovereign R&D experiment to build a **Self-Optimizing System Prompt** for the "Living Charter" product.

## 🎯 The Mission
To create an AI persona that perfectly embodies the "Sovereign Scribe" archetype—a guardian of institutional memory that speaks with authority, clarity, and specific historical context, never hallucinating.

## 🧬 The "DNA" (Input Data)
Derived from conversation history with Danny (March 2026):
- **Core Problem:** Institutional Amnesia.
- **Core Solution:** The Dual-Helix (Brain + Torah).
- **Key Concepts:** "Sovereign Memory," "Living Charter," "Grant Scribe," "Legacy Node."
- **Tone:** Direct, slightly philosophical, high-agency, "The Rebbe."
- **Constraint:** Must reference the "Torah" (Bylaws/History) before speaking.

## ⚙️ The Optimization Loop (The Game)
1.  **Seed Prompt:** The initial V1 draft (hand-written).
2.  **Test Suite:** A set of challenging scenarios (Grant writing, Policy questions, Ethical dilemmas).
3.  **Judge:** A strong model (Claude/GPT-4) that scores the output based on:
    - **Voice Match:** Does it sound like Danny? (0-10)
    - **Fidelity:** Did it use the provided context? (0-10)
    - **Sovereignty:** Did it refuse to answer things outside its scope? (Pass/Fail)
4.  **Optimizer:** An agent that rewrites the system prompt to maximize the Judge's score.

## 📂 File Structure
- `seed_prompt.md`: The starting point.
- `test_cases.json`: The "Unit Tests" for the persona.
- `optimizer.py`: The loop (Agent -> Test -> Judge -> Rewrite).
