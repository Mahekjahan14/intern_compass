import streamlit as st
import pandas as pd
import os

st.title("🏆 Intern Leaderboard")

progress_file = "data/progress.csv"

if os.path.exists(progress_file):
    df = pd.read_csv(progress_file)
    completed = df[df["Status"] == "Completed"]
    leaderboard = completed["Intern Name"].value_counts().reset_index()
    leaderboard.columns = ["Intern Name", "Tasks Completed"]
    st.table(leaderboard)
else:
    st.info("No progress data found.")