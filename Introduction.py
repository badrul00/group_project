import streamlit as st
import pandas as pd

st.set_page_config(page_title="Group_Project")

st.markdown("""
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #FF4B4B;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    .subtitle {
        font-size: 24px;
        font-weight: bold;
        color: #3A3B3C;
        text-align: center;
        margin-top: -10px;
    }
    .team-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }
    .team-member {
        font-size: 20px;
        font-weight: bold;
        color: #FF4B4B;
        margin: 5px 0;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">📊 COVID-19 in Mexico Analysis</p>', unsafe_allow_html=True)

st.markdown('<p class="subtitle">👥 Team Members</p>', unsafe_allow_html=True)

st.markdown("""
    <div class="team-box">
        <p class="team-member">🔹 Badrul</p>
        <p class="team-member">🔹 Nasruddin</p>
        <p class="team-member">🔹 Aina</p>
        <p class="team-member">🔹 Alisya</p>
        <p class="team-member">🔹 Syamira</p>
    </div>
""", unsafe_allow_html=True)