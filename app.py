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

# Modern, native way to inject CSS in Streamlit
st.html(custom_css)

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
    remaining_scenarios = [s for s in SCENARIOS if s["id"] != st.session_state.current_question["id"]]
    if remaining_scenarios:
        st.session_state.current_question = random.choice(remaining_scenarios)
    else:
        st.session_state.current_question = random.choice(SCENARIOS)

# 4. App UI Layout
st.markdown("<div class='main-title'>🧩 Emotion Explorer: The Game!</div>", unsafe_html=True)
st.write("Welcome! Read the scenario, match it to the right emotion, and learn cool tricks to manage your feelings!")

st.write("---")

# Display Scoreboard
col1, col2 = st.columns([3, 1])
with col2:
    st.markdown(f"<div class='score-box'>⭐ Score: {st.session_state.score}</div>", unsafe_html=True)

# Display Current Scenario
with col1:
    st.subheader("🕵️‍♂️ The Situation:")
    st.info(st.session_state.current_question["situation"])

# Interactive Choice Form
st.subheader("Choose the matching emotion:")

# Using a form prevents the page from auto-reloading before the user submits
with st.form(key="quiz_form"):
    user_choice = st.radio(
        "How would you most likely feel?", 
        options=st.session_state.current_question["options"],
        index=None, # Starts with no pre-selected option
        placeholder="Select an emotion..."
    )
    submit_button = st.form_submit_button(label="Submit Answer")

# 5. Answer Validation & Logic
if submit_button:
    if user_choice is None:
        st.warning("Please select an option before submitting!")
    elif not st.session_state.answered:
        st.session_state.answered = True
        st.session_state.total_questions += 1
        
        if user_choice == st.session_state.current_question["correct"]:
            st.session_state.score += 1
            st.session_state.feedback = {"type": "success", "msg": "🎉 Correct! Great job identifying that emotion!"}
        else:
            st.session_state.feedback = {"type": "error", "msg": f"❌ Not quite! The closest emotion is **{st.session_state.current_question['correct']}**."}

# Render Feedback and Explanation
if st.session_state.feedback:
    if st.session_state.feedback["type"] == "success":
        st.success(st.session_state.feedback["msg"])
    else:
        st.error(st.session_state.feedback["msg"])
    
    # Simple, kid-friendly coping mechanism breakdown
    st.markdown("### 💡 Regulation Tip:")
    st.write(st.session_state.current_question["explanation"])

# Next Question Button
if st.session_state.answered:
    st.button("Next Scenario ➡️", on_click=next_question)
