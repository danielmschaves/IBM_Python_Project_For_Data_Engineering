from datetime import datetime
import os
import pandas as pd  # Added import for pandas
from extract import extract, extract_exchange_rates  # Make sure these functions exist in your extract module
from transform import transform  # Make sure this function exists in your transform module
from load import load  # Make sure this function exists in your load module

# Importing scraping functions
from bank_info_scraper import fetch_html, parse_html, extract_data_from_table, save_data_to_json
from exchange_rate_api_scraper import get_api_key_from_config, fetch_and_save_exchange_rate

# Constants for URL and Output Path
URL = "https://en.wikipedia.org/wiki/List_of_largest_banks"
OUTPUT_PATH = os.path.join("data", "bank_market_cap.json")

def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("logs/logfile.txt", "a") as f:
        f.write(timestamp + ',' + message + '\n')

if __name__ == '__main__':
    log("ETL Job Started")

    # Extract phase for Bank Info
    log("Bank Info Extract phase Started")
    html = fetch_html(URL)
    if html:
        soup = parse_html(html)
        df_bank = extract_data_from_table(soup)
        if df_bank is not None:
            save_data_to_json(df_bank, OUTPUT_PATH)
            log("Bank Info Extract phase Ended")
        else:
            log("Bank Info Extract phase Failed")

    # Extract phase for Exchange Rates
    api_key = get_api_key_from_config()
    if api_key:
        log("Exchange Rate Extract phase Started")
        fetch_and_save_exchange_rate(api_key)
        df_exchange = pd.read_csv("data/exchange_rates.csv")  # Reading the saved CSV into DataFrame
        log("Exchange Rate Extract phase Ended")
    else:
        log("Exchange Rate Extract phase Failed")

    log("Transform phase Started")
    transformed_df = transform(df_bank, df_exchange, "GBP")  # Make sure your transform function can handle these arguments
    log("Transform phase Ended")

    # Load phase
    log("Load phase Started")
    output_path = os.path.join("data", "transformed_data.csv")
    load(transformed_df, "GBP", output_path)  # Make sure your load function can handle these arguments
    log("Load phase Ended")
