import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Finley - Your Financial Memory",
    layout="centered"  # keep centered, toggle sidebar remains default
)

# --- HEADER ---
st.markdown("""
<h1 style='text-align: center; color: #1767a0; font-family: Montserrat;'>
Finley
</h1>
<div style='text-align: center; color: #555555; max-width: 700px; margin: auto;'>
An AI-powered memory and narrative system built for FP&A teams. Finley consolidates financial commentary across your organization, tracks evolving insights over time, and surfaces relevant context when you need it.
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
st.sidebar.markdown("## About Finley")
st.sidebar.markdown("""
Finley remembers not just what happened, but why — helping your finance team tell the story behind the numbers.
- Centralized commentary engine
- Tracks insights over time
- Reduces knowledge loss and silos
- Upload files or photos for Finley to remember and analyze
""")

st.sidebar.markdown("""
<div style='background: #eaf3fc; border-left: 4px solid #1767a0; padding: 10px; border-radius: 6px; font-size: 0.9rem;'>
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

# --- SEND BUTTON ---
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
