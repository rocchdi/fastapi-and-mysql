import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy import exc
import pymysql as mysql


def create_db():

    # creating a connection to the database
    mysql_address='mysql_database'
    mysql_port='3306'
    mysql_user = 'root'
    mysql_password = '1234'


    mysql_url='{address}:{port}'.format(address=mysql_address, port=mysql_port)

    #mysql_url = '0.0.0.0:3306' 

    # recreating the URL connection
    #connection_url = 'mysql+mysqlconnector://{user}:{password}@{url}'.format(
    connection_url = 'mysql+pymysql://{user}:{password}@{url}'.format(
        user=mysql_user,
        password=mysql_password,
        url=mysql_url,
    )

    # creating the connection
    engine = create_engine(connection_url,echo=True)

    try:
        #creating the database
        conn = engine.connect()
        sql=text("CREATE DATABASE netflix;")
        res=conn.execute(sql)
        print("Database is created")

    except exc.SQLAlchemyError as e:
        print("Error while connecting to MySQL", e)

