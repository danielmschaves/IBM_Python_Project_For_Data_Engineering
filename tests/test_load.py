import os
import pandas as pd
from pathlib import Path
import pytest
from ..src.etl.load import load 

# Test function to validate the loading logic using actual transformed data
def test_load_actual_data(tmp_path: Path):
    """
    Tests the load function using actual transformed data.

    This function:
    - Creates a sample DataFrame with transformed bank market cap data.
    - Saves the DataFrame into a temporary CSV file using the load function.
    - Reads the saved CSV file back into a DataFrame.
    - Compares the original and read DataFrames to ensure they are the same.

    Arguments:
    tmp_path: pytest fixture that provides a temporary directory unique to the test invocation.

    Assertions:
    - The output file should be created in the temporary directory.
    - The DataFrame read from the file should be the same as the original DataFrame.

    Usage:
    This function is automatically discoverable by pytest and will be run during testing.
    """
        
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