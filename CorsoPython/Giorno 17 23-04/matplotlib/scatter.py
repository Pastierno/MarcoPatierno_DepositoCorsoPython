import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)  # Genera 100 valori casuali per l'asse x
y = np.random.rand(100)  # Genera 100 valori casuali per l'asse y

plt.figure()
plt.scatter(x, y)  # Crea un grafico a dispersione
plt.title("Grafico a dispersione")  # Titolo del grafico
plt.xlabel("Asse X")  # Etichetta asse X
plt.ylabel("Asse Y")  # Etichetta asse Y
plt.show()