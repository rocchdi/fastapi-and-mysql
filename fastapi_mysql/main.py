from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.engine import create_engine
from sqlalchemy import MetaData, text, inspect
from sqlalchemy import exc
from fastapi import  Request
from fastapi.responses import JSONResponse
import pymysql as mysql
import os








class MyException(Exception):
    def __init__(self, name: str):
        self.name = name



# creating a FastAPI server
apimysql = FastAPI(
    title='Netflix API',
    description="API d interrogation de la base mysql netflix contenant des titres de films et d episodes",
    version="1.0.1",
    openapi_tags=[
    {
        'name': 'home',
        'description': 'Welcome message function'
    },
    {
        'name': 'titles',
        'description': 'fonction qui permet d afficher les premiers titres dans la base de données '
    },

]
    )



@apimysql.exception_handler(MyException)
async def my_exception_handler(request: Request, exc: MyException):
    return JSONResponse(
        status_code=500,
        content={"message": f"erreur {exc.name} "},
    )




# creating a connection to the database
mysql_url = '127.0.0.1:3306'
mysql_user = 'root'
database_name = 'netflix'


#retreive the secret env variable as mysql database password
mysql_password = os.getenv("mysql_password")


# recreating the URL connection
connection_url = 'mysql+pymysql://{user}:{password}@{url}/{database}'.format(
    user=mysql_user,
    password=mysql_password,
    url=mysql_url,
    database=database_name
)






# creating a User class
class titles(BaseModel):
    title_id: int = 0
    title: str = ''
    description: str = ''


@apimysql.get('/status')
async def get_status():
    """Returns 1
    """
    return 1



@apimysql.get('/titles')
def get_titles():
 

    """
    retourne les titres neflix dans la base mysql
    """

    #connection_url = 'mysql+pymysql://root:1234@127.0.0.1:3306/netflix'
    
    engine = create_engine(connection_url,echo=True)
   

    #if not engine:
    #    raise MyException(name="connection problem")
    #return 3 

    try:
        conn = engine.connect()
        sql=text('SELECT * FROM titles limit 10;')
        res=conn.execute(sql)
        #print(res.fetchall())

        results=res.fetchall()

        if not results:
            raise MyException(name="titles not found")
        return results


    except exc.SQLAlchemyError as e:
        print("Error while connecting to MySQL", e)



@apimysql.get('/recent')
def get_recent():


    """
    retourne les 10 recent titles de 2021
    """

    engine = create_engine(connection_url,echo=True)


    try:
        conn = engine.connect()
        sql=text("SELECT * FROM titles WHERE RELEASE_YEAR='2021' limit 10;")
        res=conn.execute(sql)

        results=res.fetchall()

        if not results:
            raise MyException(name="titles not found")
        return results


    except exc.SQLAlchemyError as e:
        print("Error while connecting to MySQL", e)




@apimysql.get('/bytype')
def get_bytype():


    """
    retourne number of titles by type 
    """

    engine = create_engine(connection_url,echo=True)


    try:
        conn = engine.connect()
        sql=text('SELECT TYPE, count(*) as p FROM  titles GROUP BY TYPE ORDER BY p;')
        res=conn.execute(sql)

        results=res.fetchall()

        if not results:
            raise MyException(name="titles not found")
        return results


    except exc.SQLAlchemyError as e:
        print("Error while connecting to MySQL", e)




@apimysql.get('/byrating')
def get_byrating():


    """
    retourne number of titles by rating  
    """

    engine = create_engine(connection_url,echo=True)


    try:
        conn = engine.connect()
        sql=text('SELECT RATING, count(*) as p FROM  titles GROUP BY RATING  ORDER BY p;')
        res=conn.execute(sql)

        results=res.fetchall()

        if not results:
            raise MyException(name="titles not found")
        return results


    except exc.SQLAlchemyError as e:
        print("Error while connecting to MySQL", e)




@apimysql.get('/bycountry')
def get_bycountry():


    """
    retourne number of titles by country 
    """

    engine = create_engine(connection_url,echo=True)


    try:
        conn = engine.connect()
        sql=text('SELECT COUNTRY, count(*) as p FROM  titles GROUP BY COUNTRY  ORDER BY p;')
        res=conn.execute(sql)

        results=res.fetchall()

        if not results:
            raise MyException(name="titles not found")
        return results


    except exc.SQLAlchemyError as e:
        print("Error while connecting to MySQL", e)




@apimysql.get('/india')
def get_india():


    """
    retourne 10 titles from india 
    """

    engine = create_engine(connection_url,echo=True)


    try:
        conn = engine.connect()
        sql=text("SELECT * FROM titles WHERE COUNTRY='India' limit 10;")
        res=conn.execute(sql)

        results=res.fetchall()

        if not results:
            raise MyException(name="titles not found")
        return results


    except exc.SQLAlchemyError as e:
        print("Error while connecting to MySQL", e)






