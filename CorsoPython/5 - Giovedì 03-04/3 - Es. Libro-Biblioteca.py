class Libro():
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    def descrizione(self):
        print(f'Il libro {self.titolo} di {self.autore} ha {self.pagine} pagine.')
        
# l1 = Libro('Harry Potter', 'J.K. Rowling', 500)

# l1.descrizione()

class Biblioteca:
    def __init__(self):
        
        # Memorizza libri creati
        self.libri = []
    
    # Metodo per creare libri
    def crea_libri(self):
        while True:
            titolo = input('Inserisci il titolo del libro: ')

            # Check lista libri
            for libro in self.libri:
                if libro.titolo == titolo:
                    print(f'Il libro "{titolo}" esiste già:')
                    libro.descrizione()
                    break
            else:
                # crea il libro se non presente in lista libri
                autore = input('Inserisci l\'autore del libro: ')
                pagine = int(input('Inserisci il numero di pagine: '))
                nuovo_libro = Libro(titolo, autore, pagine)
                self.libri.append(nuovo_libro)
                print('Libro aggiunto')
            
            # Interrompere o aggiungere ancora
            scelta = int(input('Vuoi creare un altro libro? (1- Si/2 - No): '))
            if scelta == 2:
                break
            elif scelta == 1:
                continue
            else:
                ('Scelta non disponibile')
                
    def stampa_libri(self):
        # Richiama descrizione ma prima controlla lista libri
        if not self.libri:
            print('La biblioteca è vuota.')
        else:
            print('Libri presenti in biblioteca:')
            for libro in self.libri:
                libro.descrizione()
                
#biblioteca = Biblioteca()
#biblioteca.stampa_libri()

def menu():
    # Crea istanza
    b = Biblioteca()

    while True:
        print('\nMenù')
        print('1- Crea libri')
        print('2- Stampa libri')
        print('3- Esci')
        
        scelta = input('Seleziona un\'opzione: ')
        
        
        if scelta == '1':
            b.crea_libri()
        elif scelta == '2':
            b.stampa_libri()
        elif scelta == '3':
            print('Ciao!')
            break
        else:
            print('Scelta non valida, riprova.')   
            
menu()           
 