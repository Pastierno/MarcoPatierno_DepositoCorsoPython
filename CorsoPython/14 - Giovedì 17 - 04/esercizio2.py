import numpy as np

# Array 1D di 20 interi casuali tra 1 e 50 
arr = np.random.randint(1, 50, size=20)

# Slicing per estrarre i primi 10 elementi

print(arr[:10])

# ultiumi 5 elementi
print(arr[-5:])

# da indice 5 a 15 escluso
print(arr[5:15])

# ogni terzo elemento
print(arr[::3])

# modifica tramite slicing degli elementi dall'indice 5 a 10 escluso assegnando 99
arr[5:10] = 99
print(arr)



