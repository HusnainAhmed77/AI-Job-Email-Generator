# 🤖 AI Cold Email Generator (100% Free & Local)

A smart, local AI tool to generate personalized cold emails for job applications, freelancing, or client outreach — using Streamlit, LangChain, ChromaDB, and Mistral (via Ollama).

---

## 🚀 Features

- 📝 Input: job title, company name, resume/skills
- 🤖 Generates a professional cold email using local LLM (Mistral)
- 💾 Save/load resume with ChromaDB
- 📥 Export email as `.txt`
- 🧠 100% free – no OpenAI API required

---

## 🛠 Tech Stack

- Python 🐍
- Streamlit ⚡ (frontend)
- LangChain 🧠 (prompt & LLM orchestration)
- ChromaDB 📂 (vector database for storing resumes)
- Ollama + Mistral 🧙‍♂️ (LLM running locally)

---

## 🧪 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/job-email-generator.git
cd job-email-generator

2. Install dependencies
pip install -r requirements.txt

3. Install Ollama and run Mistral
brew install ollama
ollama run mistral
Or use ollama serve in a background terminal.

4. Run the app
streamlit run app.py
