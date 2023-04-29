import pandas as pd
import streamlit as st
import numpy as np

from utils import init

# np.random.seed(seed=100)

init()

###############################################################################
st.title(":blue[Main] Concepts")

if st.checkbox("Show imports"):
    code = """
    import pandas as pd
    import streamlit as st
    import numpy as np

    # np.random.seed(seed=100)
    """
    st.code(code, language="python", line_numbers=True)

###############################################################################
st.subheader("Running a streamlit app")

st.markdown("""
With an entrypoint file called `app.py`
- `streamlit run app.py`
""")

st.subheader("Display a dataframe")

df = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
    }
)

st.write(df)


if st.checkbox("Show code", key=1):
    code = """
    st.subheader("Display a dataframe")

    df = pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )

    st.write(df)
    """
    st.code(code, language="python", line_numbers=True)

###############################################################################
st.subheader("Draw a line chart")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

if st.checkbox("Show code", key=2):
    code = """
    st.subheader("Draw a line chart")

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
    """
    st.code(code, language="python", line_numbers=True)

###############################################################################
st.subheader("Widgets")

left_column, right_column = st.columns(2)
left_column.button('Press me!')

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

if st.checkbox("Show code", key=3):
    code = """
    st.subheader("Widgets")

    left_column, right_column = st.columns(2)
    left_column.button('Press me!')

    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")
    """
    st.code(code, language="python", line_numbers=True)

###############################################################################
st.subheader("Multipages")

st.markdown("""
- Create a `pages` subfolder
- Add python files insde the `pages` subfolder:
    - `pages/1_Main_Concepts.py`
    - `pages/2_NLP_App.py`
- Rerun the app: `streamlit run app.py`
""")


###############################################################################
st.markdown("""
#### Resources
- https://docs.streamlit.io/library/get-started/main-concepts
""")
