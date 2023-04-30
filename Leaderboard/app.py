import os

import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from PIL import Image
from utils import init
from yaml.loader import SafeLoader

init()

with open("config.yml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"],
)

name, authentication_status, username = authenticator.login("Login", "sidebar")

logo = Image.open("logo.png")
st.title(":blue[ifo] Hack 2023 Leaderboard")

filename = "sample_scores.csv"


def highlight_cols(_):
    return "color: blue"


if st.session_state["authentication_status"]:
    authenticator.logout("Logout", "main")
    uploaded_file = st.file_uploader("Choose a file", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        df.to_csv(filename, index=False)

if os.path.isfile(filename):
    df = pd.read_csv(filename)
    df["members"] = df["members"].str.split(";")

    df["score"] = df["score"].round(4)

    df_ifo = df.query("challenge=='#ifo'")
    df_kfw = df.query("challenge=='#KfW'")
    df_dlr = df.query("challenge=='#DLR'")
    df_ifo.sort_values(by="score", ascending=False, inplace=True, ignore_index=True)
    df_kfw.sort_values(by="score", ascending=False, inplace=True, ignore_index=True)
    df_dlr.sort_values(by="score", ascending=False, inplace=True, ignore_index=True)

    n_submissions = len(df)

    first_place = df.iloc[0]
    if n_submissions >= 3:
        second_place = df.iloc[1]
        third_place = df.iloc[2]

        # col1, col2, col3 = st.columns(3)
        # col1.metric(
        #     label=f":first_place_medal: : **{first_place['team']}**",
        #     value=first_place["score"],
        #     delta=round(first_place["score"] - second_place["score"], 2),
        # )
        # col2.metric(
        #     label=f":second_place_medal: : **{second_place['team']}**",
        #     value=second_place["score"],
        #     delta=round(second_place["score"] - first_place["score"], 2),
        # )
        # col3.metric(
        #     f":third_place_medal: : **{third_place['team']}**",
        #     value=third_place["score"],
        #     delta=round(third_place["score"] - first_place["score"], 2),
        # )

    st.subheader("ifo Challenge, accuracy")
    st.dataframe(
        df_ifo.style.applymap(
            highlight_cols, subset=pd.IndexSlice[:, ["challenge"]]
        ).format(subset=["score"], formatter="{:.4f}"),
        use_container_width=True,
        height=(len(df_ifo) + 1) * 35 + 3,
    )
    st.subheader("KfW Challenge, F1")
    st.dataframe(
        df_kfw.style.applymap(
            highlight_cols, subset=pd.IndexSlice[:, ["challenge"]]
        ).format(subset=["score"], formatter="{:.4f}"),
        use_container_width=True,
        height=(len(df_kfw) + 1) * 35 + 3,
    )
    st.subheader("DLR Challenge, R squared")
    st.dataframe(
        df_dlr.style.applymap(
            highlight_cols, subset=pd.IndexSlice[:, ["challenge"]]
        ).format(subset=["score"], formatter="{:.4f}"),
        use_container_width=True,
        height=(len(df_dlr) + 1) * 35 + 3,
    )
