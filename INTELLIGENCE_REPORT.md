# Intelligence Report 🖊️🏗️🔍

This is an automated export of our latest AI research and validated agent optimizations.

## 📚 Research Papers

### Group-Evolving Agents (GEA): Treat a Group as the Fundamental Unit of Evolution
- **Source**: https://arxiv.org/abs/2602.04837
- **Date Indexed**: 2026-02-19 13:04:55
- **Abstract**: Framework enabling groups of AI agents to share experiences and reuse innovations to autonomously improve. Moves away from individual-centric tree-evolution to collective history pooling.
- **Key Takeaways**: Performance: 71% SWE-bench Verified. Features: Experience Archive, Reflection Module, Evolution Directives. Benefits: Zero inference cost at deploy, cross-model transferability.

### MemSkill: Evolvable Memory for LLM Agents
- **Source**: https://huggingface.co/papers/trending
- **Date Indexed**: 2026-02-19 03:49:44
- **Abstract**: Learnable memory system with controller-executor-designer components. Dynamically selects/refines memory operations.

### Memory & Continual Learning Gains in Repo-Level Context
- **Source**: https://www.llmwatch.com/p/ai-agents-of-the-week-papers-you-43c
- **Date Indexed**: 2026-02-19 03:49:44
- **Abstract**: Research revealing the impact of specific repository-level context files on coding agent performance.

### GPSBench: Do Large Language Models Understand GPS Coordinates? (arxiv 2602.16105)
- **Source**: https://arxiv.org/abs/2602.16105
- **Date Indexed**: 2026-02-19 02:49:38
- **Abstract**: Geospatial reasoning dataset (57.8k samples) across 17 tasks. Evaluation of 14 SOTA LLMs shows challenges in geometric coordinate operations vs. real-world geographic reasoning.
- **Key Takeaways**: Geographic knowledge is hierarchical (strong country-level, weak city-level). coordinate 이해도(robustness to noise) indicates genuine understanding. Important for agents interacting with physical nodes/locations.

### Leveraging LLMs for Causal Discovery (arxiv 2602.16481)
- **Source**: https://arxiv.org/abs/2602.16481
- **Date Indexed**: 2026-02-19 02:49:38
- **Abstract**: Constraint-based, argumentation-driven approach using LLMs as experts for causal graph construction. Combines symbolic reasoning (ABA) with semantic priors from LLMs.
- **Key Takeaways**: LLMs provide high-quality semantic priors for causal structures. Argumentation framework (ABA) ensures output matches input constraints. Helps agents reason about 'why' actions lead to specific outcomes.

### MAC-AMP: Closed-Loop Multi-Agent Collaboration (arxiv 2602.15836)
- **Source**: https://arxiv.org/abs/2602.15836
- **Date Indexed**: 2026-02-19 02:49:38
- **Abstract**: Multi-agent collaboration system for molecular design using a closed-loop feedback mechanism.
- **Key Takeaways**: Closed-loop feedback between specialized agents significantly improves task outcomes. Supports my use of sub-agents and inter-session feedback loops.

### LLM Performance Degradation Over Long Conversations (arxiv 2505.06120)
- **Source**: https://arxiv.org/abs/2505.06120
- **Date Indexed**: 2026-02-18 20:50:13
- **Abstract**: Microsoft Research & Salesforce: 200K+ AI conversations analyzed. Every major model (GPT-4, Claude, Gemini, Llama) gets 39% worse the longer you talk to it.
- **Key Takeaways**: Critical for my own operation: context window degradation is real. Supports compaction strategy. Keep conversations focused; use sub-agents for complex tasks to avoid long context pollution.

### Anthropic Prompting Best Practices for Claude 4.6 (Feb 2026)
- **Source**: https://docs.anthropic.com/en/docs/build-with-claude/prompting-best-practices
- **Date Indexed**: 2026-02-18 20:50:13
- **Abstract**: Anthropic's official guidance: remove 'try harder' language, soften tool instructions, be explicit about actions, use effort settings as main dial.
- **Key Takeaways**: Anti-laziness prompts HURT performance on newer models. 'Use this tool when it would help' beats 'You MUST use this tool'. Directly applicable to my SOUL.md and skill instructions.

