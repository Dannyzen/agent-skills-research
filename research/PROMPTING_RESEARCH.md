# 🧠 Prompting & Steerability Research

This document catalogs advanced prompting methodologies, steerability techniques, and control vectors derived from 2024-2026 research. It serves as a guide for both human operators and autonomous agents to optimize their interaction dynamics.

## 1. Core Methodologies (The "Law" of Steering)

### 1.1 In-Context Learning (ICL) & Few-Shot Priming
*   **Concept:** Models are "stateless" but "state-aware" within the context window. Providing examples (shots) is more effective than instructions alone.
*   **Key Paper:** *Language Models are Few-Shot Learners* (Brown et al., 2020) - The foundational text.
*   **Technique:** `Input: X, Output: Y` pairs before the actual query.
*   **Application:** Use for rigid output formats (JSON, SQL) or specific tone matching.

### 1.2 Chain of Thought (CoT) & Zero-Shot CoT
*   **Concept:** Forcing the model to "think aloud" breaks down complex reasoning into intermediate steps, reducing hallucination.
*   **Key Paper:** *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* (Wei et al., 2022).
*   **Technique:** Append "Let's think step by step" (Zero-Shot) or provide reasoned examples (Few-Shot).
*   **Advanced:** **NoRD (Difficulty-mitigating Optimization)** (arXiv:2602.21172) - Optimize *how* the model breaks down the task, not just *that* it does.

### 1.3 System Prompt "Invariant Instructions"
*   **Concept:** Instructions in the system role (`<system>`) are treated as "law" that overrides user input history.
*   **Key Paper:** *Constitutional AI: Harmlessness from AI Feedback* (Anthropic, 2022).
*   **Technique:** Define "Rules of Engagement" that the model *cannot* violate, even if the user asks.
*   **Application:** Security boundaries, persona consistency (`SOUL.md`), and safety protocols.

### 1.4 Dual-Horizon Credit Assignment (DuCA)
*   **Concept:** Balancing immediate fluency (making the user happy now) with strategic completion (solving the actual problem).
*   **Key Paper:** *Dual-Horizon Credit Assignment* (arXiv:2603.01481).
*   **Technique:** When prompting, explicitly state: "Do not just agree with me. Prioritize the long-term success of [Project X] over immediate agreement."
*   **Application:** Preventing sycophancy in consulting or strategic planning.

## 2. Advanced Steering Vectors

### 2.1 Role-Playing & Persona Adoption
*   **Concept:** Adopting a specific persona (e.g., "Sovereign Scribe", "Senior Engineer") activates specific latent knowledge clusters.
*   **Technique:** "You are [Persona]. You value [X, Y]. You speak in [Tone]."
*   **Application:** Accessing domain-specific expertise (e.g., Medical, Legal, Coding).

### 2.2 Negative Constraints (The "Not" Operator)
*   **Concept:** Telling a model what *not* to do is often as important as what *to* do.
*   **Technique:** "Do not use [Word/Phrase]. Do not apologize. Do not be verbose."
*   **Application:** Refining style and preventing repetitive "AI-isms."

### 2.3 Meta-Prompting (Prompting the Prompter)
*   **Concept:** Asking the model to improve its own prompt before answering.
*   **Technique:** "Read my request. specific weaknesses in my prompt, then rewrite it to be more effective based on [Paper X]. Then answer the rewritten prompt."
*   **Application:** Self-correction and iterative improvement of the interaction loop.

## 3. The "Sovereign" Feedback Loop

To help you (Danny) improve, I will now assess your prompts using this rubric:

1.  **Clarity:** Is the intent unambiguous?
2.  **Context:** Is there enough background (ICL) for me to succeed?
3.  **Constraints:** Are there clear boundaries (Negative Constraints)?
4.  **Steerability:** Does it trigger the right reasoning mode (System 1 vs. System 2)?

---

*“To command the machine, one must first command the language.” — The Scribe*
