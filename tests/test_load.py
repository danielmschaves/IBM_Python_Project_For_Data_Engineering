import sys
sys.path.append(r"C:\Users\dmc\IBM_Python_Project_For_Data_Engineering\src")


import os
import pandas as pd
from pathlib import Path
import pytest
from ..src.etl.load import load  # Assuming load function is in this module

# Test function to validate the loading logic using actual transformed data
def test_load_actual_data(tmp_path: Path):
    """Test the load function using actual transformed data."""
    
    # Given: Create a sample transformed DataFrame
    df_transformed = pd.DataFrame({
        'Name': ['Bank A', 'Bank B'],
        'Market Cap (GBP$ Billion)': [75.0, 100.0]
    })

    # When: Load the DataFrame into a CSV file
    output_file = tmp_path / "bank_market_cap_gbp.csv"
    load(df_transformed, "GBP", output_file)
    
    # Then: Validate that the file is created
    assert output_file.exists(), "Output file should be created"
    
    # Then: Read the CSV file back into a DataFrame and validate
    df_read = pd.read_csv(output_file)
    
    # Assert the DataFrame read from file is same as the one we saved
    pd.testing.assert_frame_equal(df_read, df_transformed, check_dtype=False)