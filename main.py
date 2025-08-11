import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Finley - Workplace Helper",
    page_icon="🤖",
    layout="centered"
)

# --- HEADER ---
st.markdown(
    """
    <h1 style='text-align: center; font-family: Arial, sans-serif; color: #2E86C1;'>
        🤖 Meet Finley
    </h1>
    <p style='text-align: center; font-size: 20px; color: #555;'>
        Your friendly workplace helper for sharing ideas, feedback, and questions — safely and easily.
    </p>
    """,
    unsafe_allow_html=True
)

# --- HOW IT WORKS ---
st.markdown("### 📌 How You Can Use Finley")
categories = {
    "💡 Share Ideas": "Suggest ways to improve projects, workflows, or the office environment.",
    "📝 Give Feedback": "Provide constructive feedback on meetings, processes,
