# Extraction related functions and logic go here
import pandas as pd

def extract_from_json(file_to_process):
    return pd.read_json(file_to_process)

def extract_exchange_rates(file_path):
    df = pd.read_csv(file_path, header=None)
    df.columns = ['Currency', 'Rate']  # Add the missing column names
    return df

def extract():
    with open("data/bank_market_cap.json", "r") as file:
        df_bank = extract_from_json(file)
    return df_bank