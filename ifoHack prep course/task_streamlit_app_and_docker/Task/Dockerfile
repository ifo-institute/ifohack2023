# app/Dockerfile

#set the Base Image (python:3.9-slim) for the container
#TODO

#set the working directory
#TODO

#your code lives in the same directory as the Dockerfile, copy all your app files from your server into the container
#TODO

#Install your app’s Python dependencies from the cloned requirements.txt in the container
RUN pip3 install -r requirements.txt

#inform Docker that the container listens on 8502 port at runtime
#TODO

HEALTHCHECK CMD curl --fail http://localhost:8502/_stcore/health

ENTRYPOINT ["streamlit", "run", "application.py", "--server.port=8502", "--server.address=0.0.0.0"]