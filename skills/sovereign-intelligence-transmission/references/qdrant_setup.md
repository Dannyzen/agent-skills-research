# Qdrant Vector Database Setup (Containerized)

To support large-scale semantic research and near-instant memory recall, Qdrant must be deployed as a high-performance vector store on the Manjaro host.

## 1. Configuration
The Qdrant container is configured for maximum performance using the U.2 NVMe storage.

### `docker-compose.yml` Entry
```yaml
  qdrant:
    image: qdrant/qdrant:latest
    container_name: sovereign-qdrant
    ports:
      - "6333:6333"
      - "6334:6334"
    volumes:
      - /home/danny/qdrant_storage:/qdrant/storage:z
    restart: always
```

## 2. High-Performance Settings
- **Storage**: The `/qdrant/storage` volume is mapped directly to the U.2 NVMe array.
- **Indexing**: Configured to use the 8358P's 32 cores for parallel vector indexing.

## 3. Agent Connectivity
The OpenClaw agent (inside the Vagrant VM) connects to Qdrant via the SSH tunnel bridge.
- **Protocol**: REST (Port 6333) or gRPC (Port 6334).
- **Target**: `http://10.0.2.2:6333` (through the 127.0.0.1 mapping).
- **Use Case**: Powers the `memory_search` tool with millions of research paper vectors.
