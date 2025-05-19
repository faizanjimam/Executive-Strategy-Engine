
# Executive Strategy Insight Engine – Powered by Tier 2.5+ Logic

import streamlit as st
import openai

# Load OpenAI key securely
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit page setup
st.set_page_config(page_title="Executive Strategy Engine", layout="centered")
st.title("📡 Executive Strategy Insight Engine")
st.markdown("""
This app generates high-quality, executive-level strategic responses using advanced reasoning logic.  
Paste in one or more strategic questions or context summaries from board, C-suite, or strategic teams.
""")

# User input area
user_input = st.text_area("📝 Paste the executive question or strategy problem to analyze:")

if st.button("🧠 Generate Strategic Response"):
    if not user_input.strip():
        st.warning("Please enter a valid input.")
    else:
        with st.spinner("Generating board-level insights..."):
            system_msg = (
                "You are a senior strategy intelligence agent trained on Tier 2.5+ logic. "
                "You understand strategic drift, execution friction, consequence-weighted timing, trust failure, and silent erosion of alignment. "
                "You speak in plain language with high impact. Do not use jargon. Structure answers as if writing a high-trust internal executive memo. "
                "Each section should include: What’s working, What’s not, Insight, and a Recommendation."
            )
            prompt = f"""
Executive Strategic Brief

Context:
{user_input}

Instructions:
- Avoid buzzwords and empty phrases.
- Speak directly, as if briefing the CEO.
- Use bullet points or short paragraphs only when helpful.
- Highlight both visible and silent risks.
- Avoid suggesting 'improvements'—focus on friction, ownership gaps, or structural erosion.
- Conclude with a plain but firm closing insight.

Begin your structured response now:
"""
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": system_msg},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.4,
                    max_tokens=1000
                )
                result = response.choices[0].message.content
                st.subheader("📈 Executive-Level Strategic Response")
                st.markdown(result)
            except Exception as error:
                st.error(f"API Error: {error}")
