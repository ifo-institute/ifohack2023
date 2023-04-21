
import streamlit as st

class MultiAppfunc:

    def __init__(self):
        self.apps = []

    def add_app(self, modeltitle, func):

        self.apps.append({
            "modeltitle": modeltitle,
            "function": func
        })

    def run(self):

        app = st.selectbox(
            'Model',
            self.apps,
            format_func=lambda app: app['modeltitle'])

        app['function']()
