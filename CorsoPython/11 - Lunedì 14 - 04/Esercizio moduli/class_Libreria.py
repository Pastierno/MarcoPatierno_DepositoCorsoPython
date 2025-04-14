class Libreria():
    def __init__(self):
        self.catalogo = [] # Catalogo di libri
    
    def aggiungi_libro(self, libro): # Metodo per aggiungere libri
        self.catalogo.append(libro)
        print(f"{libro} aggiunto alla libreria")
        
    def elimina_libro(self): # Eliminare dal catalogo il libro in base all'ISBN
        isbn = int(input("Inserisci il codice ISBN: "))
        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catalogo.remove(libro)
                print(f"{libro} rimosso dal catalogo.")
                return
            print("Libro non trovato.")
            
    def cerca_per_titolo(self):
        titolo = input("Inserisci il titolo: ").strip()
        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower():
                return libro
            print("Libro nono trovato.")
    
    def mostra_catalogo(self):
        if len(self.catalogo) == 0:
            print("Libreria vuota.")
        else:
            for libro in self.catalogo:
                print(libro)