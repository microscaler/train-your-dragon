import streamlit as st
import json
from pathlib import Path
import re

# Load module index
@st.cache_data
def load_modules():
    with open("module_index.json") as f:
        return json.load(f)

modules = load_modules()

# Sidebar: module list (no dropdown)
st.sidebar.title("📘 Train Your Dragon")

# Ensure selected_module is initialized
if "selected_module" not in st.session_state:
    st.session_state.selected_module = modules[0]["number"]

# Sidebar layout
st.sidebar.title("📘 Train Your Dragon")

module_labels = [f"{m['number']} – {m['title']}" for m in modules]
default_index = next(i for i, m in enumerate(modules) if m["number"] == st.session_state.selected_module)

selected_label = st.sidebar.radio("Select Module:", module_labels, index=default_index, label_visibility="collapsed")

# Update session state on change
selected_module = next(m for m in modules if f"{m['number']} – {m['title']}" == selected_label)
st.session_state.selected_module = selected_module["number"]

# Now resolve module info
module_number = selected_module["number"]
slug = selected_module["slug"]



# Content path
base = Path(f"../modules/{module_number}_{slug.replace('-', '_')}")
readme = base / "README.md"
slides = base / "SLIDES.md"
quiz = base / "QUIZ.md"
exercises = base / "EXERCISES.md"
lab = base / "labs/jupyter_lab.ipynb"

# Display layout
st.title(f"Module {module_number} – {slug.replace('_', ' ').title()}")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
  "🧭 Overview", "🎓 Slides", "🧪 Exercises", "📝 Quiz", "📓 Notebook", "🧠 Final Exam"
])


with tab1:
    if readme.exists():
        st.markdown(readme.read_text())
    else:
        st.info("README.md not found.")

import re

with tab2:
    if slides.exists():
        raw = slides.read_text()
        slides_md = re.split(r'(?m)^---$', raw)
        for i, slide in enumerate(slides_md, 1):
            cleaned = slide.strip()

            if not cleaned:
                continue

            # Remove deck header on first slide
            if i == 1:
                cleaned = re.sub(r"#\s+🎓.*", "", cleaned)

            # ❗ Corrected regex: match lines starting with optional `#` and "Slide N:"
            cleaned = re.sub(r"(?m)^#{0,2}\s*Slide \d+:.*$", "", cleaned)

            cleaned = cleaned.strip()

            if cleaned:
                st.markdown(f"---\n\n### 📖 Slide {i}\n\n{cleaned}")
    else:
        st.info("SLIDES.md not found.")



with tab3:
    if exercises.exists():
        st.markdown(exercises.read_text())
    else:
        st.info("EXERCISES.md not found.")

with tab4:
    if quiz.exists():
        st.markdown(quiz.read_text())
    else:
        st.info("QUIZ.md not found.")

with tab5:
    st.info("Notebook preview coming soon. For now, open it in your IDE.")
    if lab.exists():
        st.code(str(lab), language='bash')

with tab6:
    import requests
    if "exam_index" not in st.session_state:
        st.session_state.exam_index = 0
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "user_id" not in st.session_state:
        st.session_state.user_id = st.text_input("Enter your User ID")

    user_id = st.session_state.user_id

    API_BASE = "http://localhost:8080/api"

    def get_question(index):
        r = requests.get(f"{API_BASE}/question/{user_id}/{index}")
        if r.status_code == 200:
            return r.json()
        return None

    if user_id:
        question = get_question(st.session_state.exam_index)
        if question:
            st.subheader(f"Question {st.session_state.exam_index + 1}")
            st.write(question["text"])
            choice = st.radio("Select your answer:", question["options"], key=f"q{st.session_state.exam_index}")

            if st.button("Submit Answer"):
                st.session_state.answers[st.session_state.exam_index] = choice
                requests.post(f"{API_BASE}/answer", json={
                    "user_id": user_id,
                    "question_id": question["question_id"],
                    "answer": choice
                })
                st.session_state.exam_index += 1

            if st.session_state.exam_index >= 90:
                st.success("🎓 Exam completed!")
                st.balloons()
        else:
            st.error("Unable to load question.")
    else:
        st.info("Please enter your User ID to begin.")
