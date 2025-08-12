import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Finley - Your Financial Memory",
    page_icon="🤖",
    layout="centered"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    /* General page styling */
    body {
        font-family: 'Montserrat', sans-serif;
        background: #f5f7fa;
        color: #222222;
    }

    /* Header container */
    .header {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        margin-bottom: 1rem;
    }
    .logo {
        font-size: 3.5rem;
        transform: rotate(-10deg);
    }
    .title {
        font-size: 3rem;
        font-weight: 700;
        color: #1767a0;
        letter-spacing: 1.2px;
        margin: 0;
    }
    .tagline {
        text-align: center;
        color: #555555;
        font-size: 1.25rem;
        margin-top: -10px;
        margin-bottom: 2rem;
    }

    /* Cards for info */
    .card {
        background: white;
        border-radius: 12px;
        padding: 20px 25px;
        box-shadow: 0 4px 10px rgb(0 0 0 / 0.08);
        margin-bottom: 2rem;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    .card h3 {
        color: #1767a0;
        margin-bottom: 10px;
        font-weight: 600;
    }
    .card p {
        color: #444444;
        font-size: 1rem;
        line-height: 1.5;
        margin: 0;
    }

    /* Form elements */
    .stTextArea textarea {
        border-radius: 10px !important;
        border: 1.5px solid #ccc !important;
        padding: 12px !important;
        font-size: 1.1rem !important;
        font-family: 'Montserrat', sans-serif !important;
        resize: vertical !important;
        min-height: 100px !important;
        box-shadow: inset 0 2px 4px rgb(0 0 0 / 0.05) !important;
    }
    .stSelectbox select {
        border-radius: 10px !important;
        border: 1.5px solid #ccc !important;
        padding: 8px !important;
        font-size: 1rem !important;
        font-family: 'Montserrat', sans-serif !important;
        box-shadow: inset 0 2px 4px rgb(0 0 0 / 0.05) !important;
    }
    .stButton > button {
        background-color: #1767a0 !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 0.7rem 2.2rem !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        border: none !important;
        cursor: pointer !important;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #125a7e !important;
    }

    /* Hide Streamlit default menu/footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<div class="header">
  <div class="logo">🤖</div>
  <h1 class="title">Finley</h1>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="tagline">Your AI-powered financial memory and narrative system</div>', unsafe_allow_html=True)

# --- INFO CARDS ---
st.markdown("""
<div class="card">
  <h3>What Finley is:</h3>
  <p>A safe, simple way to share your team’s financial insights and questions.</p>
</div>
<div class="card">
  <h3>What Finley isn’t:</h3>
  <p>Not a gossip collector or a black hole for feedback — just your finance team’s smart memory.</p>
</div>
""", unsafe_allow_html=True)

# --- FORM ---
category = st.selectbox(
    "Select a category",
    ["Finance", "Operations", "Sales", "General", "Other"]
)

comment = st.text_area("Your comment or question", placeholder="Type your thoughts here...")

if st.button("Submit"):
    if comment.strip():
        st.session_state.setdefault("submissions", [])
        st.session_state.submissions.append({"category": category, "comment": comment})
        st.success("✅ Your comment has been submitted!")
    else:
        st.error("Please enter a comment before submitting.")

# --- RECENT SUBMISSIONS ---
if "submissions" in st.session_state and st.session_state.submissions:
    st.markdown("### Recent Submissions")
    for s in st.session_state.submissions[-5:]:
        st.markdown(f"**{s['category']}**: {s['comment']}")
