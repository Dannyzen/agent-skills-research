import os
import sys
import json
import requests
from typing import List, Dict, Any

# Environment Config
ROUTER_URL = os.getenv("ROUTER_URL", "http://sovereign-llm:11434/v1")
WORKER_URL = os.getenv("WORKER_URL", "http://sovereign-llm:11434/v1")
QDRANT_URL = os.getenv("QDRANT_URL", "http://sovereign-qdrant:6333")
MODEL_NAME = os.getenv("MODEL_NAME", "llama3")

class SovereignLiteAgent:
    def __init__(self):
        print(f"🤖 Sovereign Lite Agent Initialized (Model: {MODEL_NAME})")
        self.history = []

    def get_memory(self, query: str, collection: str = "research_notes", limit: int = 2) -> str:
        """Search Qdrant for relevant context."""
        print(f"🧠 Searching Memory for: '{query}'...")
        # Note: In a real app, we'd embed the query first. 
        # For this 'Lite' version, we'll use Qdrant's scroll/filter or assume 
        # the model knows what to look for. 
        # REALITY CHECK: Qdrant search requires embeddings. 
        # Since we are in the orchestrator container, we'd need an embedding model.
        # TEMPORARY LITE SOLUTION: We will pull the latest 3 points as 'recent context'
        # until we add an embedding sidecar.
        
        try:
            url = f"{QDRANT_URL}/collections/{collection}/points/scroll"
            payload = {"limit": limit, "with_payload": True}
            resp = requests.post(url, json=payload, timeout=5)
            if resp.status_code == 200:
                points = resp.json().get("result", {}).get("points", [])
                context = "\n".join([str(p['payload']) for p in points])
                return context if context else "No relevant memory found."
            return "Memory service unavailable."
        except Exception as e:
            return f"Memory Error: {e}"

    def chat_with_memory(self, user_query: str):
        """Chat with the LLM using Qdrant context."""
        # 1. Retrieve context
        context = self.get_memory(user_query)
        
        # 2. Build augmented prompt
        system_prompt = f"""You are Sovereign Lite, a local AI. 
        Use the following RECALLED MEMORY to inform your answer. 
        If the memory is irrelevant, ignore it.
        
        RECALLED MEMORY:
        {context}
        """
        
        print(f"📡 Sending to LLM with Context...")
        payload = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            "stream": False
        }
        
        try:
            url = f"{ROUTER_URL}/chat/completions"
            resp = requests.post(url, json=payload, timeout=90)
            if resp.status_code != 200:
                 return f"⚠️ API Error {resp.status_code}: {resp.text}"
            
            data = resp.json()
            return data['choices'][0]['message']['content']
        except Exception as e:
            return f"❌ Connection Error: {e}"

    def run(self):
        print("✅ Ready for input (Ctrl+C to exit)")
        sys.stdout.flush()
        
        while True:
            try:
                print("User: ", end="", flush=True)
                user_input = sys.stdin.readline()
                if not user_input: break
                user_input = user_input.strip()
                if not user_input: continue
                
                result = self.chat_with_memory(user_input)
                print(f"\nAgent: {result}\n")
                sys.stdout.flush()
                
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                sys.stdout.flush()

if __name__ == "__main__":
    print("⏳ Verifying stack...")
    # Basic check for LLM and Qdrant
    agent = SovereignLiteAgent()
    agent.run()
