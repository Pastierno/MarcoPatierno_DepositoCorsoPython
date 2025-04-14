class Animale(): # Classe padre
    def __init__(self, nome):
        self.nome = nome
        
    def parla(self):
        print(f"{self.nome} fa suono generico")

# Classe derivata (eredita da Animale)        
class Cane(Animale): # Classe figlia
    def parla(self):
        print(f"{self.nome} abbaia!")
        
Animale_generico = Animale("Qualsiasi")
Cane1 = Cane("Fido")

Animale_generico.parla()
Cane1.parla()

