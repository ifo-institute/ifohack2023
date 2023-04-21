
### Verify that Docker Engine is installed correctly by running the hello-world Docker image in terminal:

>  docker run hello-world

### Create a Dockerfile:

1.  A Dockerfile must start with a FROM instruction. It sets the Base Image (think OS) for the container:

> FROM python:3.9-slim

2.  The WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile . Let’s set it to app/ :

> WORKDIR /app

3.  Install git so that we can clone the app code from a remote repo:
```
   RUN apt-get update && apt-get install -y \
        build-essential \
        curl \
        software-properties-common \
        git \
        && rm -rf /var/lib/apt/lists/*
```
4a. Clone your code that lives in a remote repo to WORKDIR:

> RUN git clone https://github.com/streamlit/streamlit-example.git .

Once cloned, the directory of WORKDIR will look like the following:
```
app/
- requirements.txt
- streamlit_app.py
```

4b.     If your code lives in the same directory as the Dockerfile, copy all your app files from your server into the container, including 
        streamlit_app.py, requirements.txt, etc, by replacing the git clone line with:

>     COPY . .

5. Install your app’s Python dependencies from the cloned requirements.txt in the container:

>     RUN pip3 install -r requirements.txt

6. The EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime. 
   Your container needs to listen to Streamlit’s (default) port 8501:

>     EXPOSE 8501

7. The HEALTHCHECK instruction tells Docker how to test a container to check that it is still working. Your container needs to listen to Streamlit’s (default) port 8501:

>     HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

8.  An ENTRYPOINT allows you to configure a container that will run as an executable. 
    Here, it also contains the entire streamlit run command for your app, so you don’t have to call it from the command line:

>     ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]    

### Build a Docker image

1.  The docker build command builds an image from a Dockerfile . Run the following command from the app/ directory on your server to build the image:

>     docker build -t streamlit .

The -t flag is used to tag the image. Here, we have tagged the image streamlit. If you run:

>     docker images

You should see a streamlit image under the REPOSITORY column. For example:
```
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
streamlit    latest    70b0759a094d   About a minute ago   1.02GB
```
### Run the Docker container

1.  Now that you have built the image, you can run the container by executing:

>      docker run -p 8501:8501 streamlit

The -p flag publishes the container’s port 8501 to your server’s 8501 port.