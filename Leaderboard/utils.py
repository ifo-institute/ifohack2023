import streamlit as st
from PIL import Image


def init():
    logo = Image.open("logo.png")
    st.set_page_config(
        page_title="Hack 2023", page_icon=logo, initial_sidebar_state="collapsed"
    )

    hide_streamlit_style = """
    <style>
    div[data-testid="stDecoration"] {
       visibility: hidden;
       height: 0%;
       position: fixed;
    }
    #MainMenu {visibility: hidden;}
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
    footer {visibility: hidden;}
    </style>
    """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
