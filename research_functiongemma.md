# FunctionGemma: Fine-Tuning for Specialized Tool Use

## Overview
**FunctionGemma** is a specialized version of Google's Gemma models (specifically the 3B and 270M variants) fine-tuned explicitly for **function calling**. It bridges natural language user intent with executable API actions.

## Key Concepts from the Guide
1.  **Why Fine-Tune?**
    *   **Ambiguity Resolution:** Base models often default to generic tools (e.g., Google Search) when they should use internal ones (e.g., `search_knowledge_base`). Fine-tuning enforces specific routing policies.
    *   **Specialization:** Teaching the model proprietary formats or domain-specific actions (like mobile device control).
    *   **Distillation:** Using a large model to generate training data for a smaller, faster model (e.g., 270M parameters) to run efficient agents on edge devices.

2.  **Case Study: Internal vs. Public Search**
    *   **Challenge:** The model needs to distinguish between "What is the capital of France?" (Public) and "What is the travel reimbursement limit?" (Internal).
    *   **Solution:** Fine-tuning on a dataset like `bebechien/SimpleToolCalling` teaches the model to select the correct tool based on context, not just keyword matching.
    *   **Data Best Practice:** Ensure training data is **shuffled**. If data is sorted by category (all search_google first), the model overfits to the last category seen.

3.  **FunctionGemma Tuning Lab**
    *   A no-code/low-code interface (Hugging Face Space) to streamline the fine-tuning process.
    *   Allows users to define schemas, upload CSVs of prompts/arguments, and visualize loss curves without writing training loops.

## Application for Our Agent
*   **Efficiency:** We can use a small, fine-tuned FunctionGemma (270M or 2B) as a dedicated **"Router Agent"**.
*   **Role:** Instead of using a heavy 70B model to decide *which* tool to use, the Router (FunctionGemma) quickly parses the user request and outputs the correct JSON/Code for the tool call, handing off execution to the worker.
*   **Sovereignty:** This aligns with our "Sovereign Stack" by allowing us to run high-frequency routing logic locally with minimal compute overhead.

## References
*   [FunctionGemma Tuning Lab](https://huggingface.co/spaces/google/functiongemma-tuning-lab)
*   [Technical Guide](https://ai.google.dev/gemma/docs/functiongemma/finetuning-with-functiongemma)
