import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.figsize'] = [10, 6]
# Imèposta la imensione predefinita delle figure

plt.rcParams['figure.dpi'] = 100
# Imposta la risoluzione predefinita delle figure in DPI

# si possono impostare anche i colori predefiniti, i font, ecc.

plt.rcParams["figure.facecolor"] = "white"
# Imposta il colore di sfondo delle figure

sns.set_theme(style="darkgrid")

data = np.random.normal(size=100)

sns.histplot(data, kde=True) #kde disegna la funzione di densità
plt.title("Distribuzione dei dati")


# Crea una figura
fig = plt.figure()

# Aggiunge un asse alla figura
ax = fig.add_subplot(111)

plt.show()
