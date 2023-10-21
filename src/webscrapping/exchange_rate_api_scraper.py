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
    # Replace with your API key
    api_key = "your_api_key_here"
    fetch_and_save_exchange_rate(api_key)
