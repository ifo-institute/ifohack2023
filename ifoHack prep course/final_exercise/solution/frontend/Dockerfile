FROM python:3.11.2

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8502

HEALTHCHECK CMD curl --fail http://localhost:8502/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_frontend.py", "--server.port=8502", "--server.address=0.0.0.0"]
