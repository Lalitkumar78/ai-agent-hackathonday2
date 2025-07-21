import streamlit as st
import openai

st.set_page_config(page_title="AI Job Matcher", layout="centered")

st.title("🔍 AI Job Matcher")
st.write("Paste your resume below to get matched with the best-fit jobs.")

openai.api_key = st.secrets["OPENAI_API_KEY"]

resume_text = st.text_area("Paste your resume here:", height=300)

if st.button("Analyze & Suggest Jobs"):
    with st.spinner("Analyzing your resume..."):
        prompt = f"""
        Based on this resume, suggest the best 3 job roles. 
        Explain why each is a good fit, list missing skills, and give improvement tips.

        Resume:
        {resume_text}
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.markdown("### 🧠 AI Suggestions")
        st.write(response['choices'][0]['message']['content'])
