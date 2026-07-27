# 🎓 EduPlan AI Ultimate

All-in-One AI Teaching Suite for Educators — built with [Streamlit](https://streamlit.io) and Google's [Gemini API](https://ai.google.dev).

**Author:** Sadia Iqbal

Enter a subject, topic, grade level, and teaching style, and EduPlan AI generates a complete, ready-to-use lesson package: learning objectives, materials, key vocabulary, a step-by-step lesson procedure, a quiz with answer key, and optional homework and grading rubric — in English, Urdu, or Roman Urdu.

**Live app:** https://eduplan-ai-4qu43aerfc3p4hgmvdaxua.streamlit.app/

---

## ✨ Features

- 📋 Generates a full lesson plan tailored to subject, topic, grade (Grade 1 – High School), duration, and teaching style
- 🌐 Output in **English**, **Urdu (Urdu script)**, or **Roman Urdu**
- ➕ Optional extras: homework assignment, evaluation/grading rubric
- 🤖 Choice of Gemini model in the sidebar, so the app keeps working even if Google retires a model
- 📥 Download the generated plan as a `.txt` file
- 🔑 Bring your own free Gemini API key — nothing is stored on the server

---

## 🚀 Getting Started

### 1. Get a Gemini API key

Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey), sign in with a Google account, and create a free API key.

### 2. Run it online (no setup)

Just open the [live app](https://eduplan-ai-4qu43aerfc3p4hgmvdaxua.streamlit.app/) and paste your API key into the sidebar.

### 3. Run it locally

```bash
git clone https://github.com/sadianice80/eduplan-ai.git
cd eduplan-ai
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL Streamlit prints (usually `http://localhost:8501`).

---

## 🤖 AI Feature

The core AI feature is **automated lesson-package generation**. When a teacher fills in the Subject, Topic, Grade Level, Duration, and Teaching Style (plus optional Homework/Rubric toggles and a language choice), the app sends a structured prompt to Google's Gemini model and returns a ready-to-teach lesson package.

**The exact prompt sent to the model (built dynamically from the form inputs):**

```
Act as an expert educational consultant and teacher trainer. Create a comprehensive, well-formatted teaching suite in {language} for:
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
5. Assessment / 5-Question Quiz with Answer Key
- Creative Homework Assignment for students   (only if "Include Homework" is checked)
- Simple Evaluation/Grading Rubric for assessing student work   (only if "Include Evaluation Rubric" is checked)
```

`{language}`, `{subject}`, `{topic}`, `{grade}`, `{duration}`, and `{style}` are filled in from the user's form inputs before the prompt is sent. The two extra bullet points are appended dynamically depending on which checkboxes are ticked. This means the AI isn't just answering a generic question — it's following a specific pedagogical structure (Bloom's Taxonomy objectives, a 5-part lesson procedure, a quiz with an answer key) on every single generation, which is what makes the output consistently usable in a real classroom rather than a random essay.

---

## 🧰 Tools, Services & Models Used

