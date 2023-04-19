import streamlit as st
from transformers import AutoTokenizer, T5ForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")


st.title("My first dashboard")
st.write("Hello World!")

text_translate = st.text_area(
    "Text to translate",
    """
My name is Victor and I live in Munich
""",
)
input_ids = tokenizer(
    f"translate English to German: {text_translate}", return_tensors="pt"
).input_ids
outputs = model.generate(input_ids)
st.write(tokenizer.decode(outputs[0], skip_special_tokens=True))
