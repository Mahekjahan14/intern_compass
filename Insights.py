import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.title("📊 Insights & Charts")

progress_file = "data/progress.csv"

if os.path.exists(progress_file):
    df = pd.read_csv(progress_file)
    status_counts = df["Status"].value_counts()
    st.subheader("Overall Task Status Distribution")

    fig, ax = plt.subplots()
    status_counts.plot(kind="bar", ax=ax, color="skyblue")
    st.pyplot(fig)
else:
    st.info("No data to display.")