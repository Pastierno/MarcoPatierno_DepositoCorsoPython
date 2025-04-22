import pandas as pd

df = pd.read_csv("CorsoPython/16 - Martedì 22 - 04/pandas/data.csv")

# Visualizza le prime righe del DataFrame
print(df.head())

# Visualizzare le ultime righe del DataFrame
print(df.tail())

# Calcolare statistiche descrittive
print(df.describe())

# Gestire i valori nulli
print(df.isnull().sum())


# Gestire valori errati

df["Età"] = pd.to_numeric(df["Età"], errors="coerce")  # Converte in numerico, sostituisce errori con NaN
df["Salario"] = pd.to_numeric(df["Salario"], errors="coerce")

df["Nome"].fillna("Sconosciuto", inplace=True)

df["Salario"].fillna(df["Salario"].mean(), inplace=True)

df["Età"].fillna(df["Età"].median(), inplace=True)

df["Città"].fillna("Sconosciuta", inplace=True)

df.replace({"Città": {"Milaan": "Milano"}}, inplace=True)
#print(df)

# Standardizzo i valori di Età e Salario in interi
df["Età"] = df["Età"].astype(int)
df["Salario"] = df["Salario"].astype(int)
#print(df)

# Aggiungo colonna categoria età
df["Categoria Età"] = pd.cut(df["Età"], bins=[0, 18, 65, 100], labels=["Giovane", "Adulto", "Senior"])
print(df)

print(df.describe())