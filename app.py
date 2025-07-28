import streamlit as st
from modules.generator import generate_email
from modules.chroma_handler import save_resume, get_resume


st.set_page_config(page_title="AI Job Email Generator", page_icon="📧")

st.title("📧 AI Job Email Generator")
st.markdown("Generate personalized cold emails for job applications or client outreach using a local LLM (Mistral via Ollama).")

job_title = st.text_input("💼 Job Title", placeholder="e.g., Machine Learning Intern")
company_name = st.text_input("🏢 Company Name", placeholder="e.g., OpenAI")
skills = st.text_area("🧠 Your Skills / Resume Highlights", placeholder="e.g., Python, Deep Learning, GPT-4, NLP")

if st.button(" Generate Email"):
    if not job_title or not company_name or not skills.strip():
        st.warning("Please fill out all fields to generate the email.")
    else:
        email = generate_email(job_title, company_name, skills)
        st.success("✅ Email generated successfully!")
        st.text_area("📨 Cold Email", email, height=250)

with st.expander("💾 Save / Load Resume"):
    user_id = st.text_input("User ID (for saving)", value="default_user")

    if st.button("💾 Save Resume"):
        save_resume(user_id, skills)
        st.success("Resume Saved Successfully!")

    if st.button("📂 Load Saved Resume"):
        loaded_skills = get_resume(user_id)
        if loaded_skills:
            st.success("Loaded resume data:")
            st.text_area("🔁 Loaded Skills", value=loaded_skills, height=150)

            skills=loaded_skills
        else:
            st.warning("No resume found for this user.")