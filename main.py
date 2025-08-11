import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Finley - FP&A Helper",
    page_icon="🤖",
    layout="centered"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

body {
    font-family: 'Poppins', sans-serif;
    background: #f0f4f8;
    color: #333333;
    margin: 0;
    padding: 0;
}
.header {
    text-align: center;
    margin-top: 2rem;
    margin-bottom: 1rem;
}
.logo {
    width: 90px;
    margin: 0 auto 10px auto;
}
.title {
    font-size: 3rem;
    color: #2C7BE5;
    font-weight: 700;
    margin-bottom: 0.2rem;
}
.tagline {
    font-size: 1.2rem;
    color: #555555;
    max-width: 600px;
    margin: 0 auto 2rem auto;
}
.category-card {
    background: white;
    border-radius: 15px;
    box-shadow: 0 6px 15px rgba(44,123,229,0.2);
    padding: 20px 25px;
    margin-bottom: 20px;
    max-width: 650px;
    margin-left: auto;
    margin-right: auto;
    transition: transform 0.2s ease;
}
.category-card:hover {
    transform: translateY(-5px);
}
.category-title {
    font-weight: 700;
    font-size: 1.4rem;
    margin-bottom: 6px;
    color: #2C7BE5;
}
.category-desc {
    font-size: 1rem;
    color: #444444;
}
.form-section {
    max-width: 650px;
    margin: 2rem auto 3rem auto;
    padding: 25px;
    background: white;
    border-radius: 15px;
    box-shadow: 0 6px 15px rgba(44,123,229,0.15);
}
.stTextArea textarea {
    border-radius: 12px !important;
    border: 1.8px solid #ddd !important;
    padding: 15px !important;
    font-size: 1.1rem !important;
    font-family: 'Poppins', sans-serif !important;
    resize: vertical !important;
    min-height: 120px !important;
    box-shadow: inset 0 3px 8px rgb(0 0 0 / 0.07) !important;
}
.stSelectbox select {
    border-radius: 12px !important;
    border: 1.8px solid #ddd !important;
    padding: 10px !important;
    font-size: 1rem !important;
    font-family: 'Poppins', sans-serif !important;
    box-shadow: inset 0 3px 8px rgb(0 0 0 / 0.07) !important;
}
.stButton > button {
    background-color: #2C7BE5 !important;
    color: white !important;
    border-radius: 18px !important;
    padding: 12px 30px !important;
    font-size: 1.25rem !important;
    font-weight: 700 !important;
    border: none !important;
    cursor: pointer !important;
    transition: background-color 0.3s ease;
}
.stButton > button:hover {
    background-color: #225db0 !important;
}
.expanderHeader {
    font-size: 1.15rem !important;
    font-weight: 600 !important;
}
#MainMenu, footer, header {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# --- CUSTOM LOGO SVG ---
finley_logo_svg = """
<svg width="90" height="90" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" >
  <circle cx="32" cy="32" r="30" fill="#2C7BE5" />
  <circle cx="20" cy="26" r="6" fill="white" />
  <circle cx="44" cy="26" r="6" fill="white" />
  <circle cx="20" cy="26" r="3" fill="#2C7BE5" />
  <circle cx="44" cy="26" r="3" fill="#2C7BE5" />
  <rect x="16" y="40" width="32" height="8" rx="4" fill="white" />
  <rect x="22" y="42" width="20" height="4" rx="2" fill="#2C7BE5" />
</svg>
"""

# --- HEADER ---
st.markdown(f"""
<div class="header">
  <div class="logo">{finley_logo_svg}</div>
  <h1 class="title">Finley</h1>
  <p class="tagline">Your friendly FP&amp;A helper for ideas, feedback, questions, and more.</p>
</div>
""", unsafe_allow_html=True)

# --- CATEGORY CARDS ---
st.markdown("### How can Finley help you today?")
categories = {
    "💡 Share Ideas": "Suggest new financial models, reporting approaches, or analysis methods.",
    "📝 Give Feedback": "Provide input on FP&A processes, reports, or tools.",
    "❓ Ask Questions": "Seek clarification on forecasts, budgets, or financial data.",
    "📊 Report Issues": "Flag errors, data inconsistencies, or system challenges in finance.",
    "🎉 Celebrate Wins": "Highlight successful projects, targets met, or analysis insights."
}
cols = st.columns(2)
for i, (title, desc) in enumerate(categories.items()):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="category-card">
            <div class="category-title">{title}</div>
            <div class="category-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# --- FORM ---
st.markdown('<div class="form-section">')
st.markdown("### ✍️ Submit your message")
with st.form("input_form"):
    category = st.selectbox("Select a category", list(categories.keys()))
    placeholder_map = {
        "💡 Share Ideas": "Example: Propose adding a new revenue forecasting model.",
        "📝 Give Feedback": "Example: Suggest improvements to the month-end close process.",
        "❓ Ask Questions": "Example: Clarify assumptions behind the Q3 budget variance.",
        "📊 Report Issues": "Example: Highlight discrepancies in expense reporting.",
        "🎉 Celebrate Wins": "Example: Recognize the team for exceeding the sales forecast."
    }
    message = st.text_area("Your message", placeholder=placeholder_map.get(category, "Type your message here..."))
    submitted = st.form_submit_button("🚀 Send to Finley")

if submitted:
    if message.strip():
        st.success("✅ Your message has been sent! Thanks for sharing.")
        st.session_state.setdefault("submissions", [])
        st.session_state.submissions.append({"category": category, "message": message})
    else:
        st.error("Please enter a message before sending.")
st.markdown('</div>', unsafe_allow_html=True)

# --- RECENT SUBMISSIONS ---
if "submissions" in st.session_state and st.session_state.submissions:
    st.markdown("### 📋 Recent messages")
    for sub in st.session_state.submissions[-5:]:
        st.markdown(f"**{sub['category']}**: {sub['message']}")

# --- FAQ ---
with st.expander("❓ Frequently Asked Questions"):
    st.markdown("""
    **Q:** Is this anonymous?  
    **A:** Yes, your messages are not linked to your identity unless you share it.

    **Q:** Who reviews my messages?  
    **A:** Messages go to your team’s designated reviewers.

    **Q:** Can I attach files?  
    **A:** Not currently, only text messages.

    **Q:** Is this a replacement for HR?  
    **A:** No, it helps HR and management get feedback faster.

    **Q:** Can I edit or delete messages?  
    **A:** Not yet, but improvements are coming!
    """)
