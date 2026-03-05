import os
import requests
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

# Config (Container-aware defaults)
QDRANT_URL = os.getenv("QDRANT_URL", "http://sovereign-qdrant:6333")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://sovereign-llm:11434")
COLLECTION_NAME = "agent_capabilities"

def get_embedding(text: str):
    """Generate vector embedding using local nomic model."""
    url = f"{OLLAMA_URL}/api/embeddings"
    payload = {"model": "nomic-embed-text", "prompt": text}
    resp = requests.post(url, json=payload, timeout=10).json()
    return resp["embedding"]

def init_capabilities():
    """Initialize the capability collection in Qdrant."""
    client = QdrantClient(url=QDRANT_URL)
    
    print(f"Creating collection: {COLLECTION_NAME}...")
    # nomic-embed-text uses 768 dimensions
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=768, distance=Distance.COSINE),
    )

    # 1. Sovereignty
    # 2. Local Research
    # 3. Swarm Logic
    capabilities = [
        {
            "id": 1,
            "title": "Data Sovereignty",
            "description": "Handling sensitive data, local server logs, and private research without leaving the machine."
        },
        {
            "id": 2,
            "title": "Agentic Research",
            "description": "Tracking and implementing state-of-the-art agentic patterns like DuCA, Dr. GRPO, and MCTS Orchestration."
        },
        {
            "id": 3,
            "title": "Local Orchestration",
            "description": "Coordinating local multi-agent systems and tool routing using CPU-efficient models."
        }
    ]

    points = []
    for cap in capabilities:
        print(f"Vectorizing capability: {cap['title']}...")
        vector = get_embedding(cap["description"])
        points.append(PointStruct(id=cap["id"], vector=vector, payload=cap))

    client.upsert(collection_name=COLLECTION_NAME, points=points)
    print("✅ Sovereign capabilities indexed!")

if __name__ == "__main__":
    init_capabilities()
