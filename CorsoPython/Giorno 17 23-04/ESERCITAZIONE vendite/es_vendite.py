import pandas as pd
import numpy as np

df = pd.read_csv(r'CorsoPython\Giorno 17 23 -04\ESERCITAZIONE vendite\vendite.csv')
#print(df.head(10))

# Creazione tabella pivot per analizzare le vendite per città e prodotto
df_pivot_mean = df.pivot_table(index='Città', columns='Prodotto', values='Vendite', aggfunc='mean')

# metodo groupby per vendite totali per ogni prodotto
df_groupby = df.groupby('Prodotto')['Vendite'].sum().reset_index()


print("Tabella pivot delle vendite medie per città e prodotto:")
print(df_pivot_mean)

print("\nVendite totali per ogni prodotto:")
print(df_groupby)
