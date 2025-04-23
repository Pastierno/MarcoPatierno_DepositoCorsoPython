import pandas as pd

data = {
    'Nome': ['Alice', 'Bob'],
    "Età": [25, 30],
}

# Visualizzazione delle statistiche descrittive
df = pd.DataFrame(data)
print(df.describe())

# Selezione di una colonna
ages = df['Età']
print(ages)

# Filtraggio
df_filtered = df[df['Età'] >= 18]
print(df_filtered)

# Ordinamento
df_sorted = df.sort_values(by='Età')

#Unione di DataFrame
df_merged = pd.merge(df, df_sorted, on='Nome')

print(df_merged)

# Applicazione di una funzione a una colonna

df['Età_doppia'] = df['Età'].apply(lambda x: x * 2)
print(df)

# Esportazione in CSV
df.to_csv('output.csv', index=False)

# Generazione serie temporali
date_range = pd.date_range(start='2023-01-01', periods=5, freq='ME')

#df_resample = df.resample('M').mean()
#print(df_resample)

# Visualizzazione di un grafico a barre
import matplotlib.pyplot as plt

df['Età'].plot(kind='bar')
plt.show()