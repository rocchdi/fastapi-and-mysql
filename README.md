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
The kaggle csv file cannot be used and loaded directly into the netflix database. In this step we handle the kaggle file in order to ignore some charaters and generate a csv file with fields
separated by semi columns


# Loading the csv file into our Netflix database
In this step we create a database called Netflix and then load the csv kaggle file into a table called titles using the "'LOAD DATA LOCAL INFILE" sql order.
we use python scripts in order to populate the database table

```
LOAD DATA LOCAL INFILE "titles.csv" INTO TABLE titles FIELDS TERMINATED BY ";" LINES TERMINATED BY "\\n" STARTING BY "s" IGNORE 1 LINES;
```

# The Database initial schema
The titles from the csv file are loaded is the following relational database table. Here is an example of the table content :
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


# Database Modeling from the titles table
In order to separate the different information stored in the titles table we use the following database tables :
```
show table (SHOW_ID (PRIMARY KEY), TYPE, TITLE, COUNTRY, DATE_ADDED, RELEASE_YEAR, DURATION, DESCRIPTION)
Rating table (SHOW_ID (PRIMARY KEY), RATING)
crew table (SHOW_ID (PRIMARY KEY), DIRECTOR, CAST) 
```


# The Fast API image
The FAst API image is already created and puched to the DockerHub repository : 
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
Copy  all files in the projet root , the .py files (the code)
and also the .csv files (netflix data) in your machine. To run the API : 
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
/request : to enter a sql request order

```



# How to use The Docker compose to reload and initilize the database from the csv file 

In the docker folder you can find the following file :
```
setup.sh
```
it contains the cammands that allow you use the mysql image and run docker-compose to create and populate thye Netflix database.
the docker compose displays a SUCESS status if all the steps are successfull.


