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
    "📝 Give Feedback": "Provide constructive feedback on meetings, processes, or tools.",
    "❓ Ask Questions": "Get clarification on policies, procedures, or workplace expectations.",
    "📊 Report Issues": "Discreetly flag challenges or concerns for management.",
    "🎉 Celebrate Wins": "Highlight team successes and individual contributions."
}

cols = st.columns(2)
for i, (title, desc) in enumerate(categories.items()):
    with cols[i % 2]:
        st.markdown(f"**{title}**\n\n{desc}")

# --- INPUT FORM ---
st.markdown("### ✍️ Submit Your Message to Finley")
with st.form("message_form"):
    category = st.selectbox("Select a category", list(categories.keys()))
    message = st.text_area("Your message", placeholder="Type here...")
    submit_button = st.form_submit_button("📤 Send to Finley")

if submit_button:
    st.success("✅ Your message has been sent! Thank you for sharing.")

# --- FAQ ---
with st.expander("❓ FAQ"):
    st.markdown("""
    **Q: Is this anonymous?**  
    Yes. Your messages are not linked to your name unless you choose to sign it.

    **Q: Who sees my message?**  
    Only the people or team designated to review workplace feedback.

    **Q: Can I attach files or images?**  
    Not right now — text only, to keep it simple.

    **Q: Is this a replacement for HR?**  
    No, but it can help HR and management act on feedback faster.
    """)

# --- FOOTER ---
st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size: 12px; color: #999;'>
    © 2025 Finley Workplace Helper
    </p>
    """,
    unsafe_allow_html=True
)
