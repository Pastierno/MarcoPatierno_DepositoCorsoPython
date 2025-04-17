# Overriding 

class Animale:
    def emetti_suono(self):
        print("Suono generico dell'animale")
        
class Cane(Animale):
    def emetti_suono(self):
        print("Bau Bau")
        
class Gatto(Animale):
    def emetti_suono(self):
        print("Miao Miao")
        
###############
# Overloading ossia utilizzando argomenti opzionali o variadici

class Stampa:
    def mostra(self, a=None, b=None):
        if a is not None and b is not None:
            print(f"Valori: {a}, {b}")
        elif a is not None:
            print(f"Valore: {a}")
        else:
            print("Nessun valore fornito")
            
            
# Duck Typing

class Cane:
    def emetti_suono(self):
        print("Bau Bau")

class Gatto:
    def emetti_suono(self):
        print("Miao Miao")
        
def fai_emettere_suono(animale):
    print(animale.emetti_suono())
    
cane = Cane()
gatto = Gatto()

fai_emettere_suono(cane)  # Output: Bau Bau
fai_emettere_suono(gatto)  # Output: Miao Miao  

#########

class Cerchio:
    def disegna(self):
        print("Disegno un cerchio")
    
class Rettangolo:
    def disegna(self):
        print("Disegno un rettangolo")
    
def disegna_figura(figura):
    figura.disegna()

figure = [Cerchio(), Rettangolo()] # figure[0] = Cerchio(), figure[1] = Rettangolo()

for figura in figure:
    disegna_figura(figura)