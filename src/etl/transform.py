# transform.py
import pandas as pd

def get_exchange_rate(currency_code, df_exchange):
    """
    Fetches the exchange rate for a given currency from a DataFrame.

    Parameters:
    currency_code (str): The currency code (e.g., "GBP") for which the exchange rate is to be fetched.
    df_exchange (pd.DataFrame): DataFrame containing exchange rates. Must have columns "Currency" and "Rate".

    Returns:
    float: The exchange rate for the given currency.

    Raises:
    ValueError: If df_exchange is None or if no exchange rate is found for the currency.
    TypeError: If df_exchange is not a pandas DataFrame.
    """

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
    """
    Transforms a DataFrame containing bank market cap data by converting the market cap to a different currency.

    Parameters:
    dataframe (pd.DataFrame): DataFrame containing bank market cap data. Must have a column "Market Cap (US$ Billion)".
    df_exchange (pd.DataFrame): DataFrame containing exchange rates. Must have columns "Currency" and "Rate".
    currency_code (str, optional): The currency to which market caps will be converted. Defaults to "GBP".

    Returns:
    pd.DataFrame: A new DataFrame with market caps converted to the target currency.

    Raises:
    TypeError: If dataframe['Market Cap (US$ Billion)'] is not a pandas Series or if it's not of numeric type.
    ValueError: If exchange rate for the currency is not found.
    """

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

