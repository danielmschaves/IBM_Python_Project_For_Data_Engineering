import pandas as pd

def get_exchange_rate(currency_code, df_exchange):
    rate = df_exchange.loc[df_exchange['Currency'] == currency_code, 'Rate']
    
    if rate.empty:
        raise ValueError(f"No exchange rate found for currency {currency_code}")
    
    return rate.iloc[0]

def transform(dataframe, df_exchange, currency_code="GBP"):
    # Get the exchange rate for the given currency code from df_exchange
    exchange_rate = df_exchange[df_exchange['Currency'] == currency_code]['Rate'].iloc[0]
    
    # Create a copy of the original DataFrame to avoid modifying it
    transformed_df = dataframe.copy()

    # Update the market cap column
    transformed_df['Market Cap (US$ Billion)'] *= exchange_rate
    
    # Rename the column
    transformed_df.rename(columns={'Market Cap (US$ Billion)': f'Market Cap ({currency_code}$ Billion)'}, inplace=True)
    
    return transformed_df
