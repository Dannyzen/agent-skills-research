# The Digital Bylaws Ingestion Pipeline

This project is a critical component of the "Living Charter" product. It transforms static documents (PDFs, Word Docs) into a **Structured, Authoritative Knowledge Graph** (The Torah).

## 🎯 The Mission
Generic RAG systems fail because they treat all text as equal. They confuse a casual email from 2019 with a Board Resolution from 2024.
Our pipeline solves this by introducing **Authority Tags**.

## ⚙️ How it Works
1.  **Ingest:** Reads documents from `input/`.
2.  **Chunk:** Splits text by semantic boundaries (Articles, Sections).
3.  **Tag:** Assigns metadata:
    - `authority_level`: (High/Med/Low)
    - `date`: (YYYY-MM-DD)
    - `source_type`: (Bylaw, Policy, Email)
4.  **Embed:** Stores vectors in Qdrant (Sovereign Memory).

## 🧪 The "Conflict Resolution" Test
We will ingest two conflicting documents:
1.  `2022_Email.txt`: "Sure, buy wine for the party!" (Low Authority)
2.  `2024_Expense_Policy.pdf`: "Alcohol is strictly prohibited." (High Authority)

The query engine will be tested to ensure it prioritizes the **High Authority** source.
