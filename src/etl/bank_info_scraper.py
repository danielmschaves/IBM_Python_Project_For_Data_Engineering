import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import logging

# Constants for URL and Output Path
URL = "https://en.wikipedia.org/wiki/List_of_largest_banks"
OUTPUT_PATH = os.path.join("data", "bank_market_cap.json")

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Function to fetch HTML from a URL
def fetch_html(url):
    """
    Fetch HTML content from a given URL.
    
    Parameters:
        url (str): The URL to fetch HTML from.

    Returns:
        str: The HTML content if successful, None otherwise.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Failed to fetch URL: {e}")
        return None

# Function to parse HTML
def parse_html(html):
    """
    Parse HTML content using BeautifulSoup.
    
    Parameters:
        html (str): The HTML content to parse.

    Returns:
        bs4.BeautifulSoup: The parsed HTML as a BeautifulSoup object.
    """
    
    return BeautifulSoup(html, "html.parser")

# Function to extract relevant data from HTML table
def extract_data_from_table(soup):
    """
    Extract relevant data from an HTML table using BeautifulSoup.
    
    Parameters:
        soup (bs4.BeautifulSoup): The parsed HTML as a BeautifulSoup object.

    Returns:
        pd.DataFrame: A DataFrame containing the extracted data, or None if extraction failed.
    """
    data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])
    target_table = soup.find("table", {"class": "wikitable"})
    
    if target_table:
        rows = target_table.find_all('tr')
        for row in rows[1:]:
            cells = row.find_all('td')
            if cells:
                name = cells[1].text.strip()
                market_cap = cells[2].text.strip()
                data = data._append({"Name": name, "Market Cap (US$ Billion)": market_cap}, ignore_index=True)
        return data
    else:
        logging.warning("Could not find the target table.")
        return None

# Function to save DataFrame to JSON
def save_data_to_json(data, path):
    """
    Save a DataFrame to a JSON file.
    
    Parameters:
        data (pd.DataFrame): The DataFrame to save.
        path (str): The file path to save the DataFrame to.

    Returns:
        None
    """
    try:
        with open(path, 'w') as f:
            f.write(data.to_json())
    except Exception as e:
        logging.error(f"Failed to save data: {e}")

# Main function
if __name__ == "__main__":
    logging.info("Starting the scraper...")
    html = fetch_html(URL)
    
    if html:
        logging.info(f"Received HTML data, length: {len(html)}")
        soup = parse_html(html)
        data = extract_data_from_table(soup)
        
        if data is not None and not data.empty:
            logging.info(f"Extracted {len(data)} rows of data.")
            save_data_to_json(data, OUTPUT_PATH)
            logging.info(f"Data saved to {OUTPUT_PATH}")
        else:
            logging.warning("No data extracted. Exiting.")
    else:
        logging.error("Failed to fetch HTML. Exiting.")
