import numpy as np

a = np.array([[1, 2], [3, 4]])

# inversa
a_inv = np.linalg.inv(a)
print(a_inv)

# Norma del vettore
v = np.array([3, 4])

norm_v = np.linalg.norm(v)
print(norm_v)

# Broadcasting
arr = np.array([1,2,3,4])
scalar = 10
# Broadcasting aggiunge lo scalar a ogni elemento dell'array
result = arr + scalar
print(result)  # Output: [11 12 13 14]

# Riassunto
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b # somma elemento per elemento

d = np.sin(a) # applica la funzione seno a ogni elemento di a

e = np.dot(a, b) # prodotto scalare tra a e b

f = a + 10 # somma 10 a ogni elemento di a