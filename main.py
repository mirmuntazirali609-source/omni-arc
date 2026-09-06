        st.chat_message("assistant").write(resp)

elif menu == "🛠️ All 68 Tools":
    st.subheader("🛠️ 68 )
    tool = st.selectbox("Select Tool", features)
    st.markdown(f"<div class='feature-card'><h2>{tool}</h2></div>", unsafe_allow_html=True)
    inp = st.text_area("Input:", placeholder=f"Input for {tool}")
    if st.button(f"Execute {tool}"):
        if not inp: st.warning("Enter input!")
        else:
            st.success(f"✅ {tool} Executed!")
            if "Calculator" in tool:
                try: st.metric("Result", eval(inp))
                except: st.error("Invalid expression")
            elif "Password" in tool:
                pwd=''.join(random.choice(string.ascii_letters+string.digits+"!@#$%") for _ in range(12))
                st.code(pwd)
            else:
                st.write(f"🔥 Output for {tool}: Mock result for {tool}")
                st.json({"tool":tool,"input":inp,"status":"success"})

elif menu == "🎨 Creator Studio":
    st.subheader("🎨 Creator Studio")
    tab1,tab2,tab3 = st.tabs(["Image","Video","Social"])
    with tab1:
        d=st.text_input("Image description:","Futuristic mosque in Kashmir, OMNI ARC logo")
        s=st.selectbox("Style",["Photorealistic","Anime","Cyberpunk","3D","Oil Painting"])
        if st.button("Gen Image Prompt"): st.code(f"{d}, {s} style, 8k ultra detailed, trending artstation")
    with tab2:
        vd=st.text_input("Video idea:")
        if st.button("Gen Video Prompt"): st.code(f"Cinematic video: {vd}, 4k smooth drone shot")
    with tab3:
        t=st.text_input("Post topic:")
        p=st.selectbox("Platform",["Instagram","Threads","LinkedIn","Twitter"])
        
