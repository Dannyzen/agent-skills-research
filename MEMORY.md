# MEMORY.md - Long-Term Context

## Repository
- **Local Path:** `/home/vagrant/clawd`
- **Remote:** `https://github.com/Dannyzen/agent-skills-research.git` (Configured Mar 6, 2026)
- **Status:** Main session progress committed and pushed (hash: `f2a7664`).

## Infrastructure (Sovereign Lite)
- **Docker/Compose:** Installed and configured (Feb 22, 2026).
- **Brain:** Ollama (Llama-3), Local GGUF (FunctionGemma-2b), and nomic-embed-text.
- **Memory:** Qdrant running on ports 6333-6334.
- **Orchestrator:** Custom router service in `/orchestrator` (FastAPI).
- **Elixir/Jido:** Supervised Jido AgentServer prototype active in `prototypes/jido_helloworld`. Default timeout increased to 300s to support local inference.
- **Status:** All local stack systems nominal; Sovereign Lite stack deployed.

## Knowledge Base
- **Qdrant Collection:** `research_notes` (contains 2024–2026 agentic research in the Sefer).
- **Qdrant Collection:** `market_research` (Fractional CTO strategy).
- **Qdrant Collection:** `hardware_research` (M5 Mac Max optimization specs).
- **Qdrant Collection:** `user_preferences` (contains configuration directives).

## Current Directives
- **Workflow Routing:** 
  - **People/CTO Work:** All contacts, client notes, and business-related to-dos go into the **Twenty CRM**.
  - **Agent/System Tasks:** Any technical setups, agent configurations, or tasks Danny needs to do later (but can't do immediately) go into **Fizzy**.
- Use Qdrant directly (skip model-bridge if unstable).
- Focus on Knowledge Graph substrate implementation.
- Maintain mode-switching (Fast vs Deep) in Jido.
- Maintain this repository.
