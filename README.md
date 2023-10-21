# IBM Python Project for Data Engineering

## Table of Contents
- [Features](#features)
- [Scenario](#Scenario)
- [Installation](#installation)


## Features
- **Data Extraction**: Extracts bank market capitalization data from JSON files and exchange rates from CSV files.
- **Data Transformation**: Converts bank market caps to different currencies using fetched exchange rates.
- **Data Loading**: Outputs the transformed data into CSV format.
- **Logging**: Provides detailed logs for auditing and debugging.
- **Testing**: Unit tests to validate each component of the pipeline.


## Scenario

As a data engineer working for an international financial analysis company, my job was to collect financial data from various sources such as websites, APIs, and files provided by financial analysis firms. 

- Extract API Data: Collect exchange rate data using the ExchangeRate-API and store the data as a CSV. The data is fetched using the requests library and transformed into a pandas DataFrame. The DataFrame is saved as exchange_rates_1.csv.

- Web Scraping: Scrape the largest banks' information by market capitalization from a Wikipedia page (https://en.wikipedia.org/wiki/List_of_largest_banks) using BeautifulSoup. The scraped data is stored in a pandas DataFrame and saved as a JSON file named bank_market_cap.json.

- Extract: The first phase involves extracting data from a JSON file named bank_market_cap_1.json. The extracted data is stored in a pandas DataFrame with the columns 'Name' and 'Market Cap (US$ Billion)'.

- Transform: The second phase transforms the extracted data. The 'Market Cap (US$ Billion)' column is converted from USD to GBP using exchange rate data from the exchange_rates.csv file. The transformed data is rounded to 3 decimal places, and the column is renamed to 'Market Cap (GBP$ Billion)'.

- Load: The final phase loads the transformed data into a new CSV file named bank_market_cap_gbp.csv. The index is set to False when saving the DataFrame to the CSV file.

- Logging: A logging function is implemented to keep track of the ETL process. The function logs messages with timestamps in a file named logfile.txt.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/IBM_Python_Project_For_Data_Engineering.git
cd IBM_Python_Project_For_Data_Engineering
```

2. Configure python version with `pyenv`:

```bash
pyenv install 3.11.3
pyenv local 3.11.3
```
3. Install dependencies using Poetry:

```bash
poetry install
```

4. Activate the Poetry environment:

```bash
poetry shell
```

5. Run the ETL pipeline:

```bash
python src/etl/etl.py
```

6. To run the tests, execute the following command inside the Poetry environment:

```bash
pytest
```
