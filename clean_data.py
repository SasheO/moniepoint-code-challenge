import pandas as pd
import os

input_folder = "sample_data"
output_folder = "clean_data/"

# get all files in input folder path
files = [
    f for f in os.listdir(input_folder)
    if os.path.isfile(os.path.join(input_folder, f))
]

# clean non-numeric data in "amount" column, null "merchant_id", non-date type in "event_timestamp" and write cleaned data
for filename in files:
    df = pd.read_csv('sample_data/'+filename)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["merchant_id"])
    df.drop(df[df["event_timestamp"] == "NOT-A-DATE"].index, inplace=True)
    df.to_csv(output_folder+filename, index=False)