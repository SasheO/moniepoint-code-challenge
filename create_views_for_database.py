from connect_to_database import *

import os

# this folder contains .txt files with sql queries that will be run
input_folder = "views/"

# get all files in input folder path
files = [
    input_folder+f for f in os.listdir(input_folder)
    if os.path.isfile(os.path.join(input_folder, f))
]


if __name__ == "__main__":

    conn = get_db_connection()
    cursor = conn.cursor()
    for filename in files:
        with open(filename, "r") as file:
            sql_view_query = file.read().replace("__table_name__", table_name)

        cursor.execute(sql_view_query)
        conn.commit()

    # close connection to database
    cursor.close()
    conn.close()