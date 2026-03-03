# Infrastructure Architecture

## Environment
- **Host:** Virtual Machine (`Vagrant` / `bento/ubuntu-24.04`)
- **Network:** `10.0.2.15` (Guest) ↔ `10.0.2.2` (Host Gateway)

## Service Connectivity
The agent runs inside a VM and accesses external services hosted on the physical machine (Manjaro) via the gateway IP `10.0.2.2`.

| Service | Port | Host Address | Status | Note |
| :--- | :--- | :--- | :--- | :--- |
| **Qdrant** | 6333 | `http://10.0.2.2:6333` | ✅ Active | Knowledge Base |
| **vLLM (GPU)** | 8000 | `http://10.0.2.2:8000` | ❌ Offline | DeepSeek/Llama-70B |
| **vLLM (CPU)** | 8081 | `http://10.0.2.2:8081` | ❌ Offline | Llama-3-8B |
| **RamaLlama** | 8080 | `http://10.0.2.2:8080` | ❌ Offline | Qwen-Coder |
| **Redis** | 6379 | `10.0.2.2:6379` | ❌ Offline | Message Bus |

## Bridge Configuration
The `model-bridge.service` (AutoSSH) is currently **FAILED**.
- **Reason:** SSH connection refused to `danny@10.0.2.2`.
- **Workaround:** Using direct HTTP requests to `10.0.2.2` for exposed services (like Qdrant).
- **Goal:** Fix SSH keys or ensure host services bind to `0.0.0.0` (not just `127.0.0.1`) so the VM can reach them without the tunnel.

## Sovereignty Strategy
To reduce reliance on cloud APIs (Gemini), we must restore connectivity to the local LLMs on the host.
1.  **FunctionGemma (Router)** → Host Port 8081 (CPU/Low VRAM)
2.  **Llama-3-8B (Worker)** → Host Port 8081/8082
3.  **Qdrant (Memory)** → Host Port 6333 (Working)

*Documented for future context.*
