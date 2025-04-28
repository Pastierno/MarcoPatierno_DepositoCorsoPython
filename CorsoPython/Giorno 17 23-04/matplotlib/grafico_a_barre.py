import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 12, 5]

plt.figure(figsize=(10, 6))  # Imposta la dimensione della figura
plt.bar(categories, values)  # Disegna il grafico a barre
plt.title("Grafico a barre")  # Titolo del grafico
plt.xlabel("Categorie")  # Etichetta asse X
plt.ylabel("Valori")  # Etichetta asse Y
plt.show()  # Mostra il grafico