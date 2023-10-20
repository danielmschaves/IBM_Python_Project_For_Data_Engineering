# Transformation related functions and logic go here
import pandas as pd

def get_exchange_rate(currency_code):
    df_exchange = pd.read_csv("data/exchange_rates.csv")
    df_exchange.rename(columns={'Unnamed: 0': 'Currency'}, inplace=True)
    print("Columns in df_exchange:", df_exchange.columns)  # Debugging line

    if 'Currency' in df_exchange.columns:
        return df_exchange.loc[df_exchange['Currency'] == currency_code, 'Rate'].iloc[0]
    else:
        print(f"Error: 'Currency' column not found in DataFrame. Available columns are: {df_exchange.columns}")
        return 1  # Returning a default value, you may handle it differently


def transform(df, currency_code):
    exchange_rate = get_exchange_rate(currency_code)
    df['Market Cap (US$ Billion)'] = round(df['Market Cap (US$ Billion)'] * exchange_rate, 3)
    df.rename(columns={'Market Cap (US$ Billion)': f'Market Cap ({currency_code}$ Billion)'}, inplace=True)
    return df
