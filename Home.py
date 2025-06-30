import streamlit as st
from PIL import Image
import os

# Optional: Load logo if exists
logo_path = "data/logo.png"
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=150)

# Title and description
st.markdown("<h1 style='color:#6C63FF;'>📌 InternCompass: Smart Intern Task Tracker</h1>", unsafe_allow_html=True)
st.markdown("Welcome to InternCompass! Use the sidebar to navigate between task management, progress tracking, and feedback insights.")

# Sidebar navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", [
    "🏠 Home",
    "📝 Assign Task",
    "📈 Track Progress",
    "🌟 Leaderboard",
    "💬 Feedback Center",
    "📊 Insights"
])

# Load the selected page
if page == "🏠 Home":
    st.subheader("InternCompass Dashboard")
    st.success("Select a section from the sidebar to get started!")

elif page == "📝 Assign Task":
    exec(open("Assign_Task.py", encoding="utf-8").read())

elif page == "📈 Track Progress":
    exec(open("Track_Progress.py", encoding="utf-8").read())

elif page == "🌟 Leaderboard":
    exec(open("Leaderboard.py", encoding="utf-8").read())

elif page == "💬 Feedback Center":
    exec(open("Feedback_Center.py", encoding="utf-8").read())

elif page == "📊 Insights":
    exec(open("Insights.py", encoding="utf-8").read())
