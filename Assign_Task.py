import streamlit as st
import pandas as pd
import os

st.title("📝 Assign Task")

task_file = "data/tasks.csv"
os.makedirs("data", exist_ok=True)

if not os.path.exists(task_file):
    pd.DataFrame(columns=["Intern Name", "Task", "Deadline"]).to_csv(task_file, index=False)

with st.form("assign_task_form"):
    intern = st.text_input("Intern Name")
    task = st.text_area("Task Description")
    deadline = st.date_input("Deadline")
    submitted = st.form_submit_button("Assign Task")

    if submitted and intern and task:
        df = pd.read_csv(task_file)
        new_row = pd.DataFrame([[intern, task, deadline]], columns=["Intern Name", "Task", "Deadline"])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(task_file, index=False)
        st.success(f"Task assigned to {intern}!")