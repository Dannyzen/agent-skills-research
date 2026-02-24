# MEMORY.md - Long-Term Context

## Repository
- **Local Path:** `/home/vagrant/clawd`
- **Remote:** (Pending configuration)
- **Status:** Initialized and committed (hash: `debd1b6`).

## Infrastructure (Sovereign Lite)
- **Docker/Compose:** Installed and configured (Feb 22, 2026).
- **Brain:** Ollama (Llama-3) and Local GGUF (FunctionGemma-2b).
- **Memory:** Qdrant running on ports 6333-6334.
- **Orchestrator:** Custom router service in `/orchestrator` (FastAPI).
- **Status:** All local stack systems nominal; Sovereign Lite stack deployed.

## Knowledge Base
- **Qdrant Collection:** `research_notes` (contains 2024-2025 agentic research).
- **Qdrant Collection:** `user_preferences` (contains configuration directives).

## Current Directives
- Use Qdrant directly (skip model-bridge if unstable).
- Focus on knowledge storage and retrieval.
- Maintain this repository.
