import pandas as pd
import pytest
from ..src.etl.transform import transform  
from ..src.etl.extract import extract_from_json  

# Test function to validate the transformation logic based on actual data
def test_transform_actual_data():
    # Given: Extract actual data and exchange rates into DataFrames
    df_actual = extract_from_json("data/bank_market_cap.json")  # Replace with actual path
    df_exchange = pd.DataFrame({'Currency': ['USD', 'GBP'], 'Rate': [1.0, 0.75]})  # Replace with actual extracted data
    
    # When: Transform the market cap to GBP
    df_transformed = transform(df_actual, df_exchange, "GBP")  # Pass exchange rate DataFrame and currency code
    
    # Then: Validate the transformed DataFrame
    assert 'Market Cap (GBP$ Billion)' in df_transformed.columns, "Column should be renamed to GBP"