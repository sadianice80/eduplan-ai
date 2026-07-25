
   import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(
    page_title="EduPlan AI Ultimate",
    page_icon="🎓",
    layout="centered"
)

# Title & Subtitle
st.title("🎓 EduPlan AI Ultimate")
st.caption("All-in-One AI Teaching Suite for Educators")

# Sidebar for Setup & Credentials
st.sidebar.header("🔑 Credentials")
api_key = st.sidebar.text_input("Google Gemini API Key:", type="password", help="Enter your Gemini API key here")

st.sidebar.markdown("---")
st.sidebar.subheader("🌐 Output Settings")
language = st.sidebar.selectbox("Language / زبان", ["English", "Urdu (in Urdu Script)", "Roman Urdu"])

st.sidebar.markdown("---")
st.sidebar.subheader("➕ Additional Extras")
inc_homework = st.sidebar.checkbox("Include Homework", value=True)
inc_rubric = st.sidebar.checkbox("Include Evaluation Rubric", value=True)

# Main Form Controls
st.subheader("📋 Lesson Details")

col1, col2 = st.columns(2)
with col1:
    subject = st.text_input("Subject", placeholder="e.g. Science, Mathematics")
with col2:
    topic = st.text_input("Topic", placeholder="e.g. Photosynthesis, Algebra")

col3, col4, col5 = st.columns(3)
with col3:
    grade = st.selectbox("Grade Level", ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "High School"])
with col4:
    duration = st.number_input("Duration (Mins)", min_value=10, max_value=180, value=40)
with col5:
    style = st.selectbox("Teaching Style", ["Interactive", "Lecture", "Group Work", "Inquiry-Based"])

st.markdown("---")

# Submit Button
if st.button("✨ Generate Complete Teaching Suite", type="primary", use_container_width=True):
    if not api_key:
        st.error("Please enter your Google Gemini API Key in the sidebar!")
    elif not subject or not topic:
        st.warning("Please enter both Subject and Topic.")
    else:
        # Construct Prompt
        extras = ""
        if inc_homework:
            extras += "\n- Creative Homework Assignment for students"
        if inc_rubric:
            extras += "\n- Simple Evaluation/Grading Rubric for assessing student work"

        prompt = f"""Act as an expert educational consultant and teacher trainer. Create a comprehensive, well-formatted teaching suite in {language} for:
Subject: {subject}
Topic: {topic}
Grade Level: {grade}
Duration: {duration} minutes
Teaching Approach: {style}

Structure the output with clear bold headers:
1. Learning Objectives (using Bloom's Taxonomy verbs)
2. Required Teaching Materials
3. Key Vocabulary
4. Step-by-Step Lesson Procedure (Hook/Intro, Direct Instruction, Guided Practice, Independent Activity, Conclusion)
5. Assessment / 5-Question Quiz with Answer Key {extras}"""

        with st.spinner("⏳ EduPlan AI is generating your lesson plan, quiz, homework, and rubric..."):
            try:
                genai.configure(api_key=api_key)
                
                # Using Gemini 1.5 Flash for high speed and reliable output
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt)

                if response.text:
                    st.success("🎉 Teaching Suite Generated Successfully!")
                    
                    # Display Results
                    st.markdown("### 📄 Generated Plan")
                    st.write(response.text)
                    
                    st.markdown("---")
                    
                    # Download Option
                    file_filename = f"{subject}_{topic}_EduPlan.txt"
                    st.download_button(
                        label="📥 Download Plan (.TXT)",
                        data=response.text,
                        file_name=file_filename,
                        mime="text/plain"
                    )
                else:
                    st.error("No response received from the model. Please try again.")

            except Exception as e:
                st.error(f"API Error: {e}")
