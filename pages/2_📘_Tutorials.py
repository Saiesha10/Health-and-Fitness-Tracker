import streamlit as st
import requests
from PIL import Image

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Tutorials", page_icon="📽️", layout="wide")

# ---- CUSTOM STYLES ----
st.markdown("""
    <style>
        /* App Background */
        [data-testid="stAppViewContainer"] {
            background-color: #f5f5dc; /* Beige */
            font-family: 'Poppins', sans-serif;
        }

        /* Header transparency */
        [data-testid="stHeader"] {
            background: rgba(0,0,0,0);
        }

        /* Typography */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Raleway', sans-serif;
            color: #2c2c2c;
        }

        /* Default text color */
        p, div, span, .markdown-text-container {
            color: #333333;
            font-size: 16px;
        }

        /* Layout Padding */
        div.block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 3rem;
            padding-right: 3rem;
        }

        /* Style Images & GIFs */
        img, .stImage img {
            border: 3px solid #ddd;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        img:hover, .stImage img:hover {
            transform: scale(1.03);
            box-shadow: 0 14px 30px rgba(0, 0, 0, 0.2);
            border-color: #04AA6D;
        }

        /* Sidebar dropdown styling */
        .css-1cpxqw2 {
            color: #2c2c2c !important;
        }
    </style>
""", unsafe_allow_html=True)


# ---- IMAGES ----
img1 = Image.open("./images/dumbbell.webp")
img2 = Image.open("./images/squats.jpg")
img3 = Image.open("./images/pushups.jpeg")
img4 = Image.open("./images/shoulder.jpeg")

# ---- SIDEBAR ----
app_mode = st.sidebar.selectbox("Choose the tutorial", ["About", "Bicep Curls", "Squats", "Pushups", "Shoulder press"])

# ---- ABOUT SECTION ----
if app_mode == "About":
    st.title("💪 Video Tutorials")
    st.write("Browse essential fitness exercises with visual guidance.")

    tutorials = [
        ("Bicep Curls", img1, "https://youtu.be/ykJmrZ5v0Oo",
         "Get armed with knowledge! Watch this bicep curl tutorial and unlock the secret to sleeve-busting strength!"),

        ("Squats", img2, "https://youtu.be/YaXPRqUwItQ",
         "Get lower, get stronger! Dive into this squat tutorial and unlock the power of a rock-solid foundation!"),

        ("Pushups", img3, "https://youtu.be/IODxDxX7oi4",
         "Push your limits, pump up your power! Join us for this push-up tutorial and unleash your inner strength!"),

        ("Shoulder press", img4, "https://youtu.be/qEwKCR5JCog",
         "Elevate your strength, shoulder to shoulder! Don't miss this shoulder press tutorial to reach new heights of power!"),
    ]

    for title, img, link, desc in tutorials:
        with st.container():
            image_col, text_col = st.columns((1, 2))
            with image_col:
                st.image(img, width=325)
            with text_col:
                st.subheader(title)
                st.write(desc)
                st.markdown(f"[▶ Watch Video]({link})")

# ---- INDIVIDUAL TUTORIAL SECTIONS ----
elif app_mode == "Bicep Curls":
    st.header("💪 Bicep Curls")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - Stand with a dumbbell in each hand, elbows close to torso, palms facing forward.  
        - Curl weights while keeping upper arms stationary.  
        - Raise until dumbbells are at shoulder height, squeeze biceps.  
        - Slowly return to starting position.  
        - Repeat with control and proper posture.
        """)
    with col2:
        st.image("./gif/bicep.gif", width=300)

elif app_mode == "Squats":
    st.header("🏋️‍♀️ Squats")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - Stand with feet slightly wider than shoulder-width apart.  
        - Engage your core, keep back straight.  
        - Lower your hips as if sitting back into a chair.  
        - Thighs parallel to the ground, then push back up.  
        - Keep chest up, breathe properly, and maintain good form.
        """)
    with col2:
        st.image("./gif/squats.gif", width=300)

elif app_mode == "Pushups":
    st.header("🙌 Pushups")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - Start in high plank, core engaged.  
        - Lower body until chest grazes floor.  
        - Keep elbows close, push back up.  
        - Modify with knees or wall pushups if needed.  
        - Focus on proper form and steady reps.
        """)
    with col2:
        st.image("./gif/pushups.gif", width=300)

elif app_mode == "Shoulder press":
    st.header("🧍 Shoulder Press")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - Stand with dumbbells at shoulder height, palms forward.  
        - Press upwards until arms are extended overhead.  
        - Lower with control back to start.  
        - Keep head still and posture aligned.  
        - Use manageable weight and focus on stability.
        """)
    with col2:
        st.image("./gif/shoulder.gif", width=300)
