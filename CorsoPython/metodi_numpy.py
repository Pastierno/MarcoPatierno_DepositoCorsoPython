import numpy as np

arr = np.array([1, 2, 3, 4, 5])

arr.shape # (5,)
arr.ndim # 1
arr.dtype # dtype('int64')
arr.size # 5
arr.sum() # 15
arr.mean() # 3.0
arr.std() # 1.4142135623730951
arr.max() # 5
arr.min() # 1
arr.argmax() # 4 ossia l'indice del valore massimo
arr.var() # 2.0
arr.cumsum() # [ 1  3  6 10 15] ossia la somma cumulativa
arr.cumprod() # [  1   2   6  24 120] ossia il prodotto cumulativo
arr.sort() # [1 2 3 4 5] ordina in loco
arr.argsort() # [0 1 2 3 4] ossia gli indici ordinati
np.arange
# np.arange(0, 10, 2) # [0 2 4 6 8]
np.reshape(arr, (5, 1)) # [[1] [2] [3] [4] [5]]


# Operazioni aritmetiche:
np.add()
np.subtract()
np.multiply()
np.divide()
np.power()
np.remainder() # resto della divisione
np.floordiv() # divisione intera
np.mod() # modulo
np.divmod() # divisione e resto

# Funzioni matematiche:
np.sin()
np.cos()
np.tan()
np.arcsin()
np.arccos()
np.exp()

# Funzioni statistiche:
np.mean()
np.median()
np.std()
np.var()

# Prodotto maticiale:
np.dot()
# se entrambi gli array sono 2D, fa il prodotto matriciale
# se uno è 1D e l'altro è 2D, fa il prodotto tra il vettore e la matrice
# se entrambi sono 1D, fa il prodotto scalare

np.matmul() # fa il prodotto matriciale in broadcasting (ovvero modifica le dimensioni degli array per fare il prodotto)
# se entrambi gli array sono 2D, fa il prodotto matriciale
# se uno è 1D e l'altro è 2D, fa il prodotto tra il vettore e la matrice
# se entrambi sono 1D, fa il prodotto scalare

# determinante: misura quanto allarga o schiaccia uno spazio di trasformazione lineare
np.linalg.det() # calcola il determinante di una matrice
# se il determinante è 0, la matrice non è invertibile

# autovalori e autovettori: sono i valori e i vettori che non cambiano direzione quando vengono moltiplicati per la matrice
np.linalg.eig() # calcola gli autovalori e gli autovettori di una matriceù

# Risopluzione di sistemi lineari:
# Ax = b
# A è la matrice dei coefficienti, x è il vettore delle incognite, b è il vettore dei termini noti
np.linalg.solve() # risolve il sistema lineare Ax = b senza calcolare l'inversa di A