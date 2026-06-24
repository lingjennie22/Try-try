import streamlit as st
import random
import textwrap

# 1. Page Configuration & Theme
st.set_page_config(
    page_title="Emotion Explorer!",
    page_icon="🧩",
    layout="centered"
)

# Custom colorful styling for 11-year-olds
custom_css = textwrap.dedent("""
    <style>
    .main-title { 
        font-size: 40px; 
        font-weight: bold; 
        color: #4A90E2; 
        text-align: center; 
    }
    .score-box { 
        background-color: #F0F2F6; 
        padding: 10px; 
        border-radius: 10px; 
        text-align: center; 
        font-size: 20px; 
        font-weight: bold; 
    }
    </style>
""")

st.markdown(custom_css, unsafe_html=True)

# 2. Game Data (Scenarios, Options, Correct Answers, and Explanations)
SCENARIOS = [
    {
        "id": 1,
        "situation": "Your best friend starts playing with someone else at recess and forgets to invite you.",
        "options": ["Jealous/Left Out", "Excited", "Scared", "Guilty"],
        "correct": "Jealous/Left Out",
        "explanation": "It's totally normal to feel left out when a friend plays with someone else! A good trick is to take a deep breath and gently ask if you can join in, or find another fun activity to do."
    },
    {
        "id": 2,
        "situation": "You have a huge math test tomorrow and you feel a tight knot in your stomach.",
        "options": ["Angry", "Anxious/Nervous", "Happy", "Bored"],
        "correct": "Anxious/Nervous",
        "explanation": "That knot in your stomach is anxiety. When you feel this way, try the '5-4-3-2-1' grounding method: notice 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste."
    },
    {
        "id": 3,
        "situation": "Your younger sibling accidentally rips a drawing you spent two hours working on.",
        "options": ["Sad", "Frustrated/Angry", "Surprised", "Proud"],
        "correct": "Frustrated/Angry",
        "explanation": "Feeling angry when your hard work is ruined makes sense! Before reacting, try 'box breathing': breathe in for 4 seconds, hold for 4, exhale for 4, and hold for 4. It resets your brain!"
    },
    {
        "id": 4,
        "situation": "You finally figured out how to solve a really hard coding puzzle all by yourself.",
        "options": ["Proud", "Embarrassed", "Anxious", "Confused"],
        "correct": "Proud",
        "explanation": "Heck yeah! Feeling proud rewards your brain for perseverance. Celebrate your hard work—you earned it!"
    },
    {
        "id": 5,
        "situation": "You dropped your lunch tray in the crowded cafeteria and everyone looked your way.",
        "options": ["Excited", "Angry", "Embarrassed", "Peaceful"],
        "correct": "Embarrassed",
        "explanation": "Dropping things happens to everyone! If you feel embarrassed, remember: people usually forget about it in 5 minutes. Laughing it off or taking a slow breath helps the heat fade away."
    }
]

# 3. Initialize Session State Variables
if "score" not in st.session_state:
    st.session_state.score = 0
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(SCENARIOS)
if "answered" not in st.session_state:
    st.session_state.answered = False
if "feedback" not in st.session_state:
    st.session_state.feedback = None

# Function to get a new random question (different from the current one if possible)
def next_question():
    st.session_state.answered = False
    st.session_state.feedback = None
    remaining_
