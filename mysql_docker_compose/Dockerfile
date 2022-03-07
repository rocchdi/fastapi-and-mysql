FROM debian:latest

ADD requirements_mysql.txt create_db.py populate_db.py titles.csv  init_db.py ./

RUN apt-get update && apt-get install python3-pip -y && pip install -r requirements_mysql.txt && export mysql_password=1234

CMD python3 init_db.py
