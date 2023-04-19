import streamlit as st
from PIL import Image
from utils import init

init()

st.title(":blue[A] gentle introduction to Streamlit")
image = Image.open("gentle.jpg")

st.image(image)
