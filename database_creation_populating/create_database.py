import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy import exc


# creating a connection to the database
mysql_url = '0.0.0.0:3306' 
mysql_user = 'root'
mysql_password = '1234' 

# recreating the URL connection
connection_url = 'mysql+mysqlconnector://{user}:{password}@{url}'.format(
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

