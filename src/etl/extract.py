# Extraction related functions and logic go here
import pandas as pd

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe

def extract():
    with open("data/bank_market_cap.json", "r") as file:
        df_bank = extract_from_json(file)
    return df_bank
