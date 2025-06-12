
import streamlit as st
import re
import os
import argparse

st.set_page_config(page_title="LLM Training Quiz", layout="centered")
st.title("🧠 Module Quiz: Interactive Web Version")

def parse_quiz_md(md_path):
    with open(md_path, "r") as f:
        content = f.read()

    questions = []
    blocks = content.split("---")
    for block in blocks:
        lines = [line.strip() for line in block.strip().split("\n") if line.strip()]
        if not lines:
            continue
        qtext = []
        options = []
        correct = None
        for line in lines:
            if line.startswith("**Correct Answer:**"):
                correct = line.split("**Correct Answer:**")[-1].strip()
            elif re.match(r"^[A-D]\. ", line):
                options.append(line)
            else:
                qtext.append(line)
        if options:
            questions.append({
                "question": " ".join(qtext),
                "options": options,
                "answer": correct
            })
    return questions

# Read CLI args
parser = argparse.ArgumentParser()
parser.add_argument("--module", type=str, help="Module identifier like 'module_08'")
args = parser.parse_args()

quiz_path = None
if args.module:
    module_path = f"modules/{args.module.replace('_', ' ', 1).replace('.', '').replace('module ', '').strip()}*/QUIZ.md"
    import glob
    matches = glob.glob(module_path)
    if matches:
        quiz_path = matches[0]

if not quiz_path:
    uploaded = st.file_uploader("Upload a QUIZ.md file to begin", type="md")
    if uploaded:
        with open("quiz_temp.md", "wb") as f:
            f.write(uploaded.read())
        quiz_path = "quiz_temp.md"

if quiz_path and os.path.exists(quiz_path):
    st.success(f"Loaded quiz: {quiz_path}")
    questions = parse_quiz_md(quiz_path)
    score = 0

    for i, q in enumerate(questions):
        st.markdown(f"### Q{i+1}: {q['question']}")
        selected = st.radio("Choose an answer:", q["options"], key=f"q_{i}")
        if selected.startswith(q["answer"]):
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Incorrect. Correct answer: {q['answer']}")
        st.markdown("---")

    st.markdown(f"## 🏁 Final Score: {score} / {len(questions)}")
else:
    st.info("Awaiting quiz upload or a matching CLI module path.")
