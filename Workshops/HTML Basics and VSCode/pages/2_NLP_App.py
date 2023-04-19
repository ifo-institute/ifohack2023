import streamlit as st
from transformers import AutoTokenizer, T5ForConditionalGeneration

from utils import init

init()

st.title(":blue[T5] NLP Model")
st.write("Text-To-Text Transfer Transformer")

st.markdown(
    "![t5](https://1.bp.blogspot.com/-o4oiOExxq1s/Xk26XPC3haI/AAAAAAAAFU8/NBlvOWB84L0PTYy9TzZBaLf6fwPGJTR0QCLcBGAsYHQ/s640/image3.gif)"
)


@st.cache_data
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("t5-base")
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    return tokenizer, model


tokenizer, model = load_model()

###############################################################################
st.subheader("Task 1: Translation")

col1, col2 = st.columns(2)

with col1:
    fro = st.write("From: English")

with col2:
    to = st.radio("To", ("German", "French"), index=1)

text_translate = st.text_area(
    "Text to translate",
    """My name is Victor and I live in Munich""",
)

input_ids_translate = tokenizer(
    f"translate {fro} to {to}: {text_translate}", return_tensors="pt"
).input_ids
outputs_translate = model.generate(input_ids_translate)

st.write(tokenizer.decode(outputs_translate[0], skip_special_tokens=True))

if st.checkbox("Show code", key=1):
    code = """

    st.subheader("Task 1: Translation")

    col1, col2 = st.columns(2)

    with col1:
        fro = st.radio("From", ("English"))

    with col2:
        to = st.radio("To", ("German", "French"), index=1)

    text_translate = st.text_area(
        "Text to translate",
        \"\"\"My name is Victor and I live in Munich\"\"\",
    )

    input_ids_translate = tokenizer(
        f"translate {fro} to {to}: {text_translate}", return_tensors="pt"
    ).input_ids
    outputs_translate = model.generate(input_ids_translate)


    st.write(tokenizer.decode(outputs_translate[0], skip_special_tokens=True))
    """
    st.code(code, language="python", line_numbers=True)


###############################################################################
st.subheader("Task 2: Detect grammatical errors")

text = st.text_area(
    "Detect grammatical errors",
    """
Bayern won't already hasn't
""",
)

input_ids = tokenizer(f"cola sentence: {text}", return_tensors="pt").input_ids
outputs = model.generate(input_ids)

st.write(tokenizer.decode(outputs[0], skip_special_tokens=True))

if st.checkbox("Show code", key=2):
    code = """
    st.subheader("Task 2: Detect grammatical errors")

    text = st.text_area("Detect grammatical errors", \"\"\"
    Bayern won't already hasn't
    \"\"\")

    input_ids = tokenizer(
        f"cola sentence: {text}", return_tensors="pt"
    ).input_ids
    outputs = model.generate(input_ids)

    st.write(tokenizer.decode(outputs[0], skip_special_tokens=True))
    """
    st.code(code, language="python", line_numbers=True)


###############################################################################
st.subheader("Task 3: Text summarization")

text_summarize = st.text_area(
    "Text to summarize",
    """
I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."

I have a dream that one day on the red hills of Georgia, the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood.

I have a dream that one day even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice.

I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character.

I have a dream today!
""",
)

input_ids_summarize = tokenizer(
    f"summarize: {text_summarize}", return_tensors="pt"
).input_ids
outputs_summarize = model.generate(input_ids_summarize)

st.write(tokenizer.decode(outputs_summarize[0], skip_special_tokens=True))


if st.checkbox("Show code", key=3):
    code = """
    st.subheader("Task 3: Text summarization")

    text_summarize = st.text_area(
        "Text to summarize",
        \"\"\"
    I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."

    I have a dream that one day on the red hills of Georgia, the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood.

    I have a dream that one day even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice.

    I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character.

    I have a dream today!
    \"\"\",
    )

    input_ids_summarize = tokenizer(
        f"summarize: {text_summarize}", return_tensors="pt"
    ).input_ids
    outputs_summarize = model.generate(input_ids_summarize)
    """
    st.code(code, language="python", line_numbers=True)

###############################################################################
st.subheader("Try other tasks")
st.markdown("""
- Text classification/Sentiment analysis
- Text generation
- Question answering
- ...

#### Resources
- https://huggingface.co/docs/transformers/model_doc/t5#resources
- https://towardsdatascience.com/hands-on-googles-text-to-text-transfer-transformer-t5-with-spark-nlp-6f7db75cecff
- https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html
""")

