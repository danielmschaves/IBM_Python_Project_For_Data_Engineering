import pandas as pd
import os
import pytest
from ..src.etl.extract import extract_from_json, extract_exchange_rates, extract  

"""
Test script for the extraction part of the ETL (Extract, Transform, Load) pipeline.

This script includes functions that individually test the data extraction from JSON and CSV files.

Functions:
    test_extract_from_json(): Tests the extraction of bank market cap data from a JSON file.
    test_extract_exchange_rates(): Tests the extraction of exchange rates from a CSV file.
    test_extract(): Tests the extract function that combines various extraction functionalities.

Usage:
    Run this script using pytest to validate the extraction part of the ETL process.

Example:
    pytest test_extract.py
"""

# The path where the actual files are saved
DATA_PATH = "data"

def test_extract_from_json():
    """
    Tests the extraction of bank market cap data from a JSON file.

    Assertions:
    - The returned object should be a DataFrame.
    - The DataFrame should have a 'Name' column.
    - The DataFrame should have a 'Market Cap (US$ Billion)' column.
    """
    json_file_path = os.path.join(DATA_PATH, "bank_market_cap.json")
    df = extract_from_json(json_file_path)
    
    assert isinstance(df, pd.DataFrame), "Should return a DataFrame"
    assert 'Name' in df.columns, "DataFrame should have a 'Name' column"
    assert 'Market Cap (US$ Billion)' in df.columns, "DataFrame should have a 'Market Cap (US$ Billion)' column"

def test_extract_exchange_rates():
    """
    Tests the extraction of exchange rates from a CSV file.

    Assertions:
    - The returned object should be a DataFrame.
    - The DataFrame should have a 'Currency' column.
    - The DataFrame should have a 'Rate' column.
    """
    csv_file_path = os.path.join(DATA_PATH, "exchange_rates.csv")
    df = extract_exchange_rates(csv_file_path)
    
    assert isinstance(df, pd.DataFrame), "Should return a DataFrame"
    assert 'Currency' in df.columns, "DataFrame should have a 'Currency' column"
    assert 'Rate' in df.columns, "DataFrame should have a 'Rate' column"

def test_extract():
    """
    Tests the extract function that combines various extraction functionalities.

    Assertions:
    - The returned object should be a DataFrame.
    - The DataFrame should have a 'Name' column.
    - The DataFrame should have a 'Market Cap (US$ Billion)' column.
    """

    json_file_path = os.path.join(DATA_PATH, "bank_market_cap.json")
    df = extract()
    
    assert isinstance(df, pd.DataFrame), "Should return a DataFrame"
    assert 'Name' in df.columns, "DataFrame should have a 'Name' column"
    assert 'Market Cap (US$ Billion)' in df.columns, "DataFrame should have a 'Market Cap (US$ Billion)' column"

