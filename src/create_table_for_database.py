from connect_to_database import *

sql_create_table_query ='''
DROP table IF EXISTS merchant_activity_records;

CREATE TABLE __table_name__ (
event_id UUID NOT NULL UNIQUE,
merchant_id VARCHAR(15) not null,
event_timestamp TIMESTAMP,
product VARCHAR(30), -- Product category: POS, AIRTIME, BILLS, CARD_PAYMENT, SAVINGS, MONIEBOOK, KYC
event_type VARCHAR(30), -- Type of activity
amount DECIMAL, -- Transaction amount in NGN (0 for non-monetary)
status VARCHAR(30), -- One of: SUCCESS, FAILED, PENDING
channel VARCHAR(30), -- One of: POS, APP, USSD, WEB, OFFLINE
region VARCHAR(30), -- Merchant's operating region
merchant_tier VARCHAR(30), -- KYC tier: STARTER, VERIFIED, PREMIUM
PRIMARY KEY (event_id));
'''


if __name__ == "__main__":
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(sql_create_table_query.replace("__table_name__", table_name))
    conn.commit()

    # close connection to database
    cursor.close()
    conn.close()