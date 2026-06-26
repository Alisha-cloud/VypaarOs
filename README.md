# 🚀 VyapaarOS

> AI-Powered Business Operating System for Small Businesses & E-Commerce Sellers

VyapaarOS is an intelligent multi-agent business decision platform that helps businesses analyze performance, forecast revenue, optimize pricing, generate marketing strategies, and receive AI-powered recommendations from uploaded business documents and analytics.

---

## 🌟 Features

### 📄 Business Document Intelligence
- Upload TXT files
- Upload CSV files
- Upload PDF files
- Knowledge extraction from uploaded business data

### 🤖 Multi-Agent AI Workflow
Built using LangGraph and Agent Architecture.

Agents included:

- Research Agent
- Inventory Agent
- Analytics Agent
- Forecast Agent
- Pricing Agent
- Simulation Agent
- Recommendation Agent
- Listing Agent
- Marketing Agent
- Festival Agent
- Competitor Agent
- Advisor Agent

---

### 📊 Business Analytics Dashboard

Provides:

- Revenue Tracking
- Sales Tracking
- Average Order Value (AOV)
- Revenue Forecast Visualization
- Business Performance Metrics

---

### 💡 AI Business Copilot

Interactive AI assistant that can answer questions such as:

- How can I increase sales?
- Which product should I promote?
- What pricing strategy should I use?
- How can I improve inventory turnover?
- How should I market during festivals?

---

### 📈 Forecasting Engine

Predicts:

- Future Revenue
- Growth Potential
- Sales Opportunities

---

### 🏷️ Pricing Intelligence

Automatically recommends:

- Product pricing
- Discount strategies
- Conversion optimization opportunities

---

### 📣 Marketing Automation

Generates:

- Instagram Captions
- WhatsApp Campaign Messages
- Festival Campaign Ideas
- SEO Keywords

---

### 📄 PDF Report Export

Generate downloadable business reports including:

- Executive Summary
- Business Insights
- Pricing Strategy
- Inventory Strategy
- Marketing Strategy
- Risks
- Growth Opportunities

---

## 🏗️ System Architecture

```text
User Goal
    ↓
Planner Agent
    ↓
Research Agent
    ↓
Inventory Agent
    ↓
Analytics Agent
    ↓
Forecast Agent
    ↓
Pricing Agent
    ↓
Simulation Agent
    ↓
Recommendation Agent
    ↓
Listing Agent
    ↓
Marketing Agent
    ↓
Festival Agent
    ↓
Competitor Agent
    ↓
Advisor Agent
    ↓
Final Business Report
```

---

## 🛠️ Tech Stack

### Frontend

- Next.js
- TypeScript
- Tailwind CSS
- Axios
- Recharts
- React Markdown

### Backend

- FastAPI
- LangGraph
- LangChain
- Google Gemini
- FAISS
- Sentence Transformers
- Pandas
- NumPy
- ReportLab

### AI Components

- Gemini 2.5 Flash
- Multi-Agent Workflow
- Retrieval-Augmented Generation (RAG)
- Business Recommendation Engine

---

## 📂 Project Structure

```text
vyapaaros/
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── lib/
│   │   └── styles/
│
├── backend/
│   ├── agents/
│   ├── routes/
│   ├── services/
│   ├── workflow/
│   ├── exports/
│   └── main.py
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/vyapaaros.git

cd vyapaaros
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Create `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run Backend

```bash
uvicorn main:app --reload
```

Backend:

```text
http://localhost:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install
```

Create `.env.local`

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Run Frontend

```bash
npm run dev
```

Frontend:

```text
http://localhost:3000
```

---

### Dashboard

- Revenue Analytics
- Sales Metrics
- Forecast Charts

### AI Copilot

- Business Question Answering
- Strategy Recommendations

### Report Generator

- Executive Business Reports
- PDF Export

---

## 🎯 Use Cases

- Small Businesses
- E-Commerce Sellers
- Retail Stores
- Startup Founders
- Business Analysts
- Marketing Teams

---

## 🔮 Future Enhancements

- Real-Time Market Data Integration
- Competitor Web Scraping
- Multi-Language Support
- Voice-Based Copilot
- Automated Campaign Launch
- Customer Segmentation Engine
- Predictive Inventory Management

---


