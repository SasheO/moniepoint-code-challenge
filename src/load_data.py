import os
import pandas as pd
import psycopg2
from psycopg2 import sql
from connect_to_database import *

# Define your CSV directory
csv_directory = "../clean_data/"

# Establish connection to PostgreSQL
conn = get_db_connection()
cursor = conn.cursor()

def load_csv_to_postgresql(csv_file, table_name):
    df = pd.read_csv(csv_file)
    
    # Use the `copy_from` method of psycopg2 to load data
    with open(csv_file, 'r') as f:
        next(f)  # Skip the header row
        cursor.copy_from(f, table_name, sep=',', null='')

    conn.commit()  

if __name__=="__main__":
    # Loop over all CSV files in the directory
    for csv_file in os.listdir(csv_directory):
        if csv_file.endswith(".csv"):
            # Construct the full file path
            full_csv_path = os.path.join(csv_directory, csv_file)
            
            print(f"Loading {csv_file} into {table_name}...")
            
            load_csv_to_postgresql(full_csv_path, table_name)

    # Close connection
    cursor.close()
    conn.close()