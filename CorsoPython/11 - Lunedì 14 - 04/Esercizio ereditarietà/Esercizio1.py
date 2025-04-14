class Animale():
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def fai_suono(self):
        print(f"{self.nome} emette un suono.")
        
class Capibara(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta) # Prendo da classe animale nome ed età

    def fai_suono(self):
        print("'Nome di verso sconosciuto'")

    def nuota(self): # Metodo specifico nel capibara
        print(f"{self.nome} sta nuotando serenamente nel {self.ambiente}.")
        

class Ermellino(Animale):
    def __init__(self, nome, eta, velocita):
        super().__init__(nome, eta)
        self.velocita = velocita # Aggiungo attributo in più a classe padre

    def fai_suono(self):
        print("Neanche di questo si trova il verso?!")

    def caccia(self):
        print(f"{self.nome} caccia con una velocità di {self.velocita} km/h")
        
        
class Rinoceronte(Animale):
    def __init__(self, nome, eta, peso):
        super().__init__(nome, eta)
        self.peso = peso  # Attributo aggiunto, peso

    def fai_suono(self):
        print("'Boh'")

    def carica(self):
        print(f"{self.nome}, dal peso di {self.peso} tonnellate, carica.")
        
Bara = Capibara("Capi", 3)
ErmelMeta = Ermellino("Mellino", 2, 60)
Rino = Rinoceronte("Rino", 15, 3)

Bara.fai_suono()
Rino.carica()