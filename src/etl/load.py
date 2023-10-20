# Loading related functions and logic go here
import pandas as pd

def load(df, currency_code):
    df.to_csv(f"data/bank_market_cap_{currency_code}.csv", index=False)
