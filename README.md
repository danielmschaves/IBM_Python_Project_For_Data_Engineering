# Data Engineer - ETL Project

## Repository Overview

This repository contains the code and data files for a data engineering project focused on the ETL (Extract, Transform, Load) process. The project involves extracting bank and market cap data from a JSON file, transforming the market cap currency using exchange rate data, and loading the transformed data into a separate CSV file. The ETL process is implemented using Python and several Python libraries, such as pandas, datetime, requests, and BeautifulSoup.

## Phases

### Scenario

As a data engineer working for an international financial analysis company, my job was to collect financial data from various sources such as websites, APIs, and files provided by financial analysis firms. 

- Extract API Data: Collect exchange rate data using the ExchangeRate-API and store the data as a CSV. The data is fetched using the requests library and transformed into a pandas DataFrame. The DataFrame is saved as exchange_rates_1.csv.

- Web Scraping: Scrape the largest banks' information by market capitalization from a Wikipedia page (https://en.wikipedia.org/wiki/List_of_largest_banks) using BeautifulSoup. The scraped data is stored in a pandas DataFrame and saved as a JSON file named bank_market_cap.json.

- Extract: The first phase involves extracting data from a JSON file named bank_market_cap_1.json. The extracted data is stored in a pandas DataFrame with the columns 'Name' and 'Market Cap (US$ Billion)'.

- Transform: The second phase transforms the extracted data. The 'Market Cap (US$ Billion)' column is converted from USD to GBP using exchange rate data from the exchange_rates.csv file. The transformed data is rounded to 3 decimal places, and the column is renamed to 'Market Cap (GBP$ Billion)'.

- Load: The final phase loads the transformed data into a new CSV file named bank_market_cap_gbp.csv. The index is set to False when saving the DataFrame to the CSV file.

- Logging: A logging function is implemented to keep track of the ETL process. The function logs messages with timestamps in a file named logfile.txt.

## Conclusion

This project demonstrates a comprehensive ETL process that includes collecting data from APIs, web scraping, extracting data from JSON files, transforming data using exchange rate information, and loading the transformed data into CSV files. The code is organized in a clear and modular manner, making it easy to understand and modify for other ETL tasks. By following the step-by-step instructions in the code, users can learn the essentials of data engineering and gain practical experience in implementing ETL processes.


