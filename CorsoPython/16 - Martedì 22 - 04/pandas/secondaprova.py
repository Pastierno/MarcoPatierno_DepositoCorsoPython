import pandas as pd
import numpy as np

data = {
    "Nome" : ["Alice", "Bob", "Carla", "Bob", "Carla", "Alice", None],
    "Eta" : [25, 30, 22, np.nan, 25, 29],
    "Città" : ["Roma", "Milano", "Napoli", "Milano", "Napoli", "Roma", "Roma"],
}

df = pd.DataFrame(data)

df = df.drop_duplicates()
df_cleaned = df.dropna()

df["Eta"].fillna(df["Eta"].mean(), inplace=True)

