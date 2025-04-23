from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass
    
class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
        
    def area(self):
        return self.base * self.altezza
    
    def perimetro(self):
        return 2 * (self.base + self.altezza)
    
f = Forma() # non posso creare un'istanza di una classe astratta

r = Rettangolo(5, 10)
print(r.area())  # Output: 50
print(r.perimetro())  # Output: 30  