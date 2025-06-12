import streamlit as st
import json
from pathlib import Path

# Load module index
@st.cache_data
def load_modules():
    with open("module_index.json") as f:
        return json.load(f)

modules = load_modules()

# Sidebar: module selection
st.sidebar.title("📘 Train Your Dragon")
selected = st.sidebar.selectbox("Choose a module", [f"{m['number']} – {m['title']}" for m in modules])
module_number = selected.split("–")[0].strip()
slug = next((m["slug"] for m in modules if m["number"] == module_number), None)

# Content path
base = Path(f"../modules/{module_number}_{slug.replace('-', '_')}")
readme = base / "README.md"
slides = base / "SLIDES.md"
quiz = base / "QUIZ.md"
exercises = base / "EXERCISES.md"
lab = base / "labs/jupyter_lab.ipynb"

# Display layout
st.title(f"Module {module_number} – {slug.replace('_', ' ').title()}")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🧭 Overview", "🎓 Slides", "🧪 Exercises", "📝 Quiz", "📓 Notebook"])

with tab1:
    if readme.exists():
        st.markdown(readme.read_text())
    else:
        st.info("README.md not found.")

with tab2:
    if slides.exists():
        slides_md = slides.read_text().split("---")
        for i, slide in enumerate(slides_md, 1):
            st.markdown(f"### Slide {i}\n{slide}")
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
