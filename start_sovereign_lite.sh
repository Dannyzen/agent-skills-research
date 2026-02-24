#!/bin/bash
set -e

echo "🚀 Starting 'Sovereign Lite' Stack..."

# 1. Check prerequisites
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found!"
    exit 1
fi

# 2. Start Infrastructure (Qdrant)
echo "📦 Spinning up Base Infrastructure (Qdrant)..."
docker-compose -f infra-compose.yml up -d qdrant

# 3. Start LLM Services
echo "📦 Spinning up Sovereign Lite Services (LLM + Model Puller)..."
docker-compose -f sovereign-lite-compose.yml up -d llm model-puller

# 4. Wait for services to be healthy (basic check)
echo "⏳ Waiting for services to initialize..."
sleep 5 

# 5. Build Orchestrator
echo "🤖 Building Orchestrator..."
docker-compose -f sovereign-lite-compose.yml build orchestrator

echo "✅ sovereign-lite stack is running!"
echo "To interact with the agent, run:"
echo "  docker-compose -f sovereign-lite-compose.yml run --rm orchestrator"