| Category | What was used |
|---|---|
| Language | Python |
| Web app framework | [Streamlit](https://streamlit.io) |
| AI model / provider | Google **Gemini API** (model selectable in-app; default `gemini-flash-latest`) |
| AI SDK | `google-generativeai` Python package |
| Hosting / deployment | Streamlit Community Cloud |
| Version control | Git & GitHub |

---

## 🛠️ How to use

1. Paste your Gemini API key in the sidebar.
2. Pick an output language and a Gemini model.
3. (Optional) Toggle "Include Homework" and "Include Evaluation Rubric."
4. Fill in Subject, Topic, Grade Level, Duration, and Teaching Style.
5. Click **✨ Generate Complete Teaching Suite**.
6. Review the result and, if you'd like a copy, click **📥 Download Plan (.TXT)**.

---

## 📸 Screenshots

<!-- Add your screenshots here before submitting — the assignment requires 3 or more.
     1. Take screenshots of the app (form filled in, generated output, sidebar settings).
     2. Put the image files in a folder called `screenshots/` in this repo.
     3. Replace the paths below with your actual filenames. -->

![Form screen](screenshots/form.png)
![Generated lesson plan](screenshots/output.png)
![Sidebar settings](screenshots/sidebar.png)

---

## 📦 Requirements

```
streamlit
google-generativeai
```

(see `requirements.txt`)

---

## 🧯 Troubleshooting

**"Model not found" / 404 error**
Google periodically retires older Gemini models. Open the sidebar and pick a different model from the **Model** dropdown — no code changes needed. `gemini-flash-latest` is the safest default since Google keeps it pointed at a current model.

**App shows "This app has gone to sleep"**
Free Streamlit Cloud apps sleep after a period of inactivity. Click the wake-up button and wait ~30 seconds.

**"Please enter your Google Gemini API Key" error**
You need to paste a valid key into the sidebar before generating — the app doesn't ship with one.

---

## 📄 License

Add a license of your choice here (e.g. MIT) if you plan to share or open-source this project.

---

## 🙋 Support

Built for educators. For issues or feature requests, open an issue on this repository.
##  code
import re
import streamlit as st
import google.generativeai as genai

# ------------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------------
st.set_page_config(
    page_title="EduPlan AI Ultimate",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 EduPlan AI Ultimate")
st.caption("All-in-One AI Teaching Suite for Educators")

# ------------------------------------------------------------------
# Sidebar: Credentials & Settings
# ------------------------------------------------------------------
st.sidebar.header("🔑 Credentials")
api_key = st.sidebar.text_input(
    "Google Gemini API Key:",
    type="password",
    help="Enter your Gemini API key here"
)

st.sidebar.markdown("---")
st.sidebar.subheader("🌐 Output Settings")
language = st.sidebar.selectbox(
    "Language / زبان",
    ["English", "Urdu (in Urdu Script)", "Roman Urdu"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("➕ Additional Extras")
inc_homework = st.sidebar.checkbox("Include Homework", value=True)
inc_rubric = st.sidebar.checkbox("Include Evaluation Rubric", value=True)

# ------------------------------------------------------------------
# Main Form
# ------------------------------------------------------------------
st.subheader("📋 Lesson Details")

col1, col2 = st.columns(2)
with col1:
    subject = st.text_input("Subject", placeholder="e.g. Science, Mathematics")
with col2:
    topic = st.text_input("Topic", placeholder="e.g. Photosynthesis, Algebra")

col3, col4, col5 = st.columns(3)
with col3:
    grade = st.selectbox(
        "Grade Level",
        ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5",
         "Grade 6", "Grade 7", "Grade 8", "High School"]
    )
with col4:
    duration = st.number_input("Duration (Mins)", min_value=10, max_value=180, value=40)
with col5:
    style = st.selectbox(
        "Teaching Style",
        ["Interactive", "Lecture", "Group Work", "Inquiry-Based"]
    )

st.markdown("---")


def build_prompt() -> str:
    extras = ""
    if inc_homework:
        extras += "\n- Creative Homework Assignment for students"
    if inc_rubric:
        extras += "\n- Simple Evaluation/Grading Rubric for assessing student work"

    return f"""Act as an expert educational consultant and teacher trainer. Create a comprehensive, well-formatted teaching suite in {language} for:
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
5. Assessment / 5-Question Quiz with Answer Key{extras}"""


def safe_filename(subject: str, topic: str) -> str:
    """Build a filesystem-safe filename from user-provided text."""
    raw = f"{subject}_{topic}_EduPlan".strip()
    cleaned = re.sub(r"[^A-Za-z0-9_\-]+", "_", raw)
    return f"{cleaned}.txt"


# Persist generated content across reruns (e.g. when the download button is clicked)
if "generated_plan" not in st.session_state:
    st.session_state.generated_plan = None
if "generated_filename" not in st.session_state:
    st.session_state.generated_filename = None

# ------------------------------------------------------------------
# Generate button
# ------------------------------------------------------------------
if st.button("✨ Generate Complete Teaching Suite", type="primary", use_container_width=True):
    if not api_key:
        st.error("Please enter your Google Gemini API Key in the sidebar!")
    elif not subject or not topic:
        st.warning("Please enter both Subject and Topic.")
    else:
        prompt = build_prompt()
        with st.spinner("⏳ EduPlan AI is generating your lesson plan, quiz, homework, and rubric..."):
            try:
                genai.configure(api_key=api_key, transport="rest")
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)

                if response.text:
                    st.session_state.generated_plan = response.text
                    st.session_state.generated_filename = safe_filename(subject, topic)
                    st.success("🎉 Teaching Suite Generated Successfully!")
                else:
                    st.session_state.generated_plan = None
                    st.error("No response received from the model. Please try again.")
            except Exception as e:
                st.session_state.generated_plan = None
                st.error(f"API Error: {e}")

# ------------------------------------------------------------------
# Display results (persists across reruns, e.g. after clicking Download)
# ------------------------------------------------------------------
if st.session_state.generated_plan:
    st.markdown("---")
    st.markdown("### 📄 Generated Plan")
    st.markdown(st.session_state.generated_plan)

    st.markdown("---")
    st.download_button(
        label="📥 Download Plan (.TXT)",
        data=st.session_state.generated_plan,
        file_name=st.session_state.generated_filename,
        mime="text/plain"
    )

