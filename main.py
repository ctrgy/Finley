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

.chat-box {
    background: white;
    border-radius: 12px;
    padding: 12px;
    box-shadow: 0 4px 10px rgb(0 0 0 / 0.08);
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 10px;
}

.chat-box textarea {
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
    background-color: #1767a0;
    color: white;
    border: none;
    padding: 0.7rem 2.2rem;
    font-weight: 700;
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

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- CHAT BOX ---
st.markdown('<div class="chat-box">', unsafe_allow_html=True)
comment = st.text_area(
    "",
    placeholder="Give Finley commentary or ask it questions here...",
    key="comment_box",
    height=120
)
st.markdown('</div>', unsafe_allow_html=True)

# --- FILE UPLOAD BELOW CHAT BOX ---
uploaded_file = st.file_uploader("Upload files/photos for Finley to remember or analyze", 
                                 type=["jpg", "jpeg", "png", "pdf", "docx"], key="file_upload")

# --- SEND BUTTON ---
if st.button("Send", key="send_btn"):
    if comment.strip() or uploaded_file:
        if "submissions" not in st.session_state:
            st.session_state.submissions = []
        st.session_state.submissions.append({
            "comment": comment,
            "file": uploaded_file.name if uploaded_file else None
        })
        st.success("Memory saved!")
        st.session_state.comment_box = ""  # clear text area
        st.session_state.file_upload = None  # reset file uploader
    else:
        st.error("Please enter a comment or upload a file before sending.")

# --- RECENT SUBMISSIONS ---
if "submissions" in st.session_state and st.session_state.submissions:
    st.markdown("### Recent Submissions")
    for s in reversed(st.session_state.submissions[-5:]):
        file_text = f" (File: {s['file']})" if s['file'] else ""
        st.markdown(f"- {s['comment']}{file_text}")
