## Task: Deploying a Streamlit App with Docker

### [Download Docker](https://www.docker.com/products/docker-desktop/)

#### change directory to task_streamlit_app_and_docker through terminal using:

>   cd task_streamlit_app_and_docker

### run following commands:

>   docker build -t streamlit_task -f Dockerfile .

>   docker run -p 8502:8502 streamlit_task

If all went well, you should see an output similar to the following:
```
2023-04-13 12:27:32.483 INFO    matplotlib.font_manager: generated new fontManager

Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.


  You can now view your Streamlit app in your browser.

  URL: http://0.0.0.0:8502
```
-   you can view the streamlit app in your browser:
    
>   URL: http://localhost:8502/


