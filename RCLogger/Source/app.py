import streamlit as st
import os

with open("Source\styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])

with col1:
    st.image("Resources\RCLogo.png", width=150)
with col2:
    st.markdown("<h1 class='title'>RADIANT CHAMPS</h1>", unsafe_allow_html=True)

st.markdown("<h1 class='subheading'>Badminton Academy</h1>", unsafe_allow_html=True)