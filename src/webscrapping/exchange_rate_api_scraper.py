import requests
import pandas as pd
import os
import logging
import json

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_api_key_from_config(file_path='config.json'):
    """
    Reads the API key from a JSON config file.

    Parameters:
        file_path (str): The path to the config file. Default is 'config.json'.

    Returns:
        str: The API key, or None if the key is not found or the file is missing.
    """
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
        return config.get('EXCHANGE_API_KEY', None)
    except FileNotFoundError:
        return None

def fetch_and_save_exchange_rate(api_key):
    """
    Fetches the latest exchange rates using a given API key and saves it as a CSV.

    Parameters:
        api_key (str): The API key to use for fetching exchange rates.

    Returns:
        None
    """
    try:
        logger.info("Starting to fetch exchange rate data...")
        
        # Make the API request
        url = f"https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey={api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Check for successful API call
        
        # Convert the JSON data to a DataFrame
        json_data = response.json()
        if 'rates' in json_data:
            data = pd.DataFrame(list(json_data['rates'].items()), columns=['Currency', 'Rate'])
        else:
            logger.error("Rates not found in JSON data")
            return
        
        # Save the DataFrame to a CSV file
        output_path = os.path.join("data", "exchange_rates.csv")
        logger.info(f"Saving file to: {output_path}")
        data.to_csv(output_path, index=False)
            
    except requests.RequestException as e:
        logger.error(f"Failed to fetch data: {e}")
        
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    api_key = get_api_key_from_config()
    if api_key:
        fetch_and_save_exchange_rate(api_key)
    else:
        print("API Key not found.")
