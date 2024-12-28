import streamlit as st

# Upload pdf files
st.header("Personal Doc Analyzer Chatbot")


with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a pdf & ask your questions", type="pdf")

# Extract text

# Perform data chunking

