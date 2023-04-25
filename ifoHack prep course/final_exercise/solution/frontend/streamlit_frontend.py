import pandas as pd
import streamlit as st
import requests
from PIL import Image
import json


def parse_output(json_str):
    # Parse the JSON string
    json_obj = json.loads(json_str)

    # Extract the list of integer values inside the brackets
    values = json_obj["predictions"]

    return values


def request_prediction(data):

    host = 'iris_model_api'
    port = '8080'

    url = f'http://{host}:{port}/invocations'

    headers = {
        'Content-Type': 'application/json',
    }

    r = requests.post(url=url, headers=headers, data=data)

    return r.text


def user_input_features():
    with st.sidebar.form("my_form"):
        f1 = st.slider('sepal length (cm)', 0., 10., 2.5)
        f2 = st.slider('sepal width (cm)', 0., 10., 2.5)
        f3 = st.slider('petal length (cm)', 0., 10., 2.5)
        f4 = st.slider('petal width (cm)', 0., 10., 2.5)
        submitted = st.form_submit_button("Submit")

    data = {'sepal length (cm)': f1,
            'sepal width (cm)': f2,
            'petal length (cm)': f3,
            'petal width (cm)': f4
            }

    df = pd.DataFrame(data, index=[0])
    # Convert DataFrame to dictionary
    data_dict = df.to_dict(orient='list')

    # Create the new dictionary with the required structure
    new_dict = {}
    new_dict["dataframe_split"] = {}
    new_dict["dataframe_split"]["columns"] = list(data_dict.keys())
    new_dict["dataframe_split"]["data"] = [
        list(x) for x in zip(*data_dict.values())]

    # Convert the new dictionary to JSON
    new_json = json.dumps(new_dict)
    return new_json


target = {0.: "Predicted as Iris-Setosa",
          1.: "Predicted as Iris-Versicolour",
          2.: "Predicted as Iris-Virginica"}
target_image = {0.: "Iris-Setosa.jpg",
                1.: "Iris-Versicolour.jpg",
                2.: "Iris-Virginica.jpg"}

data = user_input_features()

output = request_prediction(data)
output = parse_output(output)
output = output[0]

st.subheader('Prediction')
st.write(target[output])

image = Image.open(target_image[output])
st.image(image, caption=target_image[output])
