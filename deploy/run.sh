#!/usr/bin/env bash

# A prerequisite for this script is that miniconda is installed on the server.
# source $HOME/miniconda3/etc/profile.d/conda.sh

set -x

PROJECT="$HOME/ifohack2023"

docker build -t leaderboard $PROJECT/Leaderboard
docker build -t streamlit-workshop "$PROJECT/Workshops/Streamlit Basics and VSCode/"

docker run -d -p 8081:8081 leaderboard
docker run -d -p 8080:8080 streamlit-workshop
