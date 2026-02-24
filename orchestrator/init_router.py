import os
import requests
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

# Config
QDRANT_URL = os.getenv("QDRANT_URL", "http://host.docker.internal:6333")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://host.docker.internal:11434")
COLLECTION_NAME = "agent_capabilities"

def get_embedding(text: str):
    url = f"{OLLAMA_URL}/api/embeddings"
    payload = {"model": "nomic-embed-text", "prompt": text}
    resp = requests.post(url, json=payload).json()
    return resp["embedding"]

def init_capabilities():
    client = QdrantClient(url=QDRANT_URL)
    
    # 1. Create Collection (nomic-embed-text uses 768 dimensions)
    print(f"Creating collection: {COLLECTION_NAME}...")
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=768, distance=Distance.COSINE),
    )

    # 2. Define Capabilities
    capabilities = [
        {
            "id": 1,
            "target": "local",
            "description": "Sensitive data, local server logs, private research, privacy-first queries, and anything that shouldn't leave the machine."
        },
        {
            "id": 2,
            "target": "remote",
            "description": "Complex web research, multi-step planning across global tools, high-speed general reasoning, and public information."
        },
        {
            "id": 3,
            "target": "local",
            "description": "Agentic swarm orchestration, testing local multi-agent patterns, and low-latency interaction with local services."
        }
    ]

    # 3. Add points
    points = []
    for cap in capabilities:
        print(f"Embedding capability {cap['id']}...")
        vector = get_embedding(cap["description"])
        points.append(PointStruct(id=cap["id"], vector=vector, payload=cap))

    client.upsert(collection_name=COLLECTION_NAME, points=points)
    print("✅ Capabilities initialized!")

if __name__ == "__main__":
    init_capabilities()
