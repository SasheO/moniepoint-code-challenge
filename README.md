# moniepoint-code-challenge

## About
This directory contains code and sample data Shalom Ojuba used for the moniepoint code challenge.

## Prerequisites
* Python >=3.10
* Python libraries found in `src/requirements.txt`

## Build & Run
1. Clone the github repository onto your local device. Place your sample data in `data/` folder.
2. Create a .env file with the following values in the main directory:
```
    DATABASE='''enter database name'''
    USER='''enter user name'''
    PASSWORD='''enter password'''
    TABLE_NAME='''enter table name with cleaned data'''
```
3. In the command line, navigate to the `src/` folder.
4. Run `pip install -r requirements.txt` to install all required Python libraries.
5. Create a database in PostgreSQL named the same as the DATABASE value of the .env file.
6. Run `python create_table_for_database.py` to create a new table named the TABLE_NAME value of the .env file.
7. Run `python clean_data.py` to clean up the data.
8. Run `python load_data.py` to load the cleaned data into the PostgreSQL database.
9. Run `python create_views_for_database.py` to create different SQL table views according to the API endpoints specifications.
10. Run `python run_server.py` to set up and run a local server that fits the API endpoints specifications.

Now, you can query the various endpoints on localhost, port 8080. To do so with Python, Run `python run_server.py` in the `src/` folder.

## API Endpoints (Port 8080)

| Endpoint | Description |
|----------|-------------|
| `GET /analytics/top-merchant` | Merchant with highest total volume |
| `GET /analytics/monthly-active-merchants` | Unique merchants per month |
| `GET /analytics/product-adoption` | Unique merchants per product |
| `GET /analytics/kyc-funnel` | KYC conversion funnel |
| `GET /analytics/failure-rates` | Failure rate by product |

## Assumptions 
* Rows with "invalid" values in the "amount" column were skipped.
* Records where "event_timestamp" value was "NOT-A-DATE" or null were skipped.
* Records with null "merchant_id" were skipped.

## Problem Solving Methodology

I first looked into the dataset to get an idea of what I was working with. I cleaned the dataset in python with `clean_data.py` code. 

Then I imported a few CSV files into PostgreSQL database using the app's GUI and command line. I then created SQL views for each endpoint which I documented in the `views/` folder and ran in python with `create_views_for_database.py`. I chose views because they create a virtual table with the required results that can be easily called.

Then I created a Flask server run on port 8080 on the local host with the required endpoints that returned data in the right format. The function for each endpoint calls a view without needing complicated SQL queries.

With this method, 
* more SQL views can be programmatically added by including a new .txt file in the `views/` folder.
* New endpoints can be added to the `run_server.py` folder.


## Descriptions of Sub Folders/Files

`.env`: This file is hidden via .gitignore, but contains the database name as DATABASE, user name as USER, and password as PASSWORD, and table_name as TABLE_NAME.

`clean_data/`: This folder contains the data that has been cleaned.

`data/`: This folder contains the sample dirty data initially provided.

`views/`: This folder contains .txt files each containing descriptively named SQL queries to create a new view in the database.

`src/`: This folder contains source code.

`src/clean_data.py`: This file generated the files in clean_data/ folder from the ones in sample_data/

`src/connect_to_database.py`: This file loads environment variables such as and has a function get_db_connection() which can be used to open a database connection.

`src/create_table_for_database.py`: This creates a table with the name given in the .env file in the database.

`src/create_views_for_database.py`: This file creates view in the database described by the .env file.

`src/load_data.py`: This file loads data from clean_data/ into the table in the database described by the .env file.

`src/requirements.txt`: This contains a list of required Python libraries to run the application in this repo.

`src/run_server.py`: This file runs a Python Flask server with the endpoints specified in the question on localhost with port 8080.

