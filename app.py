import os
import openai
import streamlit as st
from openai.error import RateLimitError, AuthenticationError  # ✅ import exceptions

# Read OpenAI API key from Streamlit Secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Writing Coach (Beta)")

# Text areas for input
student_text = st.text_area("Paste previous student writing:")
draft_text = st.text_area("Paste current draft:")

if st.button("Revise"):
    if student_text.strip() == "" or draft_text.strip() == "":
        st.warning("Please paste both texts.")
    else:
        # Prompt for the AI
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
        try:
            # Call OpenAI API using GPT-3.5-turbo
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4
            )

            # Extract revised text
            revised_text = response.choices[0].message.content

            # Display revised draft
            st.subheader("Revised Draft")
            st.write(revised_text)

        except RateLimitError:
            st.error("OpenAI rate limit exceeded. Please wait a minute and try again.")
        except AuthenticationError:
            st.error("API key is invalid or missing. Check your Streamlit Secrets.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
