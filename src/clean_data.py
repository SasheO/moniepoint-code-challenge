import pandas as pd
import os
import shutil

input_folder = "../data/"
output_folder = "../clean_data/"

# Create the folder if it doesn't exist
for root, dirs, files in os.walk(output_folder, topdown=False):
    # Remove all files
    for file in files:
        file_path = os.path.join(root, file)
        os.remove(file_path)

os.makedirs(output_folder, exist_ok=True)

# get all files in input folder path
files = [
    f for f in os.listdir(input_folder)
    if os.path.isfile(os.path.join(input_folder, f))
]

# clean non-numeric data in "amount" column, null "merchant_id", non-date type in "event_timestamp" and write cleaned data
for filename in files:
    df = pd.read_csv(input_folder+filename)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["merchant_id"])
    df.drop(df[df["event_timestamp"] == "NOT-A-DATE"].index, inplace=True)
    df.to_csv(output_folder+filename, index=False)