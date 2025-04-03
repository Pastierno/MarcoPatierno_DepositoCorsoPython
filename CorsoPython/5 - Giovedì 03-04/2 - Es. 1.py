class Punto:
    # Costruttore
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # Metodo per 'muovere' il punto    
    def muovi(self):
        self.x = int(input('Inserisci una coordinata per il punto x: '))
        self.y = int(input('Inserisci una coordinata per il punto y: '))
    
    # Metodo    
    def distanza_da_origine(self):
        
        # Calcola la distanza dall'origine
        distanza = (self.x**2 + self.y**2) ** 0.5
        print('La distanza dall\'origine è:', distanza)

p1 = Punto()
p1.muovi()
p1.distanza_da_origine()