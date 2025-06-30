import streamlit as st
import pandas as pd
import os

st.title("💬 Feedback Center")

feedback_file = "data/feedback.csv"
os.makedirs("data", exist_ok=True)

if not os.path.exists(feedback_file):
    pd.DataFrame(columns=["Intern Name", "Feedback From", "Feedback"]).to_csv(feedback_file, index=False)

with st.form("feedback_form"):
    intern = st.text_input("Intern Name")
    from_whom = st.text_input("Feedback From")
    feedback = st.text_area("Your Feedback")
    submitted = st.form_submit_button("Submit Feedback")

    if submitted and intern and from_whom and feedback:
        df = pd.read_csv(feedback_file)
        new_row = pd.DataFrame([[intern, from_whom, feedback]], columns=["Intern Name", "Feedback From", "Feedback"])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(feedback_file, index=False)
        st.success("Feedback submitted!")