import numpy as np
from esercizio5 import Array

def menu():
    arr = None # inizializza l'array a None
    print("Benvenuto")
    while True:
        print("1. Crea un array")
        print("2. Mostra gli array")
        print("3. Somma del nuovo array")
        print("4. Somma degli elementi maggiori di un valore soglia")
        choice = int(input("Scegli un'opzione (0 per uscire): "))
        
        if choice == 1:
            start = int(input("Inserisci il valore di partenza: "))
            stop = int(input("Inserisci il valore di arrivo: "))
            size = int(input("Inserisci la dimensione dell'array: "))
            if size <= 0:
                print("La dimensione dell'array deve essere maggiore di zero.")
                return
            if start >= stop:
                print("Il valore di partenza deve essere minore del valore di arrivo.")
                return
            arr = Array(start, stop, size) # istanza della classe Array
            print("Array creato.")        
            
        elif choice == 2 and arr is not None:
            arr.show_array()
        
        elif choice == 3 and arr is not None:
            arr.total_sum()
            
        elif choice == 4 and arr is not None:
            threshold = int(input("Inserisci il valore soglia: "))
            result = arr.sum_greater_than(threshold)
            print(f"Somma degli elementi maggiori di {threshold}: {result}")
            
        elif choice == 0:
            break
        else:
            print("Opzione non valida o array non creato.")
            continue
            
            
menu()