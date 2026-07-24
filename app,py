import streamlit as st
import google.generativeai as genai
import os

# Page Configuration
st.set_page_config(page_title="EduPlan AI", page_icon="📚", layout="wide")

st.title("📚 EduPlan AI — Lesson Plan & Quiz Generator")
st.write("Generate structured lesson plans and quizzes for teachers in seconds!")

# Sidebar for API Key input
api_key = st.sidebar.text_input("Enter Google Gemini API Key:", type="password")

if not api_key:
    api_key = os.getenv("GEMINI_API_KEY", "")

# Input Form
with st.form("lesson_form"):
    col1, col2 = st.columns(2)
    with col1:
        subject = st.text_input("Subject", placeholder="e.g. English, Science, Mathematics")
        grade = st.selectbox("Grade Level", ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10"])
    with col2:
        topic = st.text_input("Topic", placeholder="e.g. Photosynthesis, Fractions, Nouns")
        duration = st.number_input("Duration (Minutes)", value=40, step=5)
    
    submit_button = st.form_submit_button("✨ Generate Lesson Plan & Quiz")

if submit_button:
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar or configure secrets!")
    elif not subject or not topic:
        st.warning("Please fill in both Subject and Topic.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            You are an expert educational designer and teacher's assistant. Your task is to generate a structured {duration}-minute lesson plan along with a 5-question multiple-choice quiz based on the following details:
            - Subject: {subject}
            - Grade Level: {grade}
            - Topic: {topic}

            Please format the output nicely with clear headings:
            1. Lesson Overview & Learning Objectives
            2. Required Materials
            3. Time Breakdown (Warm-up, Core Instruction, Practice Activity, Wrap-up)
            4. 5-Question Multiple Choice Quiz (with Answer Key at the bottom)
            5. Suggested Homework Assignment
            """
            
            with st.spinner("Generating lesson plan and quiz... Please wait."):
                response = model.generate_content(prompt)
                st.success("Lesson Plan & Quiz Generated Successfully!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
