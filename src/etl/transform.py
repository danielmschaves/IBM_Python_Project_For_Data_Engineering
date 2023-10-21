# transform.py
import pandas as pd

def get_exchange_rate(currency_code, df_exchange):
    if df_exchange is None:
        raise ValueError("Exchange rate DataFrame is None")
        
    if not isinstance(df_exchange, pd.DataFrame):
        raise TypeError("df_exchange must be a pandas DataFrame")
        
    if 'Currency' not in df_exchange.columns or 'Rate' not in df_exchange.columns:
        raise ValueError("Missing required columns in df_exchange DataFrame")
    
    rate = df_exchange.loc[df_exchange['Currency'] == currency_code, 'Rate']
    
    if rate.empty:
        raise ValueError(f"No exchange rate found for currency {currency_code}")
    
    return rate.iloc[0]

def transform(dataframe, df_exchange, currency_code="GBP"):
    # Validate and Get the exchange rate for the given currency code from df_exchange
    exchange_rate = get_exchange_rate(currency_code, df_exchange)
    
    # Convert exchange_rate to float
    exchange_rate = float(exchange_rate)
    
    # Make sure 'Market Cap (US$ Billion)' is also float
    dataframe['Market Cap (US$ Billion)'] = dataframe['Market Cap (US$ Billion)'].astype(float)
    
    # Create a copy of the original DataFrame to avoid modifying it
    transformed_df = dataframe.copy()

    # Update the market cap column
    transformed_df['Market Cap (US$ Billion)'] *= exchange_rate
    
    # Rename the column
    transformed_df.rename(columns={'Market Cap (US$ Billion)': f'Market Cap ({currency_code}$ Billion)'}, inplace=True)
    
    return transformed_df

