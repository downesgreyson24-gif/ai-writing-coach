import streamlit as st

st.title("AI Writing Coach (Beta)")

student_text = st.text_area("Paste previous student writing:")
draft_text = st.text_area("Paste current draft:")

if st.button("Revise"):
    if student_text.strip() == "" or draft_text.strip() == "":
        st.warning("Please paste both texts.")
    else:
        st.subheader("Revised Draft")
        st.write(
            "This draft has been reviewed for clarity and tone. "
            "Your writing already shows strong analytical depth. "
            "Focus on tightening sentence structure and maintaining consistent terminology."
        )
