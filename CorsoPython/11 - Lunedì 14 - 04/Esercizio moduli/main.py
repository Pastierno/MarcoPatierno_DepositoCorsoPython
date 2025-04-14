import class_Libreria as cl
import class_Libro as cb

def menu():
    Libreria1 = cl.Libreria() # Istanzxa Libreria
    while True:
        print("Benvenuto nella libreria")
        print("1. Aggiungi Libro")
        print("2. Elimina Libro")
        print("3. Cerca Libro per Titolo")
        print("4. Mostra Catalogo")
        print("5. Esci")
        scelta = input("Scegli un'opzione: ").strip() # Scelta utente
        
        if scelta == "1":
            Libreria1.aggiungi_libro()
        elif scelta == "2":
            Libreria1.elimina_libro()
        elif scelta == "3":
            libro_trovato = Libreria1.cerca_per_titolo()
            if libro_trovato:
                print("Libro trovato:")
                print(libro_trovato)
        elif scelta == "4":
            Libreria1.mostra_catalogo()
        elif scelta == "5":
            print("Uscita dal programma... Alla prossima!")
            break
        else:
            print("Opzione non valida. Riprova.")


menu()