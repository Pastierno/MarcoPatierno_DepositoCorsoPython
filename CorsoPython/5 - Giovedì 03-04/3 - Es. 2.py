class Libro():
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    def descrizione(self):
        print(f'Il libro {self.titolo} di {self.autore} ha {self.pagine}')