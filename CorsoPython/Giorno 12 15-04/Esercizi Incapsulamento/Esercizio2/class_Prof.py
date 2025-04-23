# sottoclasse di Person
from class_Persona import Person

class Prof(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # Inizializza la classe base
        self.__subject = subject
    
    def get_subject(self):  # getter subject
        return self.__subject
    
    def set_subject(self, subject):
        self.__subject = subject
    
    # override del metodo speach
    def speach(self):
        return f"Mi chiamo {self.get_nome()} e ho {self.get_eta()} anni. Insegno {self.get_subject()}."