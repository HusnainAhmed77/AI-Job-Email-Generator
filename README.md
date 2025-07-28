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

💡 Sample Input

-Job Title: Machine Learning Intern  
-Company: DeepMind  
-Skills: Python, Deep Learning, Streamlit, GPT, NLP, LangChain


✍️ Generated Output

-Subject: Enthusiastic ML Intern Applicant for DeepMind
    Dear Hiring Team,
    I’m writing to express my deep interest in the Machine Learning Internship at     DeepMind. With hands-on experience in Python, GPT-based NLP models, and           LangChain, I’ve built real-world AI applications using deep learning and          Streamlit. I'm passionate about advancing research that has real impact — and     DeepMind’s work inspires me.
    I’d love the opportunity to contribute to your mission.
    Warm regards,
    Your Name
    
## 🛠 Tech Stack

- Python 🐍
- Streamlit ⚡ (frontend)
- LangChain 🧠 (prompt & LLM orchestration)
- ChromaDB 📂 (vector database for storing resumes)
- Ollama + Mistral 🧙‍♂️ (LLM running locally)

---

## 🧪 How to Run

### 1. Clone the repo

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
