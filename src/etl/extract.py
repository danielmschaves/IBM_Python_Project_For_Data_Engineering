# Extraction related functions and logic go here
import pandas as pd

def extract_from_json(file_to_process):
    """
    Reads a JSON file and converts it to a pandas DataFrame.

    Parameters:
    file_to_process (file object): The JSON file object to process.

    Returns:
    pd.DataFrame: DataFrame containing the JSON data.
    """
    return pd.read_json(file_to_process)

def extract_exchange_rates(file_path):
    """
    Reads a CSV file containing exchange rates and converts it to a DataFrame.
    The function also sets the column names as 'Currency' and 'Rate'.

    Parameters:
    file_path (str): The path to the CSV file containing exchange rates.

    Returns:
    pd.DataFrame: DataFrame containing the exchange rates.
    """
    df = pd.read_csv(file_path, header=None)
    df.columns = ['Currency', 'Rate']  # Add the missing column names
    return df

def extract():
    """
    Reads the bank market capitalization JSON file and converts it to a DataFrame.

    Returns:
    pd.DataFrame: DataFrame containing the bank market capitalization data.
    """
    with open("data/bank_market_cap.json", "r") as file:
        df_bank = extract_from_json(file)
    return df_bank