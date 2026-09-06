import streamlit as st
st.set_page_config(page_title="OMNI ARC", layout="wide")
st.title("🔥 OMNI ARC - LIVE!")
st.success("App is LIVE! Branch fixed!")
st.balloons()
name = st.text_input("Ask anything:")
if st.button("Go"):
    st.write(f"You said: {name}")
