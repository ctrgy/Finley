import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Finley - Your Financial Memory",
    layout="centered"
)

# --- CUSTOM CSS ---
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
    font-size: 1.2rem;
    margin-top: -10px;
    margin-bottom: 2rem;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}

.chat-box {
    background: white;
    border-radius: 12px;
    padding: 15px 20px;
    box-shadow: 0 4px 10px rgb(0 0 0 / 0.08);
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    position: relative;
}

.chat-box textarea {
    width: 100%;
    border-radius: 10px !important;
    border: 1.5px solid #ccc !important;
    padding: 12px !important;
    font-size: 1.1rem !important;
    font-family: 'Montserrat', sans-serif !important;
    resize: vertical !important;
    min-height: 120px !important;
    box-shadow: inset 0 2px 4px rgb(0 0 0 / 0.05) !important;
}

.upload-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    background-color: #1767a0;
    color: white;
    border: none;
    padding: 0.5rem 1.2rem;
    font-weight: 700;
    font-size: 0.9rem;
    border-radius: 8px;
    cursor: pointer;
}
.upload-btn:hover {
    background-color: #125a7e;
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
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-top: 10px;
}
.stButton > button:hover {
    background-color: #125a7e !important;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.examples {
    background: #eaf3fc;
    border-left: 4px solid #1767a0;
    padding: 10px 12px;
    border-radius: 6px;
    font-size: 0.9rem;
    max-width: 250px;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# --- LOGO SVG ---
logo_svg = """
<svg width="60" height="60" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" style="display:inline-block;">
  <polygon points="50,5 95,50 50,95 5,50" fill="white" stroke="black" stroke-width="4"/>
  <circle cx="35" cy="45" r="7" fill="black"/>
  <circle cx="65" cy="45" r="7" fill="black"/>
</svg>
"""

# --- HEADER ---
st.markdown(f"""
<div class="header">
  {logo_svg}
  <h1 class="title">Finley</h1>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="tagline">An AI-powered memory and narrative system built for FP&A teams. Finley consolidates financial commentary across your organization, tracks evolving insights over time, and surfaces relevant context when you need it.</div>', unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.markdown("## About Finley")
st.sidebar.markdown("""
Finley remembers not just what happened, but why — helping your finance team tell the story behind the numbers.
- Centralized commentary engine
- Tracks insights over time
- Reduces knowledge loss and silos
- Upload files or photos for Finley to remember and analyze for you
""")

st.sidebar.markdown("""
<div class="examples">
<strong>Examples:</strong><br>
- “Why did sales dip in Q2 for the Northeast region?”<br>
- “Explain the increase in marketing expenses last month.”<br>
- “Notes on supply chain delays affecting inventory.”<br>
- “Questions about forecast assumptions for next quarter.”<br>
- “Comments on budget revisions or unusual costs.”<br>
</div>
""", unsafe_allow_html=True)

# --- Chat Box Styling ---
st.markdown("""
<style>
.chat-container {
    background: white;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0 4px 10px rgb(0 0 0 / 0.08);
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}
.chat-header {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 10px;
}
.chat-textarea {
    width: 100%;
    border-radius: 10px;
    border: 1.5px solid #ccc;
    padding: 10px;
    font-size: 1.1rem;
    min-height: 100px;
    resize: vertical;
    box-shadow: inset 0 2px 4px rgb(0 0 0 / 0.05);
}
.upload-btn {
    background-color: #1767a0;
    color: white;
    border: none;
    padding: 0.5rem 1.5rem;
    font-weight: 700;
    border-radius: 8px;
    cursor: pointer;
}
.upload-btn:hover {
    background-color: #125a7e;
}
.send-btn {
    background-color: #1767a0;
    color: white;
    border: none;
    padding: 0.7rem 2.2rem;
    font-weight: 700;
    border-radius: 8px;
    cursor: pointer;
    margin-top: 10px;
    display: block;
    margin-left: auto;
    margin-right: auto;
}
.send-btn:hover {
    background-color: #125a7e;
}
</style>
""", unsafe_allow_html=True)

import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Finley - Your Financial Memory", layout="centered")

# --- Custom CSS ---
st.markdown("""
<style>
.chat-container {
    background: white;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0 4px 10px rgb(0 0 0 / 0.08);
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    position: relative;
}
.chat-header {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 10px;
}
.chat-textarea {
    width: 100%;
    border-radius: 10px;
    border: 1.5px solid #ccc;
    padding: 12px;
    font-size: 1.1rem;
    font-family: 'Montserrat', sans-serif;
    min-height: 100px;
    resize: vertical;
    box-shadow: inset 0 2px 4px rgb(0 0 0 / 0.05);
}
.upload-btn {
    background-color: #1767a0;
    color: white;
    border: none;
    padding: 0.5rem 1.2rem;
    font-weight: 700;
    border-radius: 8px;
    cursor: pointer;
}
.upload-btn:hover {
    background-color: #125a7e;
}
.send-btn {
    background-color: #1767a0;
    color: white;
    border: none;
    padding: 0.7rem 2.2rem;
    font-weight: 700;
    border-radius: 8px;
    cursor: pointer;
    margin-top: 10px;
    display: block;
    margin-left: auto;
    margin-right: auto;
}
.send-btn:hover {
    background-color: #125a7e;
}
</style>
""", unsafe_allow_html=True)

import streamlit as st

# --- Custom CSS for unified chat box ---
st.markdown("""
<style>
.chat-container {
    position: relative;
    background: white;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0 4px 10px rgb(0 0 0 / 0.08);
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}
.chat-textarea {
    width: 100%;
    border-radius: 10px;
    border: 1.5px solid #ccc;
    padding: 12px;
    font-size: 1.1rem;
    font-family: 'Montserrat', sans-serif;
    min-height: 120px;
    resize: vertical;
    box-shadow: inset 0 2px 4px rgb(0 0 0 / 0.05);
}
.upload-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    background-color: #1767a0;
    color: white;
    border: none;
    padding: 0.5rem 1.2rem;
    font-weight: 700;
    border-radius: 8px;
    cursor: pointer;
}
.upload-btn:hover {
    background-color: #125a7e;
}
.send-btn {
    background-color: #1767a0;
    color: white;
    border: none;
    padding: 0.7rem 2.2rem;
    font-weight: 700;
    border-radius: 8px;
    cursor: pointer;
    margin-top: 10px;
    display: block;
    margin-left: auto;
    margin-right: auto;
}
.send-btn:hover {
    background-color: #125a7e;
}
</style>
""", unsafe_allow_html=True)

import streamlit as st

# --- Custom CSS for unified chat box with floating upload ---
st.markdown("""
<style>
.chat-container {
    position: relative;
    background: white;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0 4px 10px rgb(0 0 0 / 0.08);
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}
.chat-textarea {
    width: 100%;
    border-radius: 10px;
    border: 1.5px solid #ccc;
    padding: 12px;
    font-size: 1.1rem;
    font-family: 'Montserrat', sans-serif;
    min-height: 120px;
    resize: vertical;
    box-shadow: inset 0 2px 4px rgb(0 0 0 / 0.05);
}
.upload-btn-label {
    position: absolute;
    top: 10px;
    right: 10px;
    background-color: #1767a0;
    color: white;
    border-radius: 8px;
    padding: 0.5rem 1.2rem;
    font-weight: 700;
    cursor: pointer;
    text-align: center;
    display: inline-block;
}
.upload-btn-label:hover {
    background-color: #125a7e;
}
.upload-input {
    display: none;
}
.send-btn {
    background-color: #1767a0;
    color: white;
    border: none;
    padding: 0.7rem 2.2rem;
    font-weight: 700;
    border-radius: 8px;
    cursor: pointer;
    margin-top: 10px;
    display: block;
    margin-left: auto;
    margin-right: auto;
}
.send-btn:hover {
    background-color: #125a7e;
}
</style>
""", unsafe_allow_html=True)

# --- Chat Box Container ---
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Hidden file uploader
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png", "pdf", "docx"], key="file_upload", label_visibility="collapsed")

# Label acting as button
st.markdown(f"""
<label for="file_upload" class="upload-btn-label">Upload File</label>
""", unsafe_allow_html=True)

# Text area
comment = st.text_area("", placeholder="Give Finley commentary, upload files/photos or ask it questions here...", key="comment_box", height=120)

st.markdown('</div>', unsafe_allow_html=True)

# Send button
if st.button("Send", key="send_btn"):
    if comment.strip() or uploaded_file:
        if "submissions" not in st.session_state:
            st.session_state.submissions = []
        st.session_state.submissions.append({
            "comment": comment,
            "file": uploaded_file.name if uploaded_file else None
        })
        st.success("Memory saved!")
        st.session_state.comment_box = ""
        # Reset uploaded file
        st.session_state.file_upload = None
    else:
        st.error("Please enter a comment or upload a file before sending.")

# Recent submissions
if "submissions" in st.session_state and st.session_state.submissions:
    st.markdown("### Recent Submissions")
    for s in reversed(st.session_state.submissions[-5:]):
        file_text = f" (File: {s['file']})" if s['file'] else ""
        st.markdown(f"- {s['comment']}{file_text}")
