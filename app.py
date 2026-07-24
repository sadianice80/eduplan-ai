import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="EduPlan AI", page_icon="📚")

st.title("📚 EduPlan AI — Lesson Plan & Quiz Generator")
st.subheader("Generate structured lesson plans and quizzes for teachers in seconds!")

# Sidebar for API Key
api_key = st.sidebar.text_input("Enter Google Gemini API Key:", type="password")

# Form Inputs
subject = st.text_input("Subject", placeholder="e.g. English, Science, Mathematics")
topic = st.text_input("Topic", placeholder="e.g. Photosynthesis, Fractions, Nouns")
grade = st.selectbox("Grade Level", ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8"])
duration = st.number_input("Duration (Minutes)", min_value=10, max_value=120, value=40)

if st.button("✨ Generate Lesson Plan & Quiz"):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar!")
    elif not subject or not topic:
        st.warning("Please fill in both Subject and Topic.")
    else:
        try:
            genai.configure(api_key=api_key)
            # 2.0 Flash is lightweight and has high free quotas
            model = genai.GenerativeModel('gemini-1.5-flash-8b')
            
            prompt = f"Create a structured lesson plan and a short 5-question quiz for {subject} on topic '{topic}' for {grade} students. Duration: {duration} minutes."
            
            with st.spinner("Generating..."):
                response = model.generate_content(prompt)
                st.success("Generated Successfully!")
                st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
