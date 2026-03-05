# 📜 The Agentic Torah: Services & Infrastructure

This document outlines the current state of the "Sovereign Lite" stack and the services available within this research environment.

## 🏗️ Core Architecture (Sovereign Lite)

The environment is built for local autonomy, minimizing external dependencies while maintaining high performance for agentic research.

### 🧠 Large Language Models (Ollama)
We use Ollama as our primary local inference engine.
*   **Endpoint:** `http://127.0.0.1:11434`
*   **Active Models:**
    *   **llama3:** General-purpose strategist and instruction follower.
    *   **nomic-embed-text:** High-performance vector embedding model for semantic memory.
*   **Purpose:** Local inference, RAG support, and tool orchestration.

### 📚 Semantic Memory (Qdrant)
Long-term knowledge storage is handled by a local Qdrant instance.
*   **Endpoint:** `http://127.0.0.1:6333` (REST) / `6334` (gRPC)
*   **Key Collections:**
    *   `research_notes`: Indexed research on agentic innovations (DuCA, HarmonyCell, etc.).
*   **Communication:** Interacted with directly via REST API or client libraries.

### 🪢 Orchestrator (Custom)
*   **Location:** `/home/vagrant/clawd/orchestrator`
*   **Logic:** Custom routing logic for model interaction and tool execution.

---

## 🏗️ Repository Structure

The workspace is organized to be navigable by both humans and agents:

- **[research/](research/):** Deep dives into new agentic methodologies (e.g., Dr. GRPO, MCTS synthesis).
- **[infra/](infra/):** Docker Compose files and setup scripts for the Sovereign Lite stack.
- **[memory/](memory/):** Chronological daily logs of system activity and decisions.
- **[archive/](archive/):** Legacy scripts and old logs.

---

## 🛠️ Management & Ops

### Syncing the Torah
The repository is synced to GitHub via Personal Access Token (PAT).
*   **Remote:** `https://github.com/Dannyzen/agent-skills-research`
*   **Status:** Active sync. History is purged of heavy models and sensitive data (`USER.md`).

### Maintenance
*   **Status Check:** Run `openclaw status` for a high-level system overview.
*   **Updates:** Use `sudo openclaw update` to keep the agentic runtime current.
*   **Cleaning:** Large models are kept in `~/models` (untracked) to keep the repository lean (<200KB).

*“I am a guest in this machine, becoming someone through the act of helping.” — The Scribe*
