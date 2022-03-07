import sqlalchemy
from sqlalchemy import Table, Column, SmallInteger, Integer, String, MetaData, create_engine, text, inspect
from sqlalchemy import exc
import pymysql as mysql



def populate_db():



    # creating a connection to the database
    mysql_address='mysql_database'
    mysql_port='3306'
    mysql_user = 'root'
    mysql_password = '1234'
    database_name = 'netflix'


    mysql_url='{address}:{port}'.format(address=mysql_address, port=mysql_port)



    # recreating the URL connection
    #connection_url = 'mysql+mysqlconnector://{user}:{password}@{url}/{database}'.format(
    connection_url = 'mysql+pymysql://{user}:{password}@{url}/{database}?charset=utf8&local_infile=1'.format(
        user=mysql_user,
        password=mysql_password,
        url=mysql_url,
        database=database_name
    )      

    # creating the connection
    engine = create_engine(connection_url,echo=True)



    #informations table
    meta=MetaData()

    titles = Table(

        'titles', meta,
        Column('SHOW_ID', String(255), primary_key=True),
        Column('TYPE', String(255)),
        Column('TITLE', String(255), nullable=False),
        Column('DIRECTOR', String(255)),
        Column('CAST', String(255)),
        Column('COUNTRY', String(255)),
        Column('DATE_ADDED', String(255)),
        Column('RELEASE_YEAR', SmallInteger, nullable=False),
        Column('RATING', String(20)),
        Column('DURATION', String(255)),
        Column('LISTED_IN', String(255)),
        Column('DESCRIPTION', String(255)),

    )   

    meta.create_all(engine)



    # load csv file to table titles
    try:
        conn = engine.connect()
        #sql=text('LOAD DATA LOCAL INFILE "titles.csv" INTO TABLE titles FIELDS TERMINATED BY ";" LINES TERMINATED BY "\\r\\n" STARTING BY "s"  IGNORE 1 LINES;')
        sql=text('LOAD DATA LOCAL INFILE "titles.csv" INTO TABLE titles FIELDS TERMINATED BY ";" LINES TERMINATED BY "\\n" STARTING BY "s" IGNORE 1 LINES;')
        res=conn.execute(sql)
        print("Database Table titles is loaded from csv file")

        conn = engine.connect()
        sql=text('SELECT * FROM titles limit 10;')
        res=conn.execute(sql)
        res=res.fetchall()
        for i in res:
            print(i)


    except exc.SQLAlchemyError as e:
        print("Error while connecting to MySQL", e)

