import numpy as np

def menu():
    arr = None # inizializza l'array a None
    
    print("Benvenuto")
    while True:
        print("Che operazione vuoi effettuare?")
        choice = int(input("1. Crea un array di numeri equidistanti\n"
                       "2. Cambia forma dell'array creato\n"
                       "3. Genera una matrice di numeri casuali\n"
                       "4. Calcola la somma degli elementi delle matrici\n"))
        
        if choice == 1: 
            try:
                start = int(input("Da quale numero vuoi partire? "))
                stop = int(input("Fino a quale numero vuoi arrivare? "))
                size = abs(int(input("Quanti elementi vuoi l'array? "))) # valore assoluto per evitare numeri negativi
                if start >= stop: # se il numero di partenza è maggiore del numero di arrivo, chiede di nuovo i numeri
                    print("Il numero di partenza deve essere minore del numero di arrivo")
                    continue
                else:
                    arr = np.linspace(start, stop, size) # crea un array di numeri equidistanti tra start e stop
                    print(arr)
                    print("Array creato con successo")
            except ValueError:   # controllo degli errori se l'input non è un numero intero
                print("Devi inserire un numero intero")
                continue
            
        elif choice == 2:
            if arr is None: # controlla se l'array è stato creato
                print("Devi prima creare un array o una matrice.")
                continue
            try:
                righe = int(input("Quante righe vuoi?"))
                colonne = int(input("Quante colonne vuoi? "))
                if righe <= 0 or colonne <= 0:
                    print("Il numero di righe e colonne deve essere maggiore di 0")
                    continue
                if righe * colonne != size: # controllo se il numero di righe e colonne corrisponde alla dimensione dell'array
                    print("Il numero di righe e colonne non corrisponde alla dimensione dell'array")
                    continue
                arr = arr.reshape(righe, colonne)
                print(arr)
            except ValueError:
                    print("Devi inserire un numero intero")
                    continue
                
        elif choice == 3:
            righe = int(input("Quante righe vuoi?"))
            colonne = int(input("Quante colonne vuoi? "))
            start = int(input("Da quale numero vuoi partire? "))
            stop = int(input("Fino a quale numero vuoi arrivare? "))
            size = abs(int(input("Quanti elementi vuoi nella matrice? ")))
            if start >= stop:
                print("Il numero di partenza deve essere minore del numero di arrivo")
                continue
            if righe <= 0 or colonne <= 0:
                print("Il numero di righe e colonne deve essere maggiore di 0")
                continue
            if righe * colonne != size:
                print("Il numero di righe e colonne non corrisponde alla dimensione dell'array")
                continue
            arr = np.random.randint(start, stop, size)
            arr = arr.reshape(righe, colonne)
            print(arr)
            
        elif choice == 4:
            if arr is None:
                print("❗ Devi prima creare un array o una matrice (opzione 1 o 3).")
                continue
            ax = int(input("Vuoi sommare le righe o le colonne? (0 per colonne, 1 per righe) "))
            if ax == 0:
                print(np.sum(arr, axis=0)) # somma le colonne
            elif ax == 1:
                print(np.sum(arr, axis=1)) # somma le righe
            else:
                print("Devi inserire 0 o 1")
                continue
            
menu()