import pandas as pd
import os
import pytest
from ..src.etl.extract import extract_from_json, extract_exchange_rates, extract  

# The path where the actual files are saved
DATA_PATH = "data"

def test_extract_from_json():
    json_file_path = os.path.join(DATA_PATH, "bank_market_cap.json")
    df = extract_from_json(json_file_path)
    
    assert isinstance(df, pd.DataFrame), "Should return a DataFrame"
    assert 'Name' in df.columns, "DataFrame should have a 'Name' column"
    assert 'Market Cap (US$ Billion)' in df.columns, "DataFrame should have a 'Market Cap (US$ Billion)' column"

def test_extract_exchange_rates():
    csv_file_path = os.path.join(DATA_PATH, "exchange_rates.csv")
    df = extract_exchange_rates(csv_file_path)
    
    assert isinstance(df, pd.DataFrame), "Should return a DataFrame"
    assert 'Currency' in df.columns, "DataFrame should have a 'Currency' column"
    assert 'Rate' in df.columns, "DataFrame should have a 'Rate' column"

def test_extract():
    json_file_path = os.path.join(DATA_PATH, "bank_market_cap.json")
    df = extract()
    
    assert isinstance(df, pd.DataFrame), "Should return a DataFrame"
    assert 'Name' in df.columns, "DataFrame should have a 'Name' column"
    assert 'Market Cap (US$ Billion)' in df.columns, "DataFrame should have a 'Market Cap (US$ Billion)' column"

