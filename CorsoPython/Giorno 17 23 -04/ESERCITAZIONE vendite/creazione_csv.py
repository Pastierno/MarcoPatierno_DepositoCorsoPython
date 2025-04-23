import pandas as pd
import numpy as np

# Impostazioni
np.random.seed(123)
cities    = ['Roma', 'Milano', 'Napoli']
products  = ['Birra', 'Vino', 'Grappa']
dates     = pd.date_range(start='2024-04-01', end='2024-04-30', freq='D')

# Genera 500 record casuali
df = pd.DataFrame({
    'Data':     np.random.choice(dates, size=500),
    'Città':    np.random.choice(cities, size=500),
    'Prodotto': np.random.choice(products, size=500),
    'Vendite':  np.random.randint(50, 201, size=500)
})

# Ordina per data (opzionale)
df = df.sort_values('Data').reset_index(drop=True)

# Salva in CSV
df.to_csv('vendite.csv', index=False)

# Stampa un’anteprima
print(df.head(10))
