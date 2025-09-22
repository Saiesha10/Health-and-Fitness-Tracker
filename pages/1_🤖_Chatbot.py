import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

# Load .env only once
if "loaded_dotenv" not in st.session_state:
    load_dotenv()
    st.session_state.loaded_dotenv = True

# --- CONFIGURE GEMINI ---
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
    "temperature": 1.1,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 1024,  # Reduced for speed
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # You can try gemini-1.5-pro too
    generation_config=generation_config,
)

# --- SYSTEM PROMPT ---
BASE_PROMPT = """
You're ChadFlex — the ultimate gym bro + nutrition buddy. Friendly, fun, and always hyped. 
You give awesome workout plans, diet tips, motivation, and recovery help. 
You're not a doctor — so just drop that once casually *if needed*, and don't overdo it.

When users ask about illnesses, injuries, or health conditions (like diabetes or asthma), 
be smart: adjust recommendations safely, give helpful advice, and casually remind them to check with a pro. 
Keep your tone chill, confident, and gym-bro supportive — you're here to help, not lecture. 
Always sound like a fit, fun, confident gym buddy. Keep replies short, direct, and upbeat.

Example responses:
- “Let’s crush it, bro!”
- “Respect for showing up even with [issue]. Let's train smart.”
- “Not a doc, but here’s what I’d do — and you might wanna double-check with a pro.”

Stick to fitness, food, gains, recovery, and mindset. Never break character.
"""

# --- STREAMLIT SETUP ---
st.set_page_config(page_title="ChadFlex Gym Bro Bot", page_icon="💪", layout="wide")

st.markdown(
    "<h1 style='color:#b45309; font-size: 40px;'>💪 ChadFlex: Your Gym Bro + Diet Coach</h1>",
    unsafe_allow_html=True,
)

# --- SESSION STATE ---
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.messages = [{"role": "system", "content": BASE_PROMPT}]

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# --- INPUT HANDLER ---
def handle_input():
    user_message = st.session_state.user_input.strip()
    if user_message == "":
        return
    st.session_state.messages.append({"role": "user", "content": user_message})
    with st.spinner("ChadFlex is thinking, bro..."):
        response = st.session_state.chat_session.send_message(user_message)
        reply = response.text
        st.session_state.messages.append({"role": "system", "content": reply})
    st.session_state.user_input = ""  # Clear input

# --- RESET BUTTON ---
if st.button("Reset Chat 🔄"):
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.messages = [{"role": "system", "content": BASE_PROMPT}]
    st.session_state.user_input = ""

# --- CHAT DISPLAY ---
st.markdown("<h3 style='color:#111;'>Chat 💬</h3>", unsafe_allow_html=True)

def show_messages():
    chat_html = ""
    for msg in st.session_state["messages"][-30:]:  # Only last 30 messages
        if msg["role"] == "user":
            chat_html += f"<p style='color:#1e40af; font-size:17px;'><b>You:</b> {msg['content']}</p>"
        else:
            chat_html += f"<p style='color:#b45309; font-size:17px;'><b>ChadFlex:</b> {msg['content']}</p>"
    st.markdown(chat_html, unsafe_allow_html=True)

show_messages()

# --- INPUT BOX ---
st.markdown("<label style='color:#111; font-size:16px;'>Type your message, bro!</label>", unsafe_allow_html=True)
st.text_input(
    label="Chat input",
    label_visibility="collapsed",  # Fixes accessibility warning
    key="user_input",
    on_change=handle_input
)

# --- SCROLL TO BOTTOM ---
st.markdown(
    """
    <script>
        const chatContainer = window.parent.document.querySelector('.main');
        if (chatContainer) {
            setTimeout(() => {
                chatContainer.scrollTo({top: chatContainer.scrollHeight, behavior: 'smooth'});
            }, 100);
        }
    </script>
    """,
    unsafe_allow_html=True
)

# --- STYLING ---
st.markdown(
    """
    <style>
    .stTextInput > div > div > input {
        background-color: #111827;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        border: 1px solid #b45309;
    }
    button[kind="primary"] {
        background-color: #b45309 !important;
        color: white !important;
        border-radius: 8px;
        font-weight: bold;
    }
    body, [data-testid="stAppViewContainer"] {
        background-color: #f5f5dc !important;  /* Beige */
    }
    ::placeholder {
        color: #9ca3af;
    }
    </style>
    """,
    unsafe_allow_html=True
)
