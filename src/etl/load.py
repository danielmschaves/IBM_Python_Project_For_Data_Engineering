# load.py
import pandas as pd

def load(dataframe, currency, output_path):
    """
    Saves a DataFrame to a CSV file at the specified output path.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame to be saved.
    currency (str): The currency used for the market cap data in the DataFrame. This parameter is currently not used in the function but is part of its signature.
    output_path (str): The path where the CSV file will be saved.

    Returns:
    None
    """
    dataframe.to_csv(output_path, index=False)