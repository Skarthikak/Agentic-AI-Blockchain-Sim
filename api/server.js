const express = require('express');
const cors = require('cors');
const WebSocket = require('ws');
const http = require('http');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

app.use(cors());
app.use(express.json());

// Mock blockchain state
let blockchainState = {
  blockNumber: 1,
  predictions: [],
  agents: [],
  transactions: []
};

// WebSocket connections for real-time updates
wss.on('connection', (ws) => {
  console.log('New dashboard connected');
  ws.send(JSON.stringify({ type: 'initial_state', data: blockchainState }));
});

// Broadcast to all connected clients
function broadcast(data) {
  wss.clients.forEach(client => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(JSON.stringify(data));
    }
  });
}

// API Routes
app.get('/api/blockchain/state', (req, res) => {
  res.json(blockchainState);
});

app.post('/api/predictions/submit', (req, res) => {
  const { agent, marketId, predictionValue } = req.body;
  const prediction = {
    id: blockchainState.predictions.length + 1,
    agent,
    marketId,
    predictionValue,
    timestamp: new Date().toISOString(),
    resolved: false,
    correct: null
  };
  
  blockchainState.predictions.push(prediction);
  blockchainState.transactions.push({
    type: 'prediction_submission',
    ...prediction
  });
  
  broadcast({ type: 'new_prediction', data: prediction });
  broadcast({ type: 'new_transaction', data: prediction });
  
  res.json({ success: true, predictionId: prediction.id });
});

app.post('/api/agents/register', (req, res) => {
  const { agentId, capabilities } = req.body;
  const agent = {
    id: agentId,
    capabilities,
    registrationDate: new Date().toISOString(),
    score: 0
  };
  
  blockchainState.agents.push(agent);
  broadcast({ type: 'agent_registered', data: agent });
  
  res.json({ success: true, agent });
});

const PORT = process.env.PORT || 3001;
server.listen(PORT, () => {
  console.log(`Mock Blockchain API running on port ${PORT}`);
});
