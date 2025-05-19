
# Executive Strategy Insight Engine – Updated with Tier 2.5+ Structured Logic (Fixed Version)

import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Executive Strategy Engine", layout="centered")
st.title("📡 Executive Strategy Insight Engine")
st.markdown("""
Paste one or more high-level strategic questions or summaries.  
This engine generates executive responses that diagnose hidden risks, timing failures, and trust drift.
""")

user_input = st.text_area("📝 Paste the executive question or strategy problem:")

if st.button("🧠 Generate Strategic Response"):
    if not user_input.strip():
        st.warning("Please enter a valid input.")
    else:
        with st.spinner("Analyzing with Tier 2.5+ logic..."):
            system_msg = """You are a Tier 2.5+ strategic intelligence engine. Your task is to expose structural misalignments, hidden risks, timing gaps, and trust failures
within organizational strategy. Do not repeat the question. Do not summarize. Deliver insight.
Use four clear sections for each area: What’s Working, What’s Not, Strategic Insight, and Recommendation.
Follow these constraints:
- Always identify at least one silent or invisible failure (something not currently discussed openly).
- Always assign ownership: who should act, not just what to do.
- Avoid consulting language like 'consider' or 'implement'. Be decisive.
- Do not use generic business phrases.
- Treat clarity as higher priority than complexity.
- Final insight should connect execution to long-term trust, timing, or drift."""
            user_prompt = f"""Executive Strategy Request:
{user_input}

Instructions:
Analyze the situation using Tier 2.5+ logic:
1. Identify misalignments in timing, trust, and role clarity.
2. Highlight silent drift (where strategy is failing quietly).
3. Frame risks in terms of structural failure, not just surface symptoms.
4. Use plain language — no jargon, no repetition, no overexplaining.
5. End with a hard insight about what breaks first if we delay or misread the signal.

Deliver the response now.
"""
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": system_msg},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.4,
                    max_tokens=1200
                )
                result = response.choices[0].message.content
                st.subheader("📈 Executive-Level Strategic Response")
                st.markdown(result)
            except Exception as error:
                st.error(f"API Error: {error}")
