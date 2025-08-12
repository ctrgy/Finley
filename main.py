import streamlit as st

st.set_page_config(page_title="Finley", page_icon="🤖", layout="centered")

st.title("Meet Finley")
st.subheader("Your friendly workplace helper — here to take in feedback, ideas, and questions.")

st.write("**What Finley is:** A safe, simple way to share your thoughts.")
st.write("**What Finley isn’t:** A gossip collector or a black hole for feedback.")

category = st.selectbox("Select a category", ["Finance", "Operations", "Sales", "General", "Other"])
comment = st.text_area("Your comment or question")

if st.button("Submit"):
    st.session_state.setdefault("submissions", [])
    st.session_state.submissions.append({"category": category, "comment": comment})
    st.success("✅ Your comment has been submitted!")

if "submissions" in st.session_state and st.session_state.submissions:
    st.subheader("Recent submissions")
    for s in st.session_state.submissions[-5:]:
        st.write(f"**{s['category']}**: {s['comment']}")

