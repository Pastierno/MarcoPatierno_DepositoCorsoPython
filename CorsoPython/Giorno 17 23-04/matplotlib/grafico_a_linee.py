import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure(figsize=(10, 6))  # Imposta la dimensione della figura
plt.plot(x, y)  # Disegna il grafico a linee
plt.title("Grafico a linee")  # Titolo del grafico
plt.xlabel("Asse X")  # Etichetta asse X
plt.ylabel("Asse Y")  # Etichetta asse Y
plt.show()  # Mostra il grafico