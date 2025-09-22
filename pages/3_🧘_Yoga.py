import datetime
import cv2
import os
import time
import numpy as np
import streamlit as st
import mediapipe as mp
from PIL import Image
from playsound import playsound

# ----------------- UI FIXES ------------------
st.set_page_config(page_title="Yoga Trainer", layout="wide")

custom_css = """
    <style>
        /* Make entire app background beige */
        .main, .block-container {
            background-color: #f5f0e1 !important;
        }

        /* Force text color globally */
        html, body, [class*="css"] {
            color: #1a1a1a !important;
        }

        /* Headings */
        h1, h2, h3, h4, h5, h6 {
            color: #111111 !important;
        }

        /* Sidebar text and bg */
        section[data-testid="stSidebar"] {
            background-color: #f5f0e1 !important;
            color: #1a1a1a !important;
        }

        /* Markdown inside any widget container */
        .stMarkdown, .stText, .stTextInput, .stButton {
            color: #1a1a1a !important;
        }

        /* Button tweaks */
        button[kind="primary"] {
            background-color: #6e5849 !important;
            color: white !important;
        }

        button[kind="primary"]:hover {
            background-color: #5c473a !important;
        }

        /* Remove left sidebar double arrow */
        [data-testid="collapsedControl"] {
            display: none !important;
        }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ------------- Helper Functions ----------------
def calculate_angle(a, b, c):
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    return angle

def count_time(time_interval):
    global last_second, counter, pose_number
    now = datetime.datetime.now()
    current_second = int(now.strftime("%S"))
    if current_second != last_second:
        last_second = current_second
        counter += 1
        if counter == time_interval + 1:
            counter = 0
            pose_number += 1
            playsound(r'C:\Users\hp\fitness trainer and health management\gr\health and fitness trainer\models\bell.wav')
            if pose_number == 5:
                pose_number = 1
    return counter, pose_number

# ------------- Globals ----------------
last_second = 0
counter = 0
pose_number = 1

# ------------- Load Assets -------------
img1 = Image.open(r"C:\Users\hp\fitness trainer and health management\gr\health and fitness trainer\models\gif\yoga.gif")
img2 = Image.open(r"C:\Users\hp\fitness trainer and health management\gr\health and fitness trainer\models\images\pranamasana2.png")
img3 = Image.open(r"C:\Users\hp\fitness trainer and health management\gr\health and fitness trainer\models\images\Eka_Pada_Pranamasana.png")
img4 = Image.open(r"C:\Users\hp\fitness trainer and health management\gr\health and fitness trainer\models\images\ardha_chakrasana.webp")
img6 = Image.open(r"C:\Users\hp\fitness trainer and health management\gr\health and fitness trainer\models\images\Utkatasana.png")
img7 = Image.open(r"C:\Users\hp\fitness trainer and health management\gr\health and fitness trainer\models\images\Veerabhadrasan_2.png")

# ------------- MediaPipe -------------
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# ----------- Sidebar Navigation ------------
app_mode = st.sidebar.selectbox("Choose the exercise", ["About", "Track 1", "Track 2"])

# ------------- About -------------
if app_mode == "About":
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("## Welcome to the Yoga Arena 🧘‍♀️")
        st.markdown("Choose the Track you wish to do from the sidebar")
        st.write("### Guidelines:")
        st.markdown("""
        - Provide webcam access.
        - Avoid crowded places.
        - Ensure surroundings are well lit.
        - Keep the camera focused on you for correct form detection.
        """)
    with col2:
        st.image(img1, use_container_width=True)

# ----------- Track 1 UI (Only Pose Guide) -----------
elif app_mode == "Track 1":
    st.markdown("## 🧘 Track 1 - Pose Overview")
    for title, img in zip(
        ["Pranamasana (Prayer Pose)", "Eka Pada Pranamasana", "Ashwa Sanchalanasana"],
        [img2, img3, img4]):
        left, right = st.columns(2)
        with left: st.write(f"### {title}")
        with right: st.image(img, use_container_width=True)
        st.markdown("----")

# ----------- Track 2 (Live Pose Detection) -----------
elif app_mode == "Track 2":
    st.markdown("## 🔴 Track 2 - Live Pose Detection")

    if 'video_running' not in st.session_state:
        st.session_state.video_running = False

    st.write("### Yoga Poses in this Track:")
    poses = [
        ("Ardha Chakrasana", img5, """- Stand feet hip-width apart\n- Inhale, raise arms\n- Exhale, bend back\n- Hold 5 sec"""),
        ("Utkatasana", img6, """- Feet together\n- Inhale, raise arms\n- Exhale, bend knees\n- Hold 5 sec"""),
        ("Veerabhadrasana 2", img7, """- Step one foot back\n- Bend front knee\n- Arms parallel to ground\n- Hold 5 sec"""),
    ]
    for title, img, desc in poses:
        left, right = st.columns(2)
        with left: st.subheader(title); st.write(desc)
        with right: st.image(img, use_container_width=True)
        st.markdown("----")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("▶️ Start"):
            st.session_state.video_running = True
    with col2:
        if st.button("⏹️ Stop"):
            st.session_state.video_running = False

    cap = cv2.VideoCapture(0)
    FRAME_WINDOW = st.empty()

    while st.session_state.video_running:
        ret, frame = cap.read()
        if not ret:
            st.error("Webcam not detected!")
            break
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image = cv2.resize(image, (800, 600))

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2))

            landmarks = results.pose_landmarks.landmark
            def get_point(p): return [landmarks[p].x, landmarks[p].y]
            ls, rs = get_point(mp_pose.PoseLandmark.LEFT_SHOULDER), get_point(mp_pose.PoseLandmark.RIGHT_SHOULDER)
            lw, rw = get_point(mp_pose.PoseLandmark.LEFT_WRIST), get_point(mp_pose.PoseLandmark.RIGHT_WRIST)
            lh, rh = get_point(mp_pose.PoseLandmark.LEFT_HIP), get_point(mp_pose.PoseLandmark.RIGHT_HIP)
            le, re = get_point(mp_pose.PoseLandmark.LEFT_ELBOW), get_point(mp_pose.PoseLandmark.RIGHT_ELBOW)
            lk, rk = get_point(mp_pose.PoseLandmark.LEFT_KNEE), get_point(mp_pose.PoseLandmark.RIGHT_KNEE)
            la, ra = get_point(mp_pose.PoseLandmark.LEFT_ANKLE), get_point(mp_pose.PoseLandmark.RIGHT_ANKLE)

            # Pose validations
            if pose_number == 1:
                left_angle = calculate_angle(lw, ls, lh)
                right_angle = calculate_angle(rw, rs, rh)
                distance = np.linalg.norm(np.array(lw) - np.array(rw))
                if left_angle > 100 and right_angle > 100 and distance < 0.1:
                    cv2.putText(image, "Pose: Correct", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    counter, pose_number = count_time(5)
                else:
                    cv2.putText(image, "Pose: Incorrect", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    counter = 0

            elif pose_number == 2:
                if (calculate_angle(lh, lk, la) < 150 and calculate_angle(rh, rk, ra) < 150 and
                    calculate_angle(ls, le, lw) > 150 and calculate_angle(rs, re, rw) > 150):
                    cv2.putText(image, "Pose: Correct", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    counter, pose_number = count_time(5)
                else:
                    cv2.putText(image, "Pose: Incorrect", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    counter = 0

            elif pose_number == 3:
                if (calculate_angle(rh, rk, ra) < 120 and
                    calculate_angle(ls, le, lw) > 150 and calculate_angle(rs, re, rw) > 150):
                    cv2.putText(image, "Pose: Correct", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    counter, pose_number = count_time(5)
                else:
                    cv2.putText(image, "Pose: Incorrect", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    counter = 0

            else:
                cv2.putText(image, "Track Completed 🎉", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 215, 0), 2)
                st.session_state.video_running = False

            cv2.putText(image, f"TIME: {int(counter)}s", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 255), 2)

        FRAME_WINDOW.image(image, channels="BGR", use_container_width=True)

    cap.release()
