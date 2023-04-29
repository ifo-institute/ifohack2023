import streamlit as st
from PIL import Image
from utils import init

init()
st.title(":blue[A] Gentle Introduction to Streamlit")

st.markdown("[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/ifo-institute/ifohack2023/tree/main/Workshops/Streamlit%20Basics%20and%20VSCode)")

image = Image.open("images/gentle.jpg")

st.image(image, use_column_width=True)

code = """
# install

pip install streamlit
pip install torch
pip install transformers
"""

st.code(code, language="bash", line_numbers=False)
