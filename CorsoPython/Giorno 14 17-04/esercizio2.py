import numpy as np

# array 1D di 20 interi casuali tra 10 e 50 
arr = np.random.randint(10, 51, 20)

# slicing per estrarre i primi 10 elementi
print(arr[:10])

# ultiumi 5 elementi
print(arr[-5:])

# da indice 5 a 15 escluso
print(arr[5:15])

# ogni terzo elemento
print(arr[::2])

# modifica tramite slicing degli elementi dall'indice 5 a 10 escluso assegnando 99
arr[5:10] = 99
print(arr)



