import pandas as pd
import streamlit as st
from PIL import Image
from utils import init

init()

logo = Image.open("logo.png")
st.title(":blue[ifo] Hack 2023 Leaderboard")

#uploaded_file = st.file_uploader("Choose a file", type="csv")
#if uploaded_file is not None:

df = pd.read_csv("./sample_scores.csv")
df["members"] = df["members"].str.split(";")

df["score"] = df["score"].round(2)
df.sort_values(by="score", ascending=False, inplace=True, ignore_index=True)

first_place = df.iloc[0]
second_place = df.iloc[1]
third_place = df.iloc[2]

col1, col2, col3 = st.columns(3)
col1.metric(
    label=f":first_place_medal: : **{first_place['team']}**",
    value=first_place["score"],
    delta=round(first_place["score"] - second_place["score"], 2),
)
col2.metric(
    label=f":second_place_medal: : **{second_place['team']}**",
    value=second_place["score"],
    delta=round(second_place["score"] - first_place["score"], 2),
)
col3.metric(
    f":third_place_medal: : **{third_place['team']}**",
    value=third_place["score"],
    delta=round(third_place["score"] - first_place["score"], 2),
)

st.dataframe(
    df.style.format(subset=["score"], formatter="{:.2f}"),
    use_container_width=True,
    height=(len(df) + 1) * 35 + 3,
)
