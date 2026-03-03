#!/bin/bash
# init_capabilities.sh

OLLAMA_URL="http://127.0.0.1:11434"
QDRANT_URL="http://127.0.0.1:6333"
COLLECTION_NAME="agent_capabilities"

echo "Step 1: Creating collection $COLLECTION_NAME..."
curl -X DELETE "$QDRANT_URL/collections/$COLLECTION_NAME"
curl -X PUT "$QDRANT_URL/collections/$COLLECTION_NAME" \
  -H "Content-Type: application/json" \
  -d '{
    "vectors": {
      "size": 768,
      "distance": "Cosine"
    }
  }'

echo -e "\nStep 2: Embedding & Upserting Capabilities..."

caps=(
  "1|local|Sensitive data, local server logs, private research, privacy-first queries, and anything that shouldn't leave the machine."
  "2|remote|Complex web research, multi-step planning across global tools, high-speed general reasoning, and public information."
  "3|local|Agentic swarm orchestration, testing local multi-agent patterns, and low-latency interaction with local services."
)

for cap in "${caps[@]}"; do
  IFS="|" read -r id target desc <<< "$cap"
  echo "Processing #$id: $desc"
  
  # Get Embedding
  vector=$(curl -s "$OLLAMA_URL/api/embeddings" -d "{
    \"model\": \"nomic-embed-text\",
    \"prompt\": \"$desc\"
  }" | jq -c '.embedding')

  # Upsert to Qdrant
  curl -s -X PUT "$QDRANT_URL/collections/$COLLECTION_NAME/points?wait=true" \
    -H "Content-Type: application/json" \
    -d "{
      \"points\": [
        {
          \"id\": $id,
          \"vector\": $vector,
          \"payload\": {
            \"target\": \"$target\",
            \"description\": \"$desc\"
          }
        }
      ]
    }" | jq .
done

echo "✅ Initialization complete!"
