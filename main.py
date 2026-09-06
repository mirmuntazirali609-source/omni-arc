import streamlit as st
from groq import Groq

st.set_page_config(page_title="OMNI ARC")
st.title("🧠 OMNI ARC")
st.success("✅ REAL GROQ BRAIN CONNECTED")

api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

ask = st.text_input("Ask OMNI ARC anything:")

if st.button("🚀 GO OMNI!!!"):
    if ask:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "user", "content": ask}
            ]
        )
        st.write(response.choices[0].message.content)
    else:
        st.warning("Type something first!")
