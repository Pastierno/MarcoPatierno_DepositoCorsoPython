class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        
    def mostra_informazioni(self):
        print(f"{self.marca}, modello {self.modello}")
        

class Dotazioni_speciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni
    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {", ".join(self.dotazioni)}")
        
class Automobile_sportiva(Veicolo, Dotazioni_speciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello) # Quando i metodi fanno confusione, nome padre
        Dotazioni_speciali.__init__(self, dotazioni)
        self.cavalli = cavalli
    
    def mostra_informazioni(self):
        super().mostra_informazioni() # Sempre, ma sopratutto quando metodo padre sovrascritto
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni() # Quanto il metodo del padre non è sovrascritto
        
        

Auto_sportiva = Automobile_sportiva("Ferrari", "F8", ["ABS", "Controllo trazione", "Airbag laterali"], 720)
Auto_sportiva.mostra_informazioni()
