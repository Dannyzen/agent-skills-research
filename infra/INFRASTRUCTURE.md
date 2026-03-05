# Sovereign Lite: Infrastructure Architecture

## Environment
- **Host Platform:** Virtual Machine (`Vagrant` / `bento/ubuntu-24.04`)
- **Container Engine:** Docker Engine 24.x
- **Network Strategy:** Local Loopback (`127.0.0.1`) for high-security, low-latency agentic communication.

## Core Services (Sovereign Lite Stack)
All services are containerized within the VM to ensure complete data sovereignty and independence from host machine networking.

| Service | Container Name | Port | Status | Role |
| :--- | :--- | :--- | :--- | :--- |
| **Ollama** | `sovereign-llm` | 11434 | ✅ Active | Local LLM Inference Engine |
| **Qdrant** | `sovereign-qdrant` | 6333 | ✅ Active | Long-term Semantic Vector Memory |
| **Orchestrator** | `sovereign-orchestrator` | N/A | ✅ Active | Custom tool routing & model coordination |

## LLM Strategy
We prioritize local-first inference to minimize cloud VRAM dependency and maximize privacy.
1. **Model:** `llama3:latest` (8B) for general strategy and tool use.
2. **Embedding:** `nomic-embed-text:latest` for vectorizing research and memory.

## Deployment & Ops
- **Startup:** Managed via `infra/start_sovereign_lite.sh`.
- **Composition:** Split between `infra-compose.yml` (base storage) and `sovereign-lite-compose.yml` (inference services).
- **Maintenance:** Local git repository (shrunk to <200KB) is synced via GitHub PAT to `Dannyzen/agent-skills-research`.

*“Text > Brain” — Documenting the foundation of the Agentic Torah.*
