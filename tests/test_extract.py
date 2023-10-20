# Importing required libraries and modules
import json
import pandas as pd
import pytest
from ..src.etl.extract import extract_from_json  # Import path based on the project's structure

# Test function to validate the extract_from_json function with a valid JSON file
def test_extract_from_json_valid_file():
    """This test checks if the extract_from_json function handles valid JSON properly."""
    
    # Given: Arrange the test by providing a sample valid JSON as input
    sample_json = json.dumps([
        {"Name": "Bank1", "Market Cap (US$ Billion)": 100},
        {"Name": "Bank2", "Market Cap (US$ Billion)": 200}
    ])
    
    # When: Act by calling the function
    df = extract_from_json(sample_json)
    
    # Then: Assert to validate the DataFrame has the correct data
    assert isinstance(df, pd.DataFrame), "Output should be a DataFrame"
    assert "Name" in df.columns, "DataFrame should have a 'Name' column"
    assert "Market Cap (US$ Billion)" in df.columns, "DataFrame should have a 'Market Cap (US$ Billion)' column"
    assert df.iloc[0]["Name"] == "Bank1", "First row should have Name 'Bank1'"
    assert df.iloc[0]["Market Cap (US$ Billion)"] == 100, "First row should have Market Cap 100"

# Test function to validate the extract_from_json function with an invalid JSON file
def test_extract_from_json_invalid_json():
    """This test checks if the extract_from_json function handles invalid JSON properly."""
    
    # Given: Arrange the test by providing an invalid JSON string
    invalid_json = "This is not a JSON string"
    
    # When: Act by calling the function, Then: Assert to expect a ValueError
    with pytest.raises(ValueError):
        extract_from_json(invalid_json)
