# Hybrid Model Stack for the Local-First/Cloud-Hybrid Agent Workflow

## Goal
Keep your local machine responsive (M5 Max 128GB) and still get high-end reasoning when needed.

---

## 1) Recommended two-tier model ladder

### Tier A (Local-first, cheap, fast)
- **Where:** Apple M5 Max
- **What to run:** light to medium copilots for quick tasks
- **Use for:**
  - short Q&A, drafting, summaries, classification
  - retrieval+templated prompts
  - simple tool calls
  - routing pre-check and context packaging
- **Examples:** FunctionGemma / Llama3 local models you already have, plus embeddings (`nomic-embed-text`).

### Tier B (Remote heavy, expensive, deep)
- **Where:** remote endpoint with Nemotron-like scale (NIM/API)
- **What to use:** high-context and hard reasoning jobs
- **Use for:**
  - long documents (large context)
  - complex architecture/risk analysis
  - multi-step tool-call loops
  - ambiguous requests where policy/edge reasoning matters
- **Goal:** only escalate a minority of calls.

---

## 2) Routing rules (automatic)

**Send to remote (Tier B) if any condition hits):**
- `estimated_tokens > 3500` (or context window estimate > 4k)
- `expected_reasoning = high` (words: “analyze, audit, architecture, compare, evaluate, reason about risk, generate strategy”)
- `tool_steps > 2` (multi-step tasks)
- `requires_latest_info = true` (if explicitly says check recent docs/web/news)
- `contains_policy_or_legal` (policy, compliance, contract, governance)
- `retry_count > 0` after local attempt

**Keep local (Tier A) by default for:**
- status checks
- summaries / paraphrase
- formatting
- meeting notes cleanup
- list generation and simple planning

**Escalate on uncertainty:**
- If local confidence < 0.82, call Tier B.

---

## 3) Simple priority thresholds (copy into code later)

- `fast` lane
  - <= 2k input tokens
  - <= 1 tool call
  - no policy/compliance context
- `deep` lane
  - > 4k input tokens or 1M-context candidate
  - > 2 tool steps
  - executive-style strategic or architectural reasoning

---

## 4) Concrete architecture (practical)

- **Controller:** keep your OpenClaw orchestrator as the single front door.
- **Decision module:** tiny policy engine that scores each request.
- **Local model service:** your existing Ollama/FunctionGemma route.
- **Remote model service:** Nemotron endpoint (NVIDIA NIM or API wrapper) behind queue + timeout guard.
- **Caching:** cache by prompt hash so repeated heavy prompts reuse prior answer when safe.
- **Audit log:** store every deep call with:
  - prompt hash
  - model used
  - latency
  - token count
  - result hash

---

## 5) Recommended deployment split

### On M5 Max (local)
- Frontend/chat interface
- routing + sanitization
- small/medium LLM inference
- vector retrieval (Qdrant)
- docs indexing and chunking

### Remote (GPU cloud)
- deep policy + legal/risk reasoning
- long-context document synthesis
- high-stakes executive outputs

---

## 6) Cost control and reliability

- Use `prefer_fast=true` default.
- Add daily budget cap for Tier B calls.
- Retry policy:
  - local timeout: 20s
  - remote timeout: 90s
- If remote unavailable, auto-fallback to local and tag output as “low-confidence: no deep model”.

---

## 7) Minimal implementation path (1-week build)

### Day 1
- add routing config file (`hybrid_routing.yaml`)
- implement scorer with keyword + token estimates

### Day 2
- add policy gate + fallback mode
- wire local and remote wrappers

### Day 3
- add logging/audit + dashboard counters
- add “why escalated?” note in each response

### Day 4
- define per-user/team thresholds

### Day 5
- run load test + tune triggers

### Day 6–7
- hand off to pilot users and tune.

---

## 8) Starter escalation prompt (to include in orchestrator)

"Route to deep model if request is high-risk, long-context, legal/compliance, multi-step tool usage, or requires strategic recommendations." 

---

## 9) What this unlocks

- keeps your local system fast and private for most tasks
- reserves expensive compute for high-value problems
- gives predictable quality + predictable spend
- fits your hardware realities (M5 Max stays useful, no false “this must be local”).
