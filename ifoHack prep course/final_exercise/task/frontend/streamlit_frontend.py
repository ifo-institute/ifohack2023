import pandas as pd
import streamlit as st
import requests
from PIL import Image
import json

def dataframe_to_json(df):
    # Convert DataFrame to dictionary
    data_dict = df.to_dict(orient='list')

    # Create the new dictionary with the required structure
    new_dict = {}
    new_dict["dataframe_split"] = {}
    new_dict["dataframe_split"]["columns"] = list(data_dict.keys())
    new_dict["dataframe_split"]["data"] = [list(x) for x in zip(*data_dict.values())]

    # Convert the new dictionary to JSON
    new_json = json.dumps(new_dict)
    return new_json


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
        # make a slider for each feature input
        #TODO


        submitted = st.form_submit_button("Submit")

    #build a dictionnary where we have the feature names as keys and the inserted input as values
    data = {
            # TODO
            }

    #build a dataframe from the data dectionnary and call it df
    #TODO

    new_json = dataframe_to_json(df)

    return new_json


target = {0.: "Predicted as Iris-Setosa",
          1.: "Predicted as Iris-Versicolour",
          2.: "Predicted as Iris-Virginica"}
target_image = {0.: "Iris-Setosa.jpg",
                1.: "Iris-Versicolour.jpg",
                2.: "Iris-Virginica.jpg"}

# get the input data inserted from the app user, save it in a variable, request prediction from the mlflow API and parse the returned message
#TODO


#print 'Prediction' as a subheader and write the target value below
#Hint: use the target dictionnary above
#TODO



image = Image.open(target_image[output])

#print the image for the corresponding target flower with a caption
#Hint: https://docs.streamlit.io/library/api-reference/media/st.image
#TODO
