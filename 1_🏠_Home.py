import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Health and Fitness Trainer", page_icon="💪", layout="wide")

# ---- CUSTOM STYLING ----
st.markdown("""
    <style>
        /* Set the full app background to soft beige */
        [data-testid="stAppViewContainer"] {
            background-color: #f5f5dc; /* beige */
            font-family: 'Poppins', sans-serif;
        }

        /* Header transparent */
        [data-testid="stHeader"] {
            background: rgba(0,0,0,0);
        }

        /* Improve section layout */
        div.block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 3rem;
            padding-right: 3rem;
        }

        /* Typography improvements */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Raleway', sans-serif;
            color: #2c2c2c;
        }

        /* Paragraph and default text */
        p, div, span {
            color: #333333;
        }

        /* Image and Lottie visuals styling */
        img, .stImage img, .stLottie {
            border: 3px solid #ddd;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        img:hover, .stImage img:hover, .stLottie:hover {
            transform: scale(1.03);
            box-shadow: 0 14px 30px rgba(0, 0, 0, 0.2);
            border-color: #04AA6D;
        }
    </style>
""", unsafe_allow_html=True)




# ---- HELPER FUNCTION ----
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# ---- LOAD ANIMATIONS ----
lottie_fitness = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_FYx0Ph.json")
lottie_music = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_ikk4jhps.json")
lottie_podcast = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_JjpNLdaKYX.json")

# ---- IMAGES ----
img_banner = Image.open("images/home.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.title("🏃‍♀️ Health and Fitness Tracker")
    st.write("Welcome to your personalized fitness journey! Let's get stronger and healthier together.")
    

# ---- ABOUT US ----
with st.container():
    st.markdown("---")
    st.header("🏋️ About Us")
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        We bring fitness to your fingertips.

        🔸 AI-personalized workouts  
        🔸 Work out anytime, anywhere  
        🔸 Affordable and smart fitness coaching

        Whether you're starting fresh or optimizing your gains, we've got your back.
        """)
    with col2:
        st_lottie(lottie_fitness, height=300)

# ---- MUSIC SECTION ----
with st.container():
    st.markdown("---")
    st.header("🎶 Workout Beats")
    col1, col2 = st.columns([1, 2])
    with col1:
        st_lottie(lottie_music, height=250)
    with col2:
        st.subheader("Power your pump with curated playlists 🎧")
        st.markdown("[Listen on Spotify](https://open.spotify.com/playlist/6N0Vl77EzPm13GIOlEkoJn?si=9207b7744d094bd3)")

# ---- PODCAST SECTION ----
with st.container():
    st.markdown("---")
    st.header("🎙️ Fitness Podcasts")
    col1, col2 = st.columns([1, 2])
    with col1:
        st_lottie(lottie_podcast, height=250)
    with col2:
        st.subheader("Stay inspired while you train 💬")
        st.markdown("[Tune in on Spotify](https://open.spotify.com/playlist/09Ig7KfohF5WmU9RhbDBjs?si=jyZ79y3wQgezrEDHim0NvQ)")
