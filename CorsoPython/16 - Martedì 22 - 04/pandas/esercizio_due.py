import pandas as pd

# Leggo il file CSV
df = pd.read_csv(r"CorsoPython\16 - Martedì 22 - 04\pandas\data2.csv")
print("Dataset originale:")
print(df)

# Conversione dati in formato numerico
df['Quantità'] = pd.to_numeric(df['Quantità'], errors='coerce')
df['PrezzoUnitario'] = pd.to_numeric(df['PrezzoUnitario'], errors='coerce')

# Gestione valori mancanti e conversione tipi
df['Quantità'] = df['Quantità'].fillna(0).astype(int)
df['PrezzoUnitario'] = df['PrezzoUnitario'].fillna(0).astype(float)

# Calcolo vendite totali
df['Totale vendite'] = df['Quantità'] * df['PrezzoUnitario']

# Analisi per prodotto
df_grouped = df.groupby('Prodotto')['Totale vendite'].sum().reset_index()

# Identificazione prodotto più venduto (per valore)
prodotto_piu_venduto = df_grouped.loc[df_grouped['Totale vendite'].idxmax()]

# Identificazione città con più vendite (per valore)
citta_con_piu_vendite = df.groupby('Città')['Totale vendite'].sum().idxmax()

# Filtro vendite superiori a 500 euro
df_maggiori_500 = df[df['Totale vendite'] > 500]

# Ordinamento per valore vendite
df_ordinato = df.sort_values(by='Totale vendite', ascending=False)

# visualizzo il numero di articoli venduti per città (quantità)
df_citta = df.groupby('Città')['Quantità'].sum().reset_index()
# In alternativa, se vuoi il valore totale delle vendite per città:
df_citta_valore = df.groupby('Città')['Totale vendite'].sum().reset_index()

# Output risultati
print("\nProdotto più venduto:")
print(prodotto_piu_venduto)
print("\nCittà con più vendite:")
print(citta_con_piu_vendite)
print("\nDataframe con vendite maggiori di 500 euro:")
print(df_maggiori_500)
print("\nDataframe ordinato per totale vendite:")
print(df_ordinato)
print("\nNumero di articoli venduti per città:")
print(df_citta)
print("\nValore totale vendite per città:")
print(df_citta_valore)

