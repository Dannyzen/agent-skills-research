# Skill: Memory (Qdrant)

This skill provides a simple CLI for interacting with the local Qdrant instance. It allows the agent to save knowledge, search for relevant context, and list available collections.

## Setup

1.  Ensure Qdrant is running and accessible at `http://10.0.2.2:6333` (or configured via `QDRANT_URL`).
2.  Install dependencies: `npm install` in the skill directory.

## Usage

### Save a memory
```bash
node index.js save --collection research_notes --text "DeepSeek-R1 is excellent for planning." --tags "llm,planning"
```

### Search memories
```bash
node index.js search --collection research_notes --query "planning models" --limit 3
```

### List collections
```bash
node index.js list
```

## Configuration
- `QDRANT_URL`: URL of the Qdrant instance (default: `http://10.0.2.2:6333`)
- `EMBEDDING_MODEL`: (Optional) If using a local embedding service, specify here. Currently uses a mock/simple embedding for demonstration or relies on Qdrant's built-in if configured. *Note: For production, we should connect this to a real embedding model.*
