# Sefaria API Protocol for Agents

Use the Sefaria API to fetch high-fidelity primary sources.

## Core Endpoints
- **GET** `https://www.sefaria.org/api/texts/:ref`
- Example: `https://www.sefaria.org/api/texts/Genesis.1`

## Implementation Pattern
When an agent is asked for a source:
1. Fetch raw JSON.
2. Extract the `text` (English) and `he` (Hebrew) fields.
3. Check the `versionTitle` to ensure it is a recognized scholarly translation.
4. Embody the text in the response with the exact citation.
