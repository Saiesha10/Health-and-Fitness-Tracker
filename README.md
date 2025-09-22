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

<img width="701" height="370" alt="image" src="https://github.com/user-attachments/assets/e8e66d6f-e921-48e0-9e11-06641810037a" />
<img width="751" height="397" alt="image" src="https://github.com/user-attachments/assets/734d8ae5-6884-4f8a-a98d-9828fac5430b" />
<img width="694" height="367" alt="image" src="https://github.com/user-attachments/assets/b7db7ff1-af88-4735-abd5-ec21e6e8033d" />
<img width="711" height="374" alt="image" src="https://github.com/user-attachments/assets/23649226-4194-410b-8b77-ed3ec473af42" />
<img width="740" height="392" alt="image" src="https://github.com/user-attachments/assets/7490de2e-48ac-423b-8845-06cb5f1c920a" />
<img width="682" height="351" alt="image" src="https://github.com/user-attachments/assets/a88ed91c-8fd9-4995-b751-49dcaca07d97" />
<img width="773" height="331" alt="image" src="https://github.com/user-attachments/assets/be5843b3-a054-41b1-b4e1-7e840277f5a3" />






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
