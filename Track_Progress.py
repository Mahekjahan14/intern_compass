import streamlit as st
import pandas as pd
import os

st.title("📈 Track Progress")

progress_file = "data/progress.csv"
os.makedirs("data", exist_ok=True)

if not os.path.exists(progress_file):
    pd.DataFrame(columns=["Intern Name", "Task", "Status", "Update"]).to_csv(progress_file, index=False)

with st.form("progress_form"):
    intern = st.text_input("Intern Name")
    task = st.text_input("Task")
    status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
    update = st.text_area("Progress Update")
    submitted = st.form_submit_button("Submit Progress")

    if submitted and intern and task:
        df = pd.read_csv(progress_file)
        new_row = pd.DataFrame([[intern, task, status, update]], columns=["Intern Name", "Task", "Status", "Update"])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(progress_file, index=False)
        st.success("Progress submitted!")