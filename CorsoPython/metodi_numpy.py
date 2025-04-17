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

np.arange
# np.arange(0, 10, 2) # [0 2 4 6 8]
np.reshape(arr, (5, 1)) # [[1] [2] [3] [4] [5]]
