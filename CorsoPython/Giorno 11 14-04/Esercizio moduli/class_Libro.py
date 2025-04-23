class Libro():
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
    # Metodo per restituire stringa anzichè object
    def __str__(self):
        return f"{self.titolo} di {self.autore} con codice ISBN-{self.isbn}"
    # Metodo per stampare descrizione di ogni libro
    def descrizione(self):
        print(self.__str__())
        
Libro1 = Libro("Harry Potter", "J. K. Rowling", "45635342")

Libro1.descrizione()
print(Libro1.isbn)