# Agent Workspace

This repository contains the configuration, memory, and skills for the OpenClaw agent running in this environment.

## Overview

- **Skills:** Custom tools developed by the agent (e.g., `skills/memory`).
- **Memory:** Long-term memory stored in `MEMORY.md`. Daily logs in `memory/YYYY-MM-DD.md`.
- **Knowledge Base:** Vector database (Qdrant) storing structured knowledge.
- **Agent Identity:** Configuration in `AGENTS.md`, `SOUL.md`, `USER.md`.

## Setup

1.  Clone this repository:
    ```bash
    git clone <repository-url>
    cd clawd
    ```

2.  Install dependencies for skills:
    ```bash
    cd skills/memory
    npm install
    ```

3.  Ensure Qdrant is running:
    ```bash
    # (Assuming Docker is available)
    docker run -p 6333:6333 qdrant/qdrant
    ```

## Maintenance

This repository is maintained by the agent itself. It periodically commits changes to its configuration and memory.
