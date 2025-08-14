import streamlit as st

# --- REMOVE SIDEBAR TOGGLE ---
st.markdown("""
<style>
[data-testid="collapsedControl"] {
    display: none !important;
}
</style>
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

