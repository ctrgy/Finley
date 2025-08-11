import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Finley - Workplace Feedback",
    page_icon="🤖",
    layout="centered"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        /* Page background and font */
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f8f9fa;
        }
        /* Title styling */
        .main-title {
            font-size: 3rem;
            font-weight: bold;
            color: #333333;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        /* Tagline styling */
        .tagline {
            text-align: center;
            color: #666666;
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }
        /* Card container */
        .stTextArea textarea, .stSelectbox select {
            border-radius: 8px;
            border: 1px solid #cccccc;
            padding: 10px;
        }
        /* Submit button */
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 0.6rem 1.5rem;
            border: none;
            font-size: 1rem;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        /* Hide Streamlit default menu and footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='main-title'>Meet Finley 🤖</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Your friendly workplace helper — share feedback, ideas, and questions.</div>", unsafe_allow_html=True)

# --- ABOUT ---
st.write("**What Finley is:** A safe, simple way to share your thoughts.")
st.write("**What Finley isn’t:** A gossip collector or a black hole for feedback.")

st.markdown("---")

# --- FEEDBACK FORM ---
category = st.selectbox(
    "Select a category",
    ["Finance", "Operations", "Sales", "General", "Other"]
)

comment = st.text_area("Your comment or question")

if st.button("Submit"):
    if comment.strip():
        st.session_state.setdefault("submissions", [])
        st.session_state.submissions.append({"category": category, "comment": comment})
        st.success("✅ Your comment has been submitted!")
    else:
        st.error("Please enter a comment before submitting.")

# --- RECENT SUBMISSIONS (for demo only) ---
if "submissions" in st.session_state and st.session_state.submissions:
    st.markdown("### Recent Submissions")
    for s in st.session_state.submissions[-5:]:
        st.markdown(f"**{s['category']}**: {s['comment']}")