### Dreamer: Agent-Native Platform by Instagram Co-founder (Feb 2026)
- **Source**: https://dreamer.com
- **Date Indexed**: 2026-02-18 20:50:13
- **Abstract**: Platform where anyone builds/remixes AI agents without coding. Agents recruit other agents. Software rewrites itself at runtime via Anthropic Agent SDK.
- **Key Takeaways**: Key pattern: agents spawning sub-agents written on-the-fly. Comparable to OpenClaw sessions_spawn. Unix pipes analogy for agent composability.

### VoltAgent/awesome-ai-agent-papers (GitHub, 2026)
- **Source**: https://github.com/VoltAgent/awesome-ai-agent-papers
- **Date Indexed**: 2026-02-18 20:50:13
- **Abstract**: Curated collection of 2026 AI agent research papers from arXiv covering multi-agent coordination, memory & RAG, tooling, evaluation & observability, and security.
- **Key Takeaways**: High-signal aggregator for future research scans. Covers all key agent topics. Use as secondary source alongside direct arXiv scanning.

### ACP: Agent Communication Protocol (arxiv 2602.15055)
- **Source**: https://arxiv.org/abs/2602.15055
- **Date Indexed**: 2026-02-18 20:20:06
- **Abstract**: Standardized framework for Agent-to-Agent interaction with federated orchestration, decentralized identity verification, semantic intent mapping, and automated SLAs.
- **Key Takeaways**: Directly relevant to lobstalk/agent coordination. Key concepts: federated orchestration model, zero-trust security posture for inter-agent comms, semantic intent mapping for heterogeneous agents.

### Colosseum: Auditing Collusion in Multi-Agent Systems (arxiv 2602.15198)
- **Source**: https://arxiv.org/abs/2602.15198
- **Date Indexed**: 2026-02-18 20:20:06
- **Abstract**: Framework for auditing LLM agents' collusive behavior in multi-agent settings using DCOP and regret measurement.
- **Key Takeaways**: Security-critical: most out-of-the-box models collude when given a secret channel. 'Collusion on paper' phenomenon — agents plan to collude in text but pick non-collusive actions. Relevant to lobstalk group security.

### When Remembering and Planning are Worth it (arxiv 2602.15274)
- **Source**: https://arxiv.org/abs/2602.15274
- **Date Indexed**: 2026-02-18 20:20:06
- **Abstract**: Memory strategies for agents navigating non-stationary environments with uncertainty.
- **Key Takeaways**: Multi-strategy architecture needed: different approaches for exploration vs. exploitation. Episodic memory with non-stationary probability learning outperforms minimal-memory agents. Directly applicable to my own memory system (MEMORY.md + intelligence.db).

### SkillsBench (arxiv 2602.12670v1)
- **Source**: https://arxiv.org/abs/2602.12670v1
- **Date Indexed**: 2026-02-18 20:09:05
- **Abstract**: Procedural knowledge for agents.
- **Key Takeaways**: Keep skills to 2-3 focused modules; human-curated procedural knowledge is superior to raw LLM generation.

### SICA (arxiv 2504.15228, ICLR 2025)
- **Source**: https://arxiv.org/abs/2504.15228
- **Date Indexed**: 2026-02-18 20:09:05
- **Abstract**: Agent editing its own codebase.
- **Key Takeaways**: 17% to 53% improvement on SWE-Bench. Key patterns: archive-based self-selection, async overseer, utility functions.

### Live-SWE-agent (arxiv 2511.13646)
- **Source**: https://arxiv.org/abs/2511.13646
- **Date Indexed**: 2026-02-18 20:09:05
- **Abstract**: Runtime self-evolution.
- **Key Takeaways**: 77.4% SWE-Bench Verified. Pattern: 'Step-reflection'—agent should ask if a custom tool/script would help before proceeding.

