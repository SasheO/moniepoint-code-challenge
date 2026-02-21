from dotenv import load_dotenv
import os
import psycopg2 

# get environment variables
load_dotenv()
database = os.getenv("DATABASE")
user = os.getenv("USER")
password= os.getenv("PASSWORD")
table_name = os.getenv("TABLE_NAME")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database=database,
    user=user,
    password=password
)