FROM python:3.11.2


#set the working directory
#TODO

#your code lives in the same directory as the Dockerfile, copy all your app files from your server into the container
#TODO

RUN pip3 install -r requirements.txt

EXPOSE 8502

HEALTHCHECK CMD curl --fail http://localhost:8502/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_frontend.py", "--server.port=8502", "--server.address=0.0.0.0"]
