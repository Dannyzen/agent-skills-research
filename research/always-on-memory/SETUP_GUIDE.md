# The Sovereign Scribe: Setup Guide

This guide will help you run the "Living Charter" MVP using the Always-On Memory Agent architecture.

## 1. Prerequisites
- Python 3.10+
- An API Key for Gemini (Google AI Studio) OR a local LLM endpoint.

## 2. Installation
```bash
cd research/always-on-memory
pip install -r requirements.txt
```

## 3. Configuration
Set your API key (if using Gemini):
```bash
export GOOGLE_API_KEY="your-key-here"
```

## 4. Run the Agent (Backend)
This starts the background process that watches for new files and consolidates memory.
```bash
python agent.py
```

## 5. Run the Dashboard (Frontend)
In a new terminal:
```bash
streamlit run dashboard.py
```

## 6. The Demo Workflow
1.  Open the dashboard (http://localhost:8501).
2.  **Upload** the `research/digital-bylaws/test_bylaws.pdf` (or any PDF).
3.  Wait ~10 seconds for the agent to ingest it.
4.  **Ask:** "What is the policy on alcohol reimbursement?"
5.  **Observe:** The agent will cite the specific document and section.

## 7. Customization (The "Sovereign" Touch)
To enforce the "Dual-Helix" logic (High vs Low Authority), we will modify `agent.py` to check for metadata tags in the consolidation step.
