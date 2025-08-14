import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Finley - Your Financial Memory",
    page_icon="🤖",
    layout="centered"
)

# --- CUSTOM CSS for font and styling ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

body {
    font-family: 'Montserrat', sans-serif;
    background: #f5f7fa;
    color: #222222;
}
.header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: 15px;
    margin-bottom: 1rem;
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
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}
.card {
    background: white;
    border-radius: 12px;
    padding: 20px 25px;
    box-shadow: 0 4px 10px rgb(0 0 0 / 0.08);
    margin-bottom: 2rem;
    max-width: 700px;
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
    font-size: 1.0rem;
    line-height: 1.0;
    margin: 0;
}
.stTextArea textarea {
    border-radius: 10px !important;
    border: 1.5px solid #ccc !important;
    padding: 12px !important;
    font-size: 1.1rem !important;
    font-family: 'Montserrat', sans-serif !important;
    resize: vertical !important;
    min-height: 120px !important;
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
    margin-top: 10px;
    display: block;
    margin-left: auto;
    margin-right: auto;
}
.stButton > button:hover {
    background-color: #125a7e !important;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.examples {
    background: #eaf3fc;
    border-left: 6px solid #1767a0;
    padding: 15px 20px;
    margin-bottom: 2rem;
    font-style: italic;
    color: #264d73;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# --- LOGO SVG ---
logo_svg = """
<svg width="60" height="60" viewBox="0 0 100 100" 
    xmlns="http://www.w3.org/2000/svg" style="display:inline-block;">
  <polygon points="50,5 95,50 50,95 5,50" fill="white" stroke="black" stroke-width="4"/>
  <circle cx="35" cy="45" r="7" fill="black"/>
  <circle cx="65" cy="45" r="7" fill="black"/>
</svg>
"""

# --- HEADER WITH LOGO ---
st.markdown(f"""
<div class="header">
  {logo_svg}
  <h1 class="title">Finley</h1>
</div>
""", unsafe_allow_html=True)

# --- TAGLINE ---
st.markdown(
    '<div class="tagline">An AI-powered memory and narrative system built for FP&amp;A teams. Finley consolidates financial commentary across your organization, tracks evolving insights over time, and surfaces relevant context when you need it.</div>', 
    unsafe_allow_html=True)

# --- INPUT AREA ---
comment = st.text_area("", placeholder="Give Finley commentary to remember, or ask it questions here...")

if st.button("Submit"):
    if comment.strip():
        if "submissions" not in st.session_state:
            st.session_state.submissions = []
        st.session_state.submissions.append({"comment": comment})
        st.success("I'll remember that for you")
        
        xxx
        
    else:
        st.error("Please enter a comment before submitting.")

# --- RECENT SUBMISSIONS ---
if "submissions" in st.session_state and st.session_state.submissions:
    st.markdown("### Recent Submissions")
    for s in reversed(st.session_state.submissions[-5:]):
        st.markdown(f"- {s['comment']}")

# --- EXAMPLES BOX ---
st.markdown("""
<div class="examples">
<strong>Examples of what you can share or ask:</strong><br>
- “Why did sales dip in Q2 for the Northeast region?”<br>
- “Explain the increase in marketing expenses last month.”<br>
- “Notes on supply chain delays affecting inventory.”<br>
- “Questions about forecast assumptions for next quarter.”<br>
- “Comments on budget revisions or unusual costs.”<br>
</div>
""", unsafe_allow_html=True)

import streamlit as st

# --- FILE / PHOTO UPLOAD BOX ---
st.markdown("""
<div style="
    border: 2px dashed #ccc;
    padding: 1rem;
    text-align: center;
    font-size: 18px;
    border-radius: 8px;
    background-color: #f9f9f9;
">
    <strong>Add File</strong> or <strong>Add Photo</strong><br>
    <span style="font-size:14px; color:#555;">Click below to choose a file</span>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png", "pdf", "docx"])
if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")


# --- DESCRIPTION CARD ---
st.markdown("""
<div class="card">
  <h3>About Finley</h3>
  <p>Finley remembers not just what happened, but why — helping your finance team tell the story behind the numbers. It acts as a centralized commentary engine where month-end notes are stored, organized, and recalled intelligently across teams and time.</p>
  <p>Finley reduces knowledge loss, prevents information silos, and bridges insights from field teams to executives.</p>
</div>
""", unsafe_allow_html=True)
