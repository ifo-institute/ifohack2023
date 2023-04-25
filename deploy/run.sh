#!/usr/bin/env bash

# A prerequisite for this script is that miniconda is installed on the server.
# source $HOME/miniconda3/etc/profile.d/conda.sh

set -x

PROJECT="$HOME/ifohack2023"
APP1="$PROJECT/Leaderboard"
APP2="$PROJECT/Workshops/Streamlit Basics and VSCode"


if { conda env list | grep "ifohack.live"; } >/dev/null 2>&1; then
    conda activate "ifohack.live"
else
    conda create -y -n ifohack.live pip
    conda activate "ifohack.live"
fi

pip install -r "$APP1/requirements.txt"
pip install -r "$APP2/requirements.txt"

streamlit run "$APP1/app.py" --server.port 8081 > /dev/null 2>&1 &
streamlit run "$APP2/Welcome.py" --server.port 8080 > /dev/null 2>&1 &
