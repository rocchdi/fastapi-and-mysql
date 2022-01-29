FROM ubuntu:20.04

ADD requirements.txt main.py ./

RUN apt update && apt install python3-pip fastapi -y && pip install -r requirements.txt

EXPOSE 8000

CMD uvicorn main:apimysql --host 0.0.0.0 
