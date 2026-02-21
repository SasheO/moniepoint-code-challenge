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
top_merchant_view = """
CREATE VIEW top_merchant AS
select merchant_id, sum(amount) AS total_volume from merchant_activity_records
where status  = 'SUCCESS'
group by merchant_id
order by total_volume desc
limit 1;
"""

product_adoption_view = """
CREATE VIEW product_adoption AS
SELECT product, COUNT(DISTINCT merchant_id) AS merchant_product_count
FROM merchant_activity_records
group by product
order by merchant_product_count desc;
"""

kyc_funnel_view = """
CREATE VIEW kyc_funnel AS
SELECT event_type, COUNT(DISTINCT merchant_id) AS successful_kyc_event_count
FROM merchant_activity_records
where product = 'KYC' and status = 'SUCCESS'
group by event_type;
"""

# TODO: Execute the SQL queries for each
# below is how to execute for one
cursor.execute(top_merchant_view)
conn.commit()  # commit changes

# close connection to database
cursor.close()
conn.close()