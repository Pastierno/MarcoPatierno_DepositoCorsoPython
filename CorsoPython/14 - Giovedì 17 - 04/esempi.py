import numpy as np

arr = np.array([1, 2, 3])
print(arr)

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)


arr = np.array([1,2,3], dtype="int32")
print(arr.dtype) # int32

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)

arr = np.arange(10)
print(arr) # [0 1 2 3 4 5 6 7 8 9]

arr = arr.reshape((2, 5))
print(arr) # [[0 1 2] [3 4 5]]

# Indexing
arr = np.array([1,2,3,4,5])

print(arr[0]) # 1

# Slicing
print(arr[1:3]) # [2 3]

# Boolean indexing
print(arr[arr > 2]) # [3 4 5]

# In caso di array multidimensionale

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(arr2d[0, 1]) # 2

print(arr2d[1:3]) # [[4 5 6] [7 8 9]]

print(arr2d[:, 1:3]) # [[2 3] [5 6] [8 9]]

print(arr2d[1:, 1:3]) # [[5 6] [8 9]]

# Fancy indexing
arr = np.array([1, 2, 3, 4, 5])
indici = np.array([0, 2, 4])
print(arr[indici]) # [1 3 5]