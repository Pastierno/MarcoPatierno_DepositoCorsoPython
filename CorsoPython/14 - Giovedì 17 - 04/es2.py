import numpy as np
# es 2
# crea una matrice 5x5 contentente numeri interi sequenziali da 1 a 25
matrix = np.arange(1, 26).reshape(5, 5)
print(matrix)

# seconda colonna
col2 = matrix[:, 1]
print(col2)

# terza riga
row3 = matrix[2, :]
print(row3)

#somma degli elementi della diagonale della matrice
diag = np.trace(matrix)
print(diag)