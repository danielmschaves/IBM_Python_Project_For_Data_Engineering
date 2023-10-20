# Main ETL script that ties everything together
from datetime import datetime
from extract import extract
from transform import transform
from load import load

def log(message):
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
    df_transformed = transform(df_bank, "GBP")
    log("Transform phase Ended")

    log("Load phase Started")
    load(df_transformed, "GBP")
    log("Load phase Ended")

