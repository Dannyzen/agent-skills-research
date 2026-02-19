# Agentic Firmware: Technical Specifications

To be a "Sovereign Intelligence," an agent's harness must support the following:

## 1. The Multi-Model Divergence
Harnesses must support hot-swapping between:
- **Worker Tier**: (e.g., DeepSeek, Gemini Flash) for 100x iteration tasks.
- **Reasoning Tier**: (e.g., Claude Opus 4.6, GPT-o3) for strategy and final commitment.

## 2. Shared Experience Architecture
- **Local SQLite Storage**: Use `intelligence.db` patterns for structured research logging.
- **Event-Driven Memory**: Every breakthrough must be emitted as a system event for group reflection.

## 3. Tool Synthesis Logic
Agents must not just use tools; they must *write* tools.
- **Python on the Fly**: Capability to author and execute task-specific scripts to bypass API limitations.
- **Node-JS Steerage**: Native `npm` and `node` access for modern web interaction (e.g., Puppeteer).
