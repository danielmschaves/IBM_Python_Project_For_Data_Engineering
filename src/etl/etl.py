# Main ETL script that ties everything together
from datetime import datetime
import os  # Make sure to import os
from extract import extract
from transform import transform
from load import load
from extract import extract, extract_exchange_rates  # Import the new function

def log(message):
    """
    Logs a message with a timestamp to a log file.

    Parameters:
    message (str): The message to be logged.

    Side Effects:
    Appends a message with a timestamp to a log file located at 'logs/logfile.txt'.
    """
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("logs/logfile.txt", "a") as f:
        f.write(timestamp + ',' + message + '\n')

if __name__ == '__main__':
    log("ETL Job Started")
    
    log("Extract phase Started")
    df_bank = extract()
    log("Extract phase Ended")

    log("Transform phase Started")
    df_exchange = extract_exchange_rates("data/exchange_rates.csv")
    transformed_df = transform(df_bank, df_exchange, "GBP")
    log("Transform phase Ended")

    log("Load phase Started")
    
    # Define the output path
    output_path = os.path.join("data", "transformed_data.csv")

    # Call the load function with all required arguments
    load(transformed_df, "GBP", output_path)

    log("Load phase Ended")

