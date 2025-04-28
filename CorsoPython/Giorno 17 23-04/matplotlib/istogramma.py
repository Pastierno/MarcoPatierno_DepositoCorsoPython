import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)  # Genera dati casuali

plt.figure(figsize=(10, 6))  # Imposta la dimensione della figura
plt.hist(data, bins=30)  # Disegna l'istogramma
plt.title("Istogramma dei dati casuali")  # Titolo dell'istogramma
plt.xlabel("Valori")  # Etichetta asse X
plt.ylabel("Frequenza")  # Etichetta asse Y
plt.show()

