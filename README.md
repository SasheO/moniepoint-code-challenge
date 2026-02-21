# moniepoint-code-challenge

## About
This directory contains code and sample data M. S. Ojuba for the moniepoint code challenge.


## How to Use
1. Load cleaned data into a PostgreSQL database. The as
1. Create a .env file with the following values:
```
    DATABASE='''enter database name'''
    USER='''enter user name'''
    PASSWORD='''enter password'''
    TABLE_NAME='''enter table name with cleaned data'''
```
2. Run `create_views_for_database.py` to create different views that will be queried by the server. The views correspond to what was requested in the specifications document. The SQL query for each view can be found in the `views/` folder.
3. Run `run_server.py` to set up and run a local server.

You can query the various endpoints this way.

## Assumptions 
I first cleaned the data using python, then loaded the data into a PostgreSQL dataset. The data cleaning involved changing invalid values in the "amount" column to 0 and skipping records where "event_timestamp" value was "NOT-A-DATE".

## Problem Solving

I first looked into the dataset to get an idea of what I was working with. I cleaned the dataset in python with clean_data.py code. 

Then I imported a few CSV files into PostgreSQL database using the app's GUI and command line. I then created SQL views for each endpoint which I documented in the `views/` folder and ran in python with create_views_for_database.py. I chose views because they create a virtual table with the required results that can be easily called.

Then I created a Flask server run on port 8080 on the local host with the required endpoints that returned data in the right format. The function for each endpoint calls a view without needing complicated SQL queries.

With this method, 
* more SQL views can be programmatically added by including a new .txt file in the `views/` folder.
* New endpoints can be added to the `run_server.py` folder.


## Descriptions of Sub Folders/Files

`clean_data/`: This folder contains the data that has been cleaned.

`sample_data/`: This folder contains the sample data given to me.

`views/`: This folder contains .txt files each creating a new view in the database.

`clean_data.py`: This file generated the files in clean_data/ folder from the ones in sample_data/

`connect_to_database.py`: This file loads environment variables and has a function get_db_connection() which can be used to open a database connection.

`.env`: This file is hidden via .gitignore, but contains the database name as DATABASE, user name as USER, and password as PASSWORD.

`run_server.py`: This file runs a Flask server on localhost, port 8080 with the endpoints.