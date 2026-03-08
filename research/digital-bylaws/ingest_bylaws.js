// The Digital Bylaws Ingestion Pipeline (Node.js Edition)
// Demonstrates ingestion of conflicting documents and "Dual-Helix" resolution.

const { QdrantClient } = require('@qdrant/js-client-rest');

// --- Config ---
const QDRANT_HOST = 'http://localhost:6333';
const COLLECTION_NAME = 'digital_bylaws';

// --- Mock Embedding Function ---
function getEmbedding(text) {
    // Simulate a 768-dim vector (all 0.1s for demo structure)
    return Array(768).fill(0.1);
}

// --- The Pipeline ---
async function main() {
    console.log(`🚀 Ingesting 'Conflict Data' into Qdrant collection: ${COLLECTION_NAME}`);
    
    const client = new QdrantClient({ url: QDRANT_HOST });
    
    // 1. Reset Collection
    try {
        await client.deleteCollection(COLLECTION_NAME);
    } catch (e) {
        // Ignore if doesn't exist
    }
    
    await client.createCollection(COLLECTION_NAME, {
        vectors: { size: 768, distance: 'Cosine' }
    });
    
    // 2. Load Data
    const documents = [
        {
            id: 1,
            text: "Hey team! Good news. For the upcoming holiday party, we are authorizing a one-time reimbursement for wine and beer. Keep the receipts under $500 total.",
            meta: { source: "Email", authority: "low", date: "2022-12-15" }
        },
        {
            id: 2,
            text: "Strictly Prohibited Expenses: Under no circumstances shall organizational funds be used for the purchase of alcohol, tobacco products, or personal entertainment. This policy supersedes all prior memos.",
            meta: { source: "Handbook", authority: "high", date: "2024-01-01" }
        }
    ];
    
    // 3. Ingest
    const points = documents.map(doc => ({
        id: doc.id,
        vector: getEmbedding(doc.text),
        payload: doc.meta
    }));
    
    await client.upsert(COLLECTION_NAME, { points });
    console.log("✅ Ingestion Complete: 2 Documents stored (1 High Authority, 1 Low Authority).");
    
    // 4. Query & Resolve
    await queryPolicy(client, "Can I expense wine for the party?");
}

async function queryPolicy(client, question) {
    console.log(`\n❓ Query: '${question}'`);
    console.log("🔍 Searching Qdrant...");
    
    // In a real scenario, we'd embed the question and search.
    // Here we simulate the retrieval of the docs we just inserted.
    // Crucial: We can filter or sort by authority metadata in the application logic.
    
    const searchResult = await client.retrieve(COLLECTION_NAME, { ids: [1, 2] });
    
    console.log(`  -> Found ${searchResult.length} matches.`);
    
    // Sort by Authority (High > Low) and Date (New > Old)
    // Simple logic for demo: High beats Low.
    const sortedDocs = searchResult.sort((a, b) => {
        const authScore = { high: 2, medium: 1, low: 0 };
        return authScore[b.payload.authority] - authScore[a.payload.authority];
    });
    
    const winner = sortedDocs[0];
    const loser = sortedDocs[1];
    
    console.log(`  -> Winner: [Authority: ${winner.payload.authority.toUpperCase()}] (Date: ${winner.payload.date})`);
    console.log(`  -> Loser:  [Authority: ${loser.payload.authority.toUpperCase()}] (Date: ${loser.payload.date})`);
    
    console.log("\n🤖 AI Reasoning (The Dual-Helix):");
    console.log(`  - Conflict Detected.`);
    console.log(`  - Rule: High Authority (${winner.payload.source}) overrides Low Authority (${loser.payload.source}).`);
    
    console.log("\n💬 Final Answer:");
    console.log("No, you cannot be reimbursed. The **2024 Expense Policy** (High Authority) strictly prohibits alcohol, superseding the 2022 Email.");
}

main().catch(console.error);
