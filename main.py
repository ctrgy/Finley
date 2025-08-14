import streamlit as st

# Page setup
st.set_page_config(
    page_title="Finley - Your Financial Memory",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Remove the toggle arrows
st.markdown("""
<style>
[data-testid="collapsedControl"] {
    display: none !important;
}
section[data-testid="stSidebar"],
div[data-testid="stSidebar"] {
    min-width: 320px !important;
    width: 320px !important;
}
</style>
""", unsafe_allow_html=True)

# Sidebar content
st.sidebar.title("Finley")
st.sidebar.write("Your financial memory and assistant.")

# Main title
st.title("Chat with Finley")

# Chat history display (optional placeholder)
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.write(f"**{msg['role']}**: {msg['content']}")

# Chat input row
col1, col2 = st.columns([6, 1])
with col1:
    user_message = st.text_input(
        "Type your message...",
        label_visibility="collapsed"
    )
with col2:
    send_button = st.button("Send")

# When send is clicked
if send_button and user_message.strip():
    st.session_state.messages.append({"role": "You", "content": user_message})
    st.session_state.messages.append({"role": "Finley", "content": "Got your message!"})
    st.experimental_rerun()

# Upload section (completely separate)
st.markdown("#### Upload files or photos:")
uploaded_files = st.file_uploader(
    "Upload Files",
    accept_multiple_files=True,
    type=None
)

if uploaded_files:
    for file in uploaded_files:
        st.write(f"Uploaded: {file.name}")
