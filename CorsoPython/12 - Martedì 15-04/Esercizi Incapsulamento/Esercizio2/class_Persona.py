# Classe base Persona
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def speach(self):
        return f"Mi chiamo {self.__name} e ho {self.__age} anni."
    
    def get_nome(self): # getter name
        return self.__name
    def set_nome(self, name): # setter name
        self.__name = name 
    def get_eta(self): # getter eta
        return self.__age
    def set_eta(self, age): # setter eta
        self.__age = age
        
# person1 = Person("Mario", 30)
# print(person1.speach())