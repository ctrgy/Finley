import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Finley Chat", layout="wide")

# --- PERMANENT SIDEBAR ---
with st.sidebar:
    st.image("your_logo.png", width=150)  # Logo
    st.title("Finley")
    st.markdown("This is your AI companion for commentary and questions.")
    st.markdown("### Example prompts:")
    st.markdown("- What's happening in this document?")
    st.markdown("- Summarize this photo.")
    st.markdown("- Give me insights from this PDF.")

# --- REMOVE SIDEBAR TOGGLE BUTTON ---
hide_sidebar_style = """
    <style>
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

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

# --- SAVE COMMENT BUTTON ---
if st.button("Send to Finley"):
    if comment.strip():
        if "submissions" not in st.session_state:
            st.session_state.submissions = []
        st.session_state.submissions.append({"comment": comment})
        st.success("Memory saved")
        st.session_state.comment_box = ""  # Clear text area after sending
    else:
        st.error("Please enter a comment before sending.")

# --- RECENT SUBMISSIONS ---
if "submissions" in st.session_state and st.session_state.submissions:
    st.markdown("### Recent Submissions")
    for s in reversed(st.session_state.submissions[-5:]):
        st.markdown(f"- {s['comment']}")
