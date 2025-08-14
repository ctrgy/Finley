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

.comment-box textarea {
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
    background-color: #1767a0;
    color: white;
    border: none;
    padding: 0.7rem 2.2rem;
    font-weight: 700;
    font-size: 1.1rem;
    border-radius: 8px;
    cursor: pointer;
    margin-top: 8px;
    display: block;
    margin-left: auto;
    margin-right: auto;
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

.examples {
    background: #eaf3fc;
    border-left: 4px solid #1767a0;
    padding: 10px 12px;
    border-radius: 6px;
    font-size: 0.9rem;
    max-width: 250px;
    margin-bottom: 1rem;
}

.upload-note {
    font-size: 0.85rem;
    color: #333333;
    margin-top: 10px;
    padding: 5px 8px;
    border-radius: 5px;
    background-color: #f0f4f8;
}
</style>
""", unsafe_allow_html=True)

# --- LOGO SVG ---
logo_svg = """
<svg width="60" height="60" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
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
st.set_page_config(
    page_title="My App",
    layout="wide",
    initial_sidebar_state="expanded"  # always open
)

hide_sidebar_style = """
    <style>
        [data-testid="collapsedControl"] {
            display: none !important;
        }

        /* This hides the collapse/expand sidebar button */
        [data-testid="stSidebarNavCollapse"] {
            display: none !important;
        }

        /* This hides the small chevron button in some Streamlit versions */
        button[kind="header"] {
            display: none !important;
        }

    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

st.sidebar.markdown("## About Finley")
st.sidebar.markdown("""
Finley remembers not just what happened, but why — helping your finance team tell the story behind the numbers.
- Centralized commentary engine
- Tracks insights over time
- Reduces knowledge loss and silos
- Upload files or photos for Finley to remember or analyze
""")

st.sidebar.markdown("""
<div class="examples">
<strong>Examples of what you can share or ask:</strong><br>
- “Why did sales dip in Q2 for the Northeast region?”<br>
- “Explain the increase in marketing expenses last month.”<br>
- “Notes on supply chain delays affecting inventory.”<br>
- “Questions about forecast assumptions for next quarter.”<br>
- “Comments on budget revisions or unusual costs.”<br>
</div>
""", unsafe_allow_html=True)

# --- CHAT BOX ---
comment = st.text_area(
    "",
    placeholder="Give Finley commentary or ask it questions here...",
    key="comment_box",
    height=120
)

# --- FILE UPLOAD BELOW CHAT BOX ---
uploaded_file = st.file_uploader(
    "Upload File/Photo",
    type=["jpg", "jpeg", "png", "pdf", "docx"],
    key="file_upload"
)

# --- SEND COMMENT BUTTON ---
if st.button("Send to Finley"):
    if comment.strip():
        if "submissions" not in st.session_state:
            st.session_state.submissions = []
        st.session_state.submissions.append({"comment": comment})
        st.success("Memory saved")
        st.session_state.comment_box = ""  # Clear text area
    else:
        st.error("Please enter a comment before sending.")

# --- RECENT SUBMISSIONS ---
if "submissions" in st.session_state and st.session_state.submissions:
    st.markdown("### Recent Submissions")
    for s in reversed(st.session_state.submissions[-5:]):
        st.markdown(f"- {s['comment']}")
