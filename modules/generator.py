from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(model="mistral")

template = """
You are an expert at writing cold outreach emails for job applications.
Write a short, personalized email for someone applying as a {job_title} at {company_name}.
Use the following skills and background: {skills}

The email should sound professional, enthusiastic, and human-like.
Do not use bullet points. Keep it concise (5–7 sentences). Add a subject line.
"""

prompt = PromptTemplate(
    input_variables=["job_title", "company_name", "skills"],
    template=template,
)

email_chain = LLMChain(llm=llm, prompt=prompt)

def generate_email(job_title, company_name, skills):
    return email_chain.run({
        "job_title": job_title,
        "company_name": company_name,
        "skills": skills
    })