import streamlit as st
from PIL import Image
from utils import init

init()

st.title(":blue[A] Gentle Introduction to Streamlit")
image = Image.open("images/gentle.jpg")

st.image(image, use_column_width=True)

code = """
# install

pip install streamlit
pip install torch
pip install transformers
"""

st.code(code, language="bash", line_numbers=False)
