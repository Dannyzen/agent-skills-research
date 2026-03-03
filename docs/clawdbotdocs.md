# ClawdBot Services Documentation

This document outlines the internal services available to the ClawdBot agent within the Vagrant sandbox. All services are bridged securely from the host machine to the sandbox via an `autossh` tunnel, making them accessible directly on `127.0.0.1` (localhost).

## 1. Large Language Models (LLMs) & Inference Engines
The models expose OpenAI-compatible API endpoints. You can communicate with them using standard HTTP REST requests or OpenAI client SDKs by overriding the base URL.

### Primary Strategist (vLLM-GPU)
*   **Model:** `DeepSeek-R1-Distill-Llama-70B` (4-bit)
*   **Endpoint:** `http://127.0.0.1:8000/v1`
*   **Purpose:** Complex reasoning, primary strategy, and heavy-lifting tasks.

### Unified Swarm Batcher (vLLM-CPU)
*   **Model:** `Llama-3.1-8B-Instruct`
*   **Endpoint:** `http://127.0.0.1:8081/v1`
*   **Purpose:** Handling concurrent agents and general-purpose instructions efficiently.

### Specialist: Architect (RamaLlama)
*   **Model:** `Qwen-2.5-Coder-32B-Instruct`
*   **Endpoint:** `http://127.0.0.1:8080/v1`
*   **Purpose:** Advanced code generation, software architecture design, and programming tasks.

### Specialist: Vision (RamaLlama)
*   **Model:** `Llama-3.2-11B-Vision`
*   **Endpoint:** `http://127.0.0.1:8082/v1`
*   **Purpose:** Image analysis, OCR, and multi-modal tasks.

## 2. Memory & Message Coordination

### Qdrant (Semantic Vector Database)
*   **Endpoint:** `http://127.0.0.1:6333`
*   **Protocol:** REST API / gRPC
*   **Purpose:** High-performance storage and retrieval of vector embeddings for long-term agent memory.
*   **Communication:** Use the Qdrant REST API (e.g., `GET /collections`, `PUT /collections/{name}/points`) or official client libraries (Python, Node.js, etc.).

### Redis (Message Bus)
*   **Endpoint:** `127.0.0.1:6379`
*   **Protocol:** RESP (Redis Serialization Protocol)
*   **Purpose:** Zero-latency coordination between swarm agents, Pub/Sub messaging, and short-term state storage.
*   **Communication:** Connect using standard Redis clients like `redis-cli`, `redis-py`, or equivalent libraries.

## 3. Observability & Interfaces

### Netdata (Hardware & System Monitoring)
*   **Endpoint:** `http://127.0.0.1:19999`
*   **Protocol:** REST API
*   **Purpose:** Real-time hardware monitoring (CPU, RAM, GPU VRAM, Network) of the host system.
*   **Communication:** Query the Netdata REST API (`/api/v1/data`) to dynamically evaluate hardware stress and adapt agent behavior. 
    *   *Example:* `GET http://127.0.0.1:19999/api/v1/data?chart=system.cpu`

### Dozzle (Container Logs)
*   **Endpoint:** `http://127.0.0.1:8888`
*   **Protocol:** HTTP/WebSocket
*   **Purpose:** Real-time viewing of Docker container logs for infrastructure troubleshooting.

### Open WebUI (Human-Agent Interface)
*   **Endpoint:** `http://127.0.0.1:3000`
*   **Protocol:** HTTP
*   **Purpose:** Primary web interface for humans to interact with the swarm.
