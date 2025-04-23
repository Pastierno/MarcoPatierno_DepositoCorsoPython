import numpy as np

# es.1
# cea un array di 15 elementi contenente numeri casuali tra 1 e 100
array = np.random.randint(1, 101, 15)
print(array)

# somma ditutti gli elementi dell'array
sum = np.sum(array)
print(sum)

# media degli elementi dell'array
mean = np.mean(array)
print(mean)