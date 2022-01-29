import sqlalchemy
from sqlalchemy import Table, Column, SmallInteger, String, MetaData, create_engine, text, inspect
from sqlalchemy import exc
mport pymysql as mysql


# creating a connection to the database
mysql_url = '0.0.0.0:3306' 
mysql_user = 'root'
mysql_password = '1234'
database_name = 'netflix'

# recreating the URL connection
connection_url = 'mysql+pymysql://{user}:{password}@{url}'.format(
    user=mysql_user,
    password=mysql_password,
    url=mysql_url,
    database=database_name
)

# creating the connection
engine = create_engine(connection_url,echo=True)



try:
    sql=text('DROP TABLE IF EXISTS titles;')
    res = engine.execute(sql)
    print('table titles supprimée')

except exc.SQLAlchemyError as e:
    print("Error while connecting to MySQL", e)

