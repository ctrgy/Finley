import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Finley - FP&A Memory & Q&A",
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
.card-section {
    max-width: 700px;
    margin: 0 auto 2rem auto;
    padding: 20px 30px;
    background: white;
    border-radius: 15px;
    box-shadow: 0 6px 15px rgba(44,123,229,0.2);
}
.card-title {
    font-weight: 700;
    font-size: 1.6rem;
    margin-bottom: 12px;
    color: #2C7BE5;
    text-align: center;
}
.card-desc {
    font-size: 1rem;
    color: #444444;
    line-height: 1.5;
    margin-bottom: 8px;
}
.form-section {
    max-width: 700px;
    margin: 2rem auto 3rem auto;
    padding: 30px 30px;
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
    min-height: 140px !important;
    box-shadow: inset 0 3px 8px rgb(0 0 0 / 0.07) !important;
}
.stButton > button {
    background-color: #2C7BE5 !important;
    color: white !important;
    border-radius: 18px !important;
    padding: 14px 38px !important;
    font-size: 1.3rem !important;
    font-weight: 700 !important;
    border: none !important;
    cursor: pointer !important;
    transition: background-color 0.3s ease;
    display: block;
    margin: 0 auto;
    min-width: 180px;
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
.icon {
    font-size: 1.8rem;
    vertical-align: middle;
    margin-right: 8px;
}
.example {
    color: #666;
    font-style: italic;
    margin-left: 1.5rem;
    margin-bottom: 10px;
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
  <p class="tagline">Your FP&A memory and question assistant — always learning, remembering, and helping.</p>
</div>
""", unsafe_allow_html=True)

# --- HOW FINLEY HELPS ---
st.markdown('<div class="card-section">')
st.markdown('<div class="card-title">How Finley can help you</div>')

with st.expander("🧠 Store Memories: Capture insights, learnings, and wins"):
    st.markdown("""
    - Note recurring budget discrepancies to track trends over time.<br>
    - Celebrate team wins on forecasts, projects, or analysis milestones.<br>
    - Document process improvements, assumptions, or key decisions.<br>
    <div class="example">Example: “Q2 revenue shortfall due to delayed product launch.”</div>
    """ , unsafe_allow_html=True)

with st.expander("❓ Ask Questions: Quickly get context and answers"):
    st.markdown("""
    - What caused the Q2 revenue variance?<br>
    - Who owns the updated expense report?<br>
    - When was the last revision to forecast assumptions?<br>
    <div class="example">Example: “What’s the current cash flow forecast?”</div>
    """, unsafe_allow_html=True)

st.markdown('</div>')

# --- INPUT FORM ---
st.markdown('<div class="form-section">')
st.markdown("### ✍️ Add your commentary or question")

with st.form("input_form", clear_on_submit=True):
    message = st.text_area("Type here...", placeholder="Type your ideas, insights, or questions about FP&A...")
    submitted = st.form_submit_button("💾 Save to Finley")

if submitted:
    if message.strip():
        st.success("💡 Memory saved! Finley is learning and remembering your insights.")
        st.session_state.setdefault("submissions", [])
        st.session_state.submissions.append({"message": message})
    else:
        st.error("⚠️ Please enter something before saving.")
st.markdown('</div>', unsafe_allow_html=True)

# --- RECENT SUBMISSIONS ---
if "submissions" in st.session_state and st.session_state.submissions:
    st.markdown("### 📋 Recent memories & questions")
    for sub in reversed(st.session_state.submissions[-5:]):  # newest first
        st.markdown(f"- {sub['message']}")

# --- FAQ ---
with st.expander("❓ Frequently Asked Questions"):
    st.markdown("""
    **Q:** Is my input anonymous?  
    **A:** Yes, Finley stores your insights without linking them to your identity unless you include your name.

    **Q:** Who can see my saved memories and questions?  
    **A:** Only authorized FP&A team members or reviewers.

    **Q:** Can I attach files or images?  
    **A:** Not at this time — text only to keep it simple.

    **Q:** Is Finley a replacement for ERP or BI tools?  
    **A:** No, Finley is a smart memory layer that complements your existing tools.

    **Q:** Can I edit or delete saved inputs?  
    **A:** Not yet, but we’re working on it!
    """)
