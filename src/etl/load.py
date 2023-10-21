# load.py
import pandas as pd

def load(dataframe, currency, output_path):
    dataframe.to_csv(output_path, index=False)