# mysql-fastapi-repo 
My repository for requeting a mysql Netflix database from a fastapi API :  project 3 


# Overview
This is a fastapi API that handles requests to a Mysql netflix database which has been initially loaded from a kaggle csv file. The Netflix database contains a description of Netflix recent titles, shows and episodes with rating, casting, year, country and category information.



# the Input data file
we use the following kaggle csv data file  which containd Netflix movie title descriptions in order to handle and populate our Mysql Netflix database :
```
https://www.kaggle.com/shivamb/netflix-shows/version/5
```


# Data Preparation
The kaggle csv file cannot be used and loaded directly into the netflix database. In this step we handle the kaggle file called " netflix_titles.csv" in order to ignore the quotation marks and generate a csv file called "titles.csv" with fields separated by semi columns. 

You have to install pandas library, download the csv file from the above url (or from the csv_preparation folder) and then run the following python file :
```
python3 prepare_csv.py
```


# Using Mysql docker image as our Netflix Database environment
In this step we import and run a Mysql docker image in order to use it as our Netflix database environment
use the following docker command line in order to create a mysql container
```
docker run --name mysql_database -e MYSQL_ROOT_PASSWORD=1234 -p 3306:3306 -p 33060:33060 -d mysql:8.0 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --local-infile=1
```

# Loading the csv data file into our Netflix database
In this step we create a database called Netflix and then load the csv kaggle file into a relational database table called "titles" using the "'LOAD DATA LOCAL INFILE" sql order.
we use the following python scripts to create and populate the database table.


# How to create and populate the database in your machine using a python virtual environment

first create a new python virtual environment, install the requirements (see database_creation_populating folder) :
```
pip install -r requirements_sql.txt 
```

then copy the titles.csv" file in your environment  and run the following : 

```
python3 create_database.py
python3 create_table_from_csv.py
```


# The Table Schema and Content
The movie titles (from the csv data file) are now loaded in the "titles" table. Here is an example of the table schema and content :
```
"SHOW_ID": "s5"
"TYPE": "TV Show"
"TITLE": "Kota Factory"
"DIRECTOR" : ""
"CAST": "Mayur More, Jitendra Kumar, Ranjan Raj, Alam Khan, Ahsaas Channa, Revathi Pillai, Urvi Singh, Arun Kumar"
"COUNTRY": "India"
"DATE_ADDED": "September 24, 2021"
"RELEASE_YEAR": "2021"
"RATING": "TV-MA"
"DURATION": "2 Seasons"
"LISTED_IN": "International TV Shows, Romantic TV Shows, TV Comedies"
"DESCRIPTION": "In a city of coaching centers known to train India’s finest collegiate minds, an earnest but unexceptional student and his friends navigate campus life."                           
```




# The Fast API image
We use a Fastapi API in order to query our Netflix Mysql database
For example, we can display some movie titles from the database or find the country where a movie has been made
The FAst API image is also created and puched to the DockerHub repository : 
```
rocchdi/apimysql:1.0.0
```
You can check the Dockerfile of the API and the requirements.txt used to create the image
You can also check the API code (main.py)


# How to use and test the Fast API in your machine using a python virtual environment

create a new python virtual environment, install the requirements :  

```
pip install -r requirements.txt
```
Copy the main.py file (see fastapi_mysql folder)
The Mysql database container is supposed to be running in your machine and the Netflix database created and populated. 

set the mysql_password variable
```
export mysql_password=1234
```

To run the API : 
```
uvicorn main:apimysql --reload
```
To test the API: redirect the port 8000, and use the url :
```
http://localhost:8000/docs
```
Choose the following endpoint :
```
/titles
```
This will return the 10 first movie titles in the Netflix database

you can also check the other endpoints :
```
/home : Welcome message
/recent : 10 recent titles from 2021
/bytype : number of titles by type
/byrating : number of titles by rating
/bycountry : number of titles by country 
/india : 10 titles from india 

```



# How to use The Docker compose to reload and initilize the database from the csv file 

In the mysql_docker_compose folder you can find the following file :
```
setup.sh
```
it contains the cammands that allow you use the mysql image and run docker-compose to create and populate the Netflix database.
the docker compose displays a SUCESS status if all the steps are successfull.


