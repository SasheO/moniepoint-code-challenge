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

cursor = conn.cursor()

# create views for all needed queries
top_merchant_query = """
CREATE VIEW top_merchant AS
select merchant_id, sum(amount) AS total_volume from merchant_activity_records
where status  = 'SUCCESS'
group by merchant_id
order by total_volume desc
limit 1;
"""

# Execute the SQL
cursor.execute(top_merchant_query)
conn.commit()  # commit changes

# close connection to database
cursor.close()
conn.close()