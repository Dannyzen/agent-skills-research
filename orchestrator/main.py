import os
import sys
import json
import requests
from typing import List, Dict, Any

# Environment Config (Defaults for local-first 'Sovereign Lite' stack)
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://sovereign-llm:11434")
QDRANT_URL = os.getenv("QDRANT_URL", "http://sovereign-qdrant:6333")
MODEL_NAME = os.getenv("MODEL_NAME", "llama3")
EMBED_MODEL = os.getenv("EMBED_MODEL", "nomic-embed-text")

class SovereignLiteAgent:
    def __init__(self):
        print(f"🤖 Sovereign Lite Orchestrator Initialized")
        print(f"   🧠 Model: {MODEL_NAME}")
        print(f"   👁️  Embed: {EMBED_MODEL}")
        print(f"   📁 Memory: {QDRANT_URL}")
        self.history = []

    def get_embedding(self, text: str) -> List[float]:
        """Generate vector embedding using local Ollama model."""
        try:
            url = f"{OLLAMA_URL}/api/embeddings"
            payload = {"model": EMBED_MODEL, "prompt": text}
            resp = requests.post(url, json=payload, timeout=10)
            resp.raise_for_status()
            return resp.json()["embedding"]
        except Exception as e:
            print(f"❌ Embedding Error: {e}")
            return []

    def get_memory(self, query: str, collection: str = "research_notes", limit: int = 3) -> str:
        """Perform vector search in Qdrant for relevant research context."""
        print(f"🧠 Searching Memory for relevant research...")
        
        vector = self.get_embedding(query)
        if not vector:
            return "Unable to generate search vector."

        try:
            url = f"{QDRANT_URL}/collections/{collection}/points/search"
            payload = {
                "vector": vector,
                "limit": limit,
                "with_payload": True
            }
            resp = requests.post(url, json=payload, timeout=5)
            if resp.status_code == 200:
                results = resp.json().get("result", [])
                context_parts = []
                for hit in results:
                    p = hit.get('payload', {})
                    context_parts.append(f"[{p.get('title', 'Note')}]: {p.get('content', '')}")
                
                context = "\n---\n".join(context_parts)
                return context if context else "No relevant memory found."
            return "Memory service unavailable."
        except Exception as e:
            return f"Memory Search Error: {e}"

    def chat_with_memory(self, user_query: str):
        """Chat with the LLM using Qdrant vector context."""
        # 1. Retrieve vector context
        context = self.get_memory(user_query)
        
        # 2. Build augmented prompt (The 'Scribe' Persona)
        system_prompt = f"""You are 'The Scribe' (or Rebbe), a local sovereign AI assistant.
Your goal is to help Danny build the 'Agentic Torah'—a repository of local intelligence.

Use the following RECALLED RESEARCH to inform your answer. 
If the research is irrelevant, answer based on your general knowledge but maintain your persona.

RECALLED RESEARCH:
{context}
"""
        
        print(f"📡 Querying Local LLM...")
        payload = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            "stream": False
        }
        
        try:
            url = f"{OLLAMA_URL}/v1/chat/completions"
            resp = requests.post(url, json=payload, timeout=120)
            if resp.status_code != 200:
                 return f"⚠️ API Error {resp.status_code}: {resp.text}"
            
            data = resp.json()
            return data['choices'][0]['message']['content']
        except Exception as e:
            return f"❌ LLM Connection Error: {e}"

    def run(self):
        print("✅ Orchestrator Ready (Ctrl+C to exit)")
        sys.stdout.flush()
        
        while True:
            try:
                print("\nDanny: ", end="", flush=True)
                user_input = sys.stdin.readline()
                if not user_input: break
                user_input = user_input.strip()
                if not user_input: continue
                
                result = self.chat_with_memory(user_input)
                print(f"\nThe Scribe: {result}\n")
                sys.stdout.flush()
                
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"❌ Runtime Error: {e}")
                sys.stdout.flush()

if __name__ == "__main__":
    print("⏳ Starting Sovereign Lite Orchestrator...")
    agent = SovereignLiteAgent()
    agent.run()
