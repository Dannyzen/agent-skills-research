#!/usr/bin/env node
const { Command } = require('commander');
const axios = require('axios');
const fs = require('fs');
const path = require('path');
const { v4: uuidv4 } = require('uuid');

const program = new Command();
const QDRANT_URL = process.env.QDRANT_URL || 'http://10.0.2.2:6333';
const DIMENSION = 768; // Default for small embeddings

// Helper: Simple/Mock Embedding (for demo without dedicated service)
// In production, this would call a real embedding API (e.g., local BERT/SentenceTransformer)
function getEmbedding(text) {
  // Simple hash-based mock embedding for demonstration
  const vector = new Array(DIMENSION).fill(0);
  let hash = 0;
  for (let i = 0; i < text.length; i++) {
    hash = ((hash << 5) - hash) + text.charCodeAt(i);
    hash |= 0;
  }
  // Fill vector with pseudo-random values seeded by text hash
  for (let i = 0; i < DIMENSION; i++) {
    vector[i] = (Math.sin(hash + i) + 1) / 2;
  }
  return vector;
}

// Command: Save
program
  .command('save <text>')
  .description('Save a memory into Qdrant')
  .option('-c, --collection <name>', 'Collection name', 'general_memory')
  .option('-t, --tags <tags>', 'Comma-separated tags', '')
  .action(async (text, options) => {
    try {
      const collection = options.collection;
      const tags = options.tags.split(',').map(t => t.trim()).filter(Boolean);
      const embedding = getEmbedding(text);
      const pointId = uuidv4();

      // Ensure collection exists (lazy creation)
      try {
        await axios.get(`${QDRANT_URL}/collections/${collection}`);
      } catch (e) {
        if (e.response && e.response.status === 404) {
          console.log(`Creating collection '${collection}'...`);
          await axios.put(`${QDRANT_URL}/collections/${collection}`, {
            vectors: { size: DIMENSION, distance: 'Cosine' }
          });
        }
      }

      // Upsert point
      const payload = {
        points: [{
          id: pointId,
          vector: embedding,
          payload: { text, tags, timestamp: Date.now() }
        }]
      };

      await axios.put(`${QDRANT_URL}/collections/${collection}/points?wait=true`, payload);
      console.log(`✅ Memory saved (ID: ${pointId})`);
    } catch (error) {
      console.error('Error saving memory:', error.response?.data || error.message);
    }
  });

// Command: Search
program
  .command('search <query>')
  .description('Search memories using semantic similarity')
  .option('-c, --collection <name>', 'Collection name', 'general_memory')
  .option('-l, --limit <number>', 'Max results', '3')
  .action(async (query, options) => {
    try {
      const collection = options.collection;
      const embedding = getEmbedding(query); // Search using same embedding logic

      const response = await axios.post(`${QDRANT_URL}/collections/${collection}/points/search`, {
        vector: embedding,
        limit: parseInt(options.limit),
        with_payload: true
      });

      if (response.data.result.length === 0) {
        console.log('No relevant memories found.');
        return;
      }

      console.log(`🔍 Found ${response.data.result.length} matches:\n`);
      response.data.result.forEach((hit, i) => {
        const payload = hit.payload || {};
        const title = payload.title || payload.text || '(No content)';
        const content = payload.content || '';
        const date = payload.timestamp ? new Date(payload.timestamp).toLocaleString() : '(No date)';
        
        console.log(`${i + 1}. [Score: ${hit.score.toFixed(4)}] ${date}`);
        console.log(`   Title/Text: ${title}`);
        if (content) console.log(`   Content: ${content.substring(0, 100)}...`);
        
        const tags = payload.tags || [];
        if (tags.length) console.log(`   Tags: ${tags.join(', ')}`);
        console.log('');
      });

    } catch (error) {
      console.error('Error searching memory:', error.response?.data || error.message);
    }
  });

// Command: List
program
  .command('list')
  .description('List available memory collections')
  .action(async () => {
    try {
      const response = await axios.get(`${QDRANT_URL}/collections`);
      const collections = response.data.result.collections.map(c => c.name);
      console.log('📂 Available Collections:');
      collections.forEach(c => console.log(` - ${c}`));
    } catch (error) {
      console.error('Error listing collections:', error.response?.data || error.message);
    }
  });

program.parse(process.argv);
