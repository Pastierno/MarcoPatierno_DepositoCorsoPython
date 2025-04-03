# Prime classi

class Car():
    wheels = 4
    def __init__(self, brand, model): # self è l'oggetto stesso, sostituire mentalmente (in questo caso car1 o car2)
        self.brand = brand
        self.model = model
        
    # Metodo
    def info(self):
        print(f'L\'auto è una {self.brand}, {self.model}')

# Oggetti di tipo automobile        
Car1 = Car('Fiat', 'Panda')
Car2 = Car('Mercedes', 'Class C220')

Car1.info()
print(Car1.wheels)

#________________________________________________________________________________________

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# Oggetti persona
P1 = Person('Marco', 26)

print(P1.name)
print(P1.age)

print(type(P1))
print(type(P1.name))
print(type(P1.age))

#_________________________________________________________________________________________
# Metodo statico
class Calculator():
    @staticmethod
    def sum (a, b):
        return a+b
    
res = Calculator.sum(1, 2)
print(res)

# Metodo di classe (con decoratore)
class Counter():
    count = 0 # Attributo di classe
    
    def __init__(self):
        Counter.count += 1
        
    @classmethod
    def show_count(cls):
        print(f'Sono state contate {cls.count} istanze.')
        
C1 = Counter() # Aumenta count 1
C2 = Counter() # Aumenta count 2 
C3 = Counter()
C4 = Counter()

Counter.show_count()

