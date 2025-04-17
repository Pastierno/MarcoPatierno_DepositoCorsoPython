import numpy as np

def menu():
    while True:
        try:
            start = int(input("Crea un array\n"
                            "Da quale numero vuoi partire? "))
            stop = int(input("Fino a quale numero vuoi arrivare? "))
            size = abs(int(input("Quanti elementi vuoi l'array? "))) # valore assoluto per evitare numeri negativi
            if start >= stop: # se il numero di partenza è maggiore del numero di arrivo, chiede di nuovo i numeri
                print("Il numero di partenza deve essere minore del numero di arrivo")
                continue
        except ValueError:   # controllo degli errori se l'input non è un numero intero
            print("Devi inserire un numero intero")
            continue
        arr = np.random.randint(start, stop, size)
        
        print(arr)
        
        reshape = input("Vuoi fare un reshape? (s/n) ").strip().lower()
        if reshape == "s":
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
        elif reshape == "n":
            pass
        else:
            print("Devi inserire s o n")
            continue
        
        continua = input("Vuoi continuare? (s/n) ").strip().lower()
        if continua == "n":
            break
       
    
    
    
    
menu()