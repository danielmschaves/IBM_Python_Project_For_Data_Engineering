import pandas as pd
import os
import pytest
from ..src.etl.extract import extract  
from ..src.etl.load import load 
from ..src.etl.transform import transform 

"""
Test script for E2E (End-to-End) testing of the ETL (Extract, Transform, Load) pipeline.

This script includes a function that tests the entire ETL process, from data extraction to data transformation
and finally to data loading.

Functions:
    test_etl_pipeline(): Tests the entire ETL pipeline and validates each phase.

Usage:
    Run this script using pytest to validate the entire ETL process.

Example:
    pytest test_etl_pipeline.py
"""

# Define paths for test
JSON_FILE_PATH = "data/bank_market_cap.json"
CSV_FILE_PATH = "data/exchange_rates.csv"
OUTPUT_FILE_PATH = "data/transformed_data.csv"

def test_etl_pipeline():
    """
    Tests the entire ETL (Extract, Transform, Load) pipeline and validates each phase.

    Steps:
    - Runs the extract phase and validates the extracted DataFrame.
    - Runs the transform phase and validates the transformed DataFrame.
    - Runs the load phase and validates that the data is correctly saved as a CSV file.

    Assertions:
    - The extracted and loaded DataFrames should not be empty.
    - Column names should match the expected names at each phase.
    - The output CSV file should exist after the load phase.
    """

    # Run the extract phase
    df_bank = extract()
    
    # Validate the extracted data
    assert isinstance(df_bank, pd.DataFrame), "Extract phase should return a DataFrame"
    assert not df_bank.empty, "Extracted DataFrame should not be empty"
    assert 'Name' in df_bank.columns, "DataFrame should have a 'Name' column"
    assert 'Market Cap (US$ Billion)' in df_bank.columns, "DataFrame should have a 'Market Cap (US$ Billion)' column"
    
    # Run the transform phase
    df_exchange = pd.read_csv(CSV_FILE_PATH)
    transformed_df = transform(df_bank, df_exchange, "GBP")
    
    # Validate the transformed data
    assert isinstance(transformed_df, pd.DataFrame), "Transform phase should return a DataFrame"
    assert not transformed_df.empty, "Transformed DataFrame should not be empty"
    assert f"Market Cap (GBP$ Billion)" in transformed_df.columns, "Transformed DataFrame should have a 'Market Cap (GBP$ Billion)' column"
    
    # Run the load phase
    load(transformed_df, "GBP", OUTPUT_FILE_PATH)
    
    # Validate the loaded data
    assert os.path.exists(OUTPUT_FILE_PATH), "Output CSV file should exist"
    
    loaded_df = pd.read_csv(OUTPUT_FILE_PATH)
    assert not loaded_df.empty, "Loaded DataFrame should not be empty"
    assert f"Market Cap (GBP$ Billion)" in loaded_df.columns, "Loaded DataFrame should have a 'Market Cap (GBP$ Billion)' column"

