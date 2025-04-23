import numpy as np

# genera un array di 5 numeri casuali tra 0 e 1
arr = np.linspace(0, 1, 5)
print(arr) # [0.  0.25 0.5  0.75 1. ]

# matrice 3x3 di numeri casuali tra 0 e 1
random_arr = np.random.rand(3, 3)
print(random_arr)

# operazioni
arr = np.array([1, 2, 3, 4, 5])

sum = np.sum(arr) # somma degli elementi
mean = np.mean(arr) # media degli elementi
std = np.std(arr) # deviazione standard degli elementi