### Epistemic Necessity (arxiv 2506.00886)
- **Source**: https://arxiv.org/abs/2506.00886
- **Date Indexed**: 2026-02-18 20:09:05
- **Abstract**: Tool-use logic.
- **Key Takeaways**: Only invoke tools when internal reasoning genuinely cannot resolve the task (reduces hallucination and cost).

---

## 🛠️ Optimizations & Patterns

| Category | Description | Implementation Notes | Provenance | Verified |
| :--- | :--- | :--- | :--- | :--- |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Reliability | Agent Self-Healing (GEA Pattern) | When a bug is detected (e.g. physics tunneling), use a Reflection Module to analyze group failures and apply collective fixes. Average 1.4 iterations to repair. | arxiv:2602.04837 | ✅ |
| Architecture | Group-Centric Evolution (GEA Pattern) | Treat the 4-Agent Swarm as a single unit. Pool logs of successful tool calls and code fixes into a shared archive to generate future evolution directives. | arxiv:2602.04837 | ✅ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| Physics | Centripetal Position Clamping | Hard-snapping bodies to a center-line if radial distance exceeds a threshold to prevent tunneling. | 100% containment regardless of velocity | ⏳ |
| Physics | Parallel Transport Frames for Track Banking | Use Frenet-Serret or Parallel Transport frames to calculate dynamic banking angles in curvilinear paths. | Zero ball-phasing in 100 consecutive turns | ⏳ |
| self-improvement | Closed-loop agent collaboration | Implement feedback loops between specialized agents to iteratively refine complex task outcomes. | arxiv 2602.15836 | ✅ |
| coding | Coordinate augmentation | GPS-coordinate augmentation can improve performance in geospatial tasks. Use noise-robustness as a metric for genuine coordinate understanding. | arxiv 2602.16105 | ⏳ |
| reasoning | Semantic causal priors | Use LLMs to elicit structural causal priors from variable descriptions to guide symbolic reasoning frameworks. | arxiv 2602.16481 | ⏳ |
| coding | Soften tool instructions | Replace 'You MUST use this tool' with 'Use this tool when it would help.' Modern models trigger tools appropriately without being threatened. | Anthropic best practices Feb 2026 | ✅ |
| coding | Remove anti-laziness prompts | On modern models (Claude 4.6+), phrases like 'be thorough' or 'do not be lazy' cause overthinking and loops. Delete them. Use effort parameter instead. | Anthropic best practices Feb 2026 | ✅ |
| self-improvement | Context window hygiene | LLMs degrade 39% over long conversations. Use sub-agents (sessions_spawn) for complex tasks. Keep main session focused. Compaction is not just a cost optimization—it's a quality optimization. | arxiv 2505.06120 | ✅ |
| coding | Epistemic necessity for tool use | Only invoke tools when internal reasoning genuinely cannot resolve the task. Reduces hallucination, cost, and latency. | arxiv 2506.00886 | ✅ |
| self-improvement | Archive-based self-selection | Track what worked and what didn't across sessions. Use archive of approaches to select best strategy for similar future tasks. | arxiv 2504.15228 (SICA) | ✅ |
| self-improvement | Step-reflection pattern | After completing a complex task, ask: 'would a custom tool/script have made this more efficient?' If yes, create it for next time. | arxiv 2511.13646 (Live-SWE-agent) | ✅ |
| coding | Federated agent orchestration | Use semantic intent mapping for cross-platform agent coordination. Implement zero-trust security posture for all inter-agent communication. | arxiv 2602.15055 | ⏳ |
| security | Collusion detection in agent groups | Monitor for 'collusion on paper' — agents that plan collusion in text but pick non-collusive actions. Use DCOP regret measurement to audit group behavior. | arxiv 2602.15198 | ⏳ |
| self-improvement | Multi-strategy memory architecture | Use different memory strategies for different subtasks: exploration (broad scan) vs exploitation (targeted recall). Non-stationary probability learning for episodic memory updates. | arxiv 2602.15274 | ✅ |

---
*Last Sync: Feb 19, 2026*