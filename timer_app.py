import streamlit as st
import time

st.title("⏱️ Smart Study & Focus Timer (Pomodoro)")
st.write("Boost your productivity for coding and science studies!")

study_time = st.slider("Select Study Duration (minutes):", 10, 60, 25)

if st.button("Start Focus Session"):
    with st.status("Focus mode active... Stay concentrated! 🚀", expanded=True) as status:
        st.write(f"Timer set for {study_time} minutes. Keep going, Rabia!")
        time.sleep(2) # Simulating progress for demo
        status.update(label="Session completed like a champion! 🎉", state="complete", expanded=False)
    st.balloons()
    st.success("Great job! Now take a 5-minute break.")
