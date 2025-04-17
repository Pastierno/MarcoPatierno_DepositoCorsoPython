import numpy as np

class Array:
    def __init__(self, start, stop, size):
        self.linspace = np.linspace(start, stop, size)
        self.random = np.random.random(size)
        self.sum = self.linspace + self.random
    
    def show_array(self):
        print(f"Array linspace: {self.linspace}")
        print(f"Array random: {self.random}")
        print(f"Somma dei due array: {self.sum}")
          
    def total_sum(self):
        print(f"Somma del nuovo array:  {np.sum(self.sum)}")
        
    def sum_greater_than(self, threshold):
        return np.sum(self.linspace[self.linspace > threshold])
    
    
    
# arr1 = Array(0, 10, 5)
# arr1.show_array()
# arr1.total_sum()
# arr1.sum_greater_than(5)