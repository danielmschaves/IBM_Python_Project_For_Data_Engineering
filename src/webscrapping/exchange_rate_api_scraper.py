# exchange_rate_api_scraper.py

import requests
import pandas as pd
import os
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_and_save_exchange_rate(api_key):
    try:
        logger.info("Starting to fetch exchange rate data...")
        
        # Make the API request
        url = f"https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=VlJF1oqydt0EGDGBSOWxa7Jvx1jLy9ei"
        response = requests.get(url)
        response.raise_for_status()  # Check for successful API call
        
        # Convert the JSON data to a DataFrame
        json_data = response.json()
        data = pd.DataFrame.from_dict(json_data)
        
        # Drop unnecessary columns and rename the 'rates' column
        cleaned_data = data.drop(["success", "timestamp", "base", "date"], axis=1).rename(columns={"rates": "Rate"})
        
        # Save the DataFrame to a CSV file
        output_path = os.path.join("data", "exchange_rates.csv")
        logger.info(f"Saving file to: {output_path}")
        with open(output_path, 'w') as openfile:
            openfile.write(cleaned_data.to_csv())
            
    except requests.RequestException as e:
        logger.error(f"Failed to fetch data: {e}")
        
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with your API key
    api_key = "your_api_key_here"
    fetch_and_save_exchange_rate(api_key)
