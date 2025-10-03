#!/bin/bash

echo "🚀 Setting up Agentic AI Blockchain Simulator..."

# Check if Python and Node are installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed."
    exit 1
fi

echo "✅ Python and Node.js found"

# Setup AI Agents
echo "📦 Setting up AI Agents..."
cd ai-agents
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# Setup API
echo "🌐 Setting up API..."
cd api
npm install
cd ..

# Setup Frontend
echo "🖥️ Setting up Frontend..."
cd frontend
npm install
cd ..

# Setup Smart Contracts
echo "⛓️ Setting up Smart Contracts..."
cd smart-contracts
npm install
cd ..

echo "🎉 Setup complete!"
echo ""
echo "To run the simulation:"
echo "1. Start API: cd api && npm run dev"
echo "2. Start AI Agents: cd ai-agents && source venv/bin/activate && python main.py"
echo "3. Start Frontend: cd frontend && npm start"
echo ""
echo "Visit http://localhost:3000 to view the dashboard"
