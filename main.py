import streamlit as st
from groq import Groq

st.set_page_config(page_title="OMNI ARC", page_icon="✨")
st.title("✨ Ask OMNI Anything")

try:
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)
    st.success("✅ REAL GROQ BRAIN CONNECTED")
    real = True
except:
    st.error("❌ Demo Mode - Add Key in Secrets")
    real = False

q = st.text_input("Ask:", "American president name")

if st.button("🚀 GO OMNI!!"):
    if real:
        r = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role":"system","content":"You are OMNI ARC with 68 brains. Give best answer."},
                {"role":"user","content":q}
            ]
        )
        st.write(r.choices[0].message.content)
    else:
        st.write(f"Demo answer for: {q}")
        
