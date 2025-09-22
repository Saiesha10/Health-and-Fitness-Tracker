# 🏋️ Health and Fitness Tracker 

## 🚀 Overview
Health and Fitness Tracker is a **Python and Streamlit-based web application** designed to help users track their exercises, improve workout form, count reps, and manage nutrition. It also features an **AI-powered chatbot using Gemini API** for personalized fitness guidance.

This project combines **computer vision (Mediapipe, OpenCV)** for real-time pose detection with **Streamlit** for an interactive web interface, providing a full-stack fitness tracking experience.

## 🛠️ Tech Stack
- **Frontend / Backend:** Python + Streamlit
- **Computer Vision:** OpenCV, Mediapipe (Pose Detection)
- **AI Integration:** Gemini API (for chatbot guidance)
- **Styling:** CSS
- **Data Handling:** Local storage or CSV for user progress

## ⚡ Features
- **Real-time pose detection:** Track exercises like squats, pushups, curls, and shoulder press.  
- **Form analysis & rep counting:** Detect correct posture and count repetitions.  
- **Interactive AI chatbot (“FitBot”):** Powered by **Gemini API** to answer fitness-related questions.  
- **Nutrition tracking:** Log meals and monitor daily intake.  
- **Exercise tutorials:** Video guidance for proper form.  

## 📌 How to Run
```bash
# Clone the repository
git clone https://github.com/Saiesha10/Health-and-Fitness-Tracker.git

# Navigate to project folder
cd Health-and-Fitness-Tracker

# (Optional) Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Set up Gemini API key
# Example: Add your Gemini API key in 4__Chatbot.py or a .env file

# Run the app
streamlit run 1__Home.py
