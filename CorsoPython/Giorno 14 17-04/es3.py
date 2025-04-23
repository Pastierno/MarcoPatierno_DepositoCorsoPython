import numpy as np
# es 3
# crea un array di forma 4,4 con numeri casuali interi tra 10 e 50
matrix2 = np.random.randint(10, 51, (4, 4))
print(matrix2)

# fancy indexing per stampare (0,1), (1,3), (2,2), (3,0)
fancy_index = matrix2[[0, 1, 2, 3], [1, 3, 2, 0]]
print(fancy_index)

# fancy indexing per selezionare righe dispari
fancy_index = matrix2[0::2, :]
print(fancy_index)

# elementi selezionai nel primo punto + 10
fancy_index = matrix2[[0, 1, 2, 3], [1, 3, 2, 0]] + 10
print(fancy_index)