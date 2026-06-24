import streamlit as st
import random

st.set_page_config(page_title="Emotion Match Game", page_icon="😊")

# Questions database
questions = [
    {
        "scenario": "Your best friend ignores you during recess.",
        "options": ["Happy", "Sad", "Angry", "Excited"],
        "answer": "Sad",
        "explanation": "You may feel sad because being ignored can feel hurtful."
    },
    {
        "scenario": "You studied hard and got full marks on a test.",
        "options": ["Angry", "Excited", "Scared", "Confused"],
        "answer": "Excited",
        "explanation": "You may feel excited and proud after doing well."
    },
    {
        "scenario": "Someone cuts in front of you in line.",
        "options": ["Angry", "Happy", "Sleepy", "Calm"],
        "answer": "Angry",
        "explanation": "It can feel unfair when someone cuts the queue."
    },
    {
        "scenario": "You are about to perform on stage for the first time.",
        "options": ["Scared", "Bored", "Happy", "Sleepy"],
        "answer": "Scared",
        "explanation": "New experiences can feel scary or nerve-wracking."
    },
    {
        "scenario": "Your family surprises you with your favorite meal.",
        "options": ["Happy", "Angry", "Scared", "Confused"],
        "answer": "Happy",
        "explanation": "Pleasant surprises often make us feel happy."
    },
    {
        "scenario": "You cannot solve a difficult math problem.",
        "options": ["Confused", "Excited", "Happy", "Calm"],
        "answer": "Confused",
        "explanation": "It's normal to feel confused when something is difficult."
    }
]

# Session state
if "score" not in st.session_state:
    st.session_state.score = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = random.randint(0, len(questions) - 1)

if "answered" not in st.session_state:
    st.session_state.answered = False

st.title("🎮 Emotion Match Game")
st.write("Match the emotion to the situation!")

question = questions[st.session_state.question_index]

st.subheader("Situation")
st.info(question["scenario"])

choice = st.radio("How would someone feel?", question["options"])

if st.button("Submit Answer"):
    st.session_state.answered = True

    if choice == question["answer"]:
        st.success("✅ Correct!")
        st.session_state.score += 1
    else:
        st.error(f"❌ Not quite. The correct answer is {question['answer']}.")

    st.write(f"💡 Explanation: {question['explanation']}")

st.write(f"🏆 Score: {st.session_state.score}")

def next_question():
    st.session_state.question_index = random.randint(0, len(questions) - 1)
    st.session_state.answered = False

if st.button("Next Question"):
    next_question()
    st.rerun()

if st.button("Restart Game"):
    st.session_state.score = 0
    st.session_state.question_index = random.randint(0, len(questions) - 1)
    st.session_state.answered = False
    st.rerun()

st.markdown("---")
st.write("### Emotional Regulation Tip 🌈")
st.write("When you feel a strong emotion, try this:")
st.write("1. Stop")
st.write("2. Take 3 deep breaths")
st.write("3. Name your emotion")
st.write("4. Choose a calm action")
