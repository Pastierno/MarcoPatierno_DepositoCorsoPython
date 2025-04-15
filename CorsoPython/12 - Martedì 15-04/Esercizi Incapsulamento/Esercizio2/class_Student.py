# sottoclasse di Person
from class_Persona import Person

class Student(Person):
    def __init__(self, name, age, votes):
        super().__init__(name, age)  # Inizializza la classe base
        self.__votes = votes
    
    def get_votes(self):  # getter student_id
        return self.__votes
    
    def set_votes(self, votes):
        self.__votes = votes
    
    def __avg(self):
        return sum(self.__votes) / len(self.__votes) if self.__votes else 0
    # override del metodo speach
    def speach(self):
        return f"Mi chiamo {self.get_nome()} e ho {self.get_eta()} anni. La mia media è {self.__avg()}."