import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

import streamlit as st

st.title("AI Writing Coach (Beta)")

student_text = st.text_area("Paste previous student writing:")
draft_text = st.text_area("Paste current draft:")

if st.button("Revise"):
    if student_text.strip() == "" or draft_text.strip() == "":
        st.warning("Please paste both texts.")
    else:
        prompt = f"""
You are a writing coach.

Here is a student's previous writing:
{student_text}

Here is their current draft:
{draft_text}

Revise the current draft to:
- Preserve the student's ideas
- Match their natural writing voice
- Improve clarity and flow
- Avoid sounding robotic or overly formal
- Do NOT add new arguments or content

Return only the revised draft.
"""

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )

        revised_text = response.choices[0].message.content

        st.subheader("Revised Draft")
        st.write(revised_text)
