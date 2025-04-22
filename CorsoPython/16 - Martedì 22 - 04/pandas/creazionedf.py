import pandas as pd

data = {
    "Nome" : ["Marco", "Pasquale", "Pippo"],
    "Eta" : [25, 30, 35],
    "Città" : ["Roma", "Milano", "Torino"],
    
}

df = pd.DataFrame(data)

print("DataFrame originale:")
print(df)

df_older = df[df["Eta"] > 30]


print("\nDataFrame filtrato (Eta > 30):")
print(df_older)

df["Maggiorenne"] = df["Eta"] >= 18

print("\nDataFrame con colonna 'Maggiorenne':")
print(df)