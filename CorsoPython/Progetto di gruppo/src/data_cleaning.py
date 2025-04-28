import pandas as pd

def dataframe():
    df = pd.read_csv('https://raw.githubusercontent.com/MaSTERmIKK/data_-marvel/refs/heads/main/data/spotify-charts-daily-2020-10-07.csv')
    return df

