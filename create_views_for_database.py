from connect_to_database import *

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

monthly_active_merchants_view = """
CREATE VIEW monthly_active_merchants AS
SELECT TO_CHAR(DATE_TRUNC('month', event_timestamp), 'YYYY-MM') AS month, COUNT(DISTINCT merchant_id) AS monthly_active_merchant_count
FROM merchant_activity_records
-- WHERE status = 'SUCCESS'
WHERE event_timestamp IS NOT NULL
GROUP BY month
HAVING SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) > 0
ORDER BY month;
"""

failure_rates_view = """
CREATE VIEW failure_rates AS
SELECT product, 
    ROUND(
        100.0 * SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) / COUNT(*),
        1
    ) AS failure_rate
FROM merchant_activity_records
where status = 'SUCCESS' or status = 'FAILED'
group by product
order by failure_rate desc;
"""

if __name__ == "__main__":
    # TODO: Execute the SQL queries for each
    # below is how to execute for one
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(top_merchant_view)
    conn.commit()  # commit changes

    # close connection to database
    cursor.close()
    conn.close()