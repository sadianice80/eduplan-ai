# 🎓 EduPlan AI Ultimate

All-in-One AI Teaching Suite for Educators — built with [Streamlit](https://streamlit.io) and Google's [Gemini API](https://ai.google.dev).

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

## 🛠️ How to use

1. Paste your Gemini API key in the sidebar.
2. Pick an output language and a Gemini model.
3. (Optional) Toggle "Include Homework" and "Include Evaluation Rubric."
4. Fill in Subject, Topic, Grade Level, Duration, and Teaching Style.
5. Click **✨ Generate Complete Teaching Suite**.
6. Review the result and, if you'd like a copy, click **📥 Download Plan (.TXT)**.

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
