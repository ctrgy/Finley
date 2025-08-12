import streamlit as st

st.set_page_config(
    page_title="Finley - FP&A Memory & Q&A",
    page_icon="🤖",
    layout="centered"
)

# Minimal CSS for fonts and spacing + bigger emojis & color pop
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');
    body {
        font-family: 'Poppins', sans-serif;
        background-color: #f0f4f8;
        color: #333;
        padding: 0 1rem 2rem 1rem;
    }
    .title {
        color: #2C7BE5;
        font-weight: 700;
        font-size: 3rem;
        margin-bottom: 0;
        text-align: center;
    }
    .tagline {
        color: #555;
        text-align: center;
        margin-top: 0;
        margin-bottom: 2rem;
        font-size: 1.2rem;
    }
    .section-title {
        color: #2C7BE5;
        font-weight: 700;
        font-size: 1.5rem;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
    }
    .example {
        font-style: italic;
        color: #666;
        margin-left: 1.5rem;
        margin-bottom: 1rem;
    }
    .emoji {
        font-size: 1.4rem;
        margin-right: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="title">Finley 🤖✨</h1>', unsafe_allow_html=True)
st.markdown('<p class="tagline">Your FP&A memory & question assistant — always learning, remembering, and helping 💡📊</p>', unsafe_allow_html=True)

# How Finley can help
st.markdown('<h2 class="section-title">How Finley can help you 🚀</h2>', unsafe_allow_html=True)

with st.expander("🧠 Store Memories: Capture insights, learnings, and wins 🎉"):
    st.write("• Note recurring budget discrepancies to track trends over time 📉")
    st.write("• Celebrate team wins on forecasts, projects, or milestones 🏆")
    st.write("• Document process improvements, assumptions, or key decisions 📚")
    st.markdown('<p class="example">Example: “Q2 revenue shortfall due to delayed product launch 🚀.”</p>', unsafe_allow_html=True)

with st.expander("❓ Ask Questions: Quickly get context and answers 🔍"):
    st.write("• What caused the Q2 revenue variance? 💰")
    st.write("• Who owns the updated expense report? 📝")
    st.write("• When was the last revision to forecast assumptions? 📅")
    st.markdown('<p class="example">Example: “What’s the current cash flow forecast? 💵”</p>', unsafe_allow_html=True)

# Input form
st.markdown('<h2 class="section-title">✍️ Add your commentary or question 🗣️</h2>', unsafe_allow_html=True)
with st.form("input_form", clear_on_submit=True):
    message = st.text_area("Type here...", placeholder="Type your ideas, insights, or questions about FP&A... 📈💬")
    submitted = st.form_submit_button("💾 Save to Finley")

if submitted:
    if message.strip():
        st.success("💡 Memory saved! Finley is learning and remembering your insights. 🤓")
        if "submissions" not in st.session_state:
            st.session_state.submissions = []
        st.session_state.submissions.append(message)
    else:
        st.error("⚠️ Please enter something before saving.")

# Show recent submissions
if "submissions" in st.session_state and st.session_state.submissions:
    st.markdown('<h2 class="section-title">📋 Recent memories & questions 📚</h2>', unsafe_allow_html=True)
    for msg in reversed(st.session_state.submissions[-5:]):
        st.markdown(f"• {msg}")

# FAQ
with st.expander("❓ Frequently Asked Questions 🤔"):
    st.markdown("""
    **Q:** Is my input anonymous? 🙈  
    **A:** Yes, Finley stores your insights without linking them to your identity unless you include your name.

    **Q:** Who can see my saved memories and questions? 👀  
    **A:** Only authorized FP&A team members or reviewers.

    **Q:** Can I attach files or images? 📎  
    **A:** Not at this time — text only to keep it simple.

    **Q:** Is Finley a replacement for ERP or BI tools? 🔄  
    **A:** No, Finley is a smart memory layer that complements your existing tools.

    **Q:** Can I edit or delete saved inputs? ✏️❌  
    **A:** Not yet, but we’re working on it!
    """)
