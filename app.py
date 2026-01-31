import streamlit as st

st.title("AI Writing Coach (Beta)")

student_text = st.text_area("Paste previous student writing:")
draft_text = st.text_area("Paste current draft:")

if st.button("Revise"):
    st.subheader("Revised Draft")
    st.write("This is where your revised text will go.")
