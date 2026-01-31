import streamlit as st

st.title("AI Writing Coach (Beta) - Mock Mode")

# Text areas for input
student_text = st.text_area("Paste previous student writing:")
draft_text = st.text_area("Paste current draft:")

if st.button("Revise"):
    if student_text.strip() == "" or draft_text.strip() == "":
        st.warning("Please paste both texts.")
    else:
        # MOCK GPT response - just simulates a revised draft
        revised_text = f"""
        [Mocked Revision] This is how the AI would revise your draft.
        Original draft length: {len(draft_text.split())} words.
        """
        st.subheader("Revised Draft")
        st.write(revised_text)
