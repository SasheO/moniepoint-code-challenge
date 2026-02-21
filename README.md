# moniepoint-code-challenge

## About
This directory contains code and sample data M. S. Ojuba for the moniepoint code challenge.

## Assumptions 
I first cleaned the data using python, then loaded the data into a PostgreSQL dataset. The data cleaning involved changing invalid values in the "amount" column to 0.

## How to Use
With the database and table set up, this is what you need to do to run the server:
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

## Descriptions of Sub Folders/Files

`clean_data/`: This folder contains the data that has been cleaned.

`sample_data/`: This folder contains the sample data given to me.

`views/`: This folder contains .txt files each creating a new view in the database.

`clean_data.py`: This file generated the files in clean_data/ folder from the ones in sample_data/

`connect_to_database.py`: This file loads environment variables and has a function get_db_connection() which can be used to open a database connection.

`.env`: This file is hidden via .gitignore, but contains the database name as DATABASE, user name as USER, and password as PASSWORD.

`run_server.py`: This file runs a Flask server on localhost, port 8080 with the endpoints.