import random as r
# numeri_casuali = r.sample(range(1,11), 5)

# Funzione per scrivere un file
def scrivi(numeri):
    with open('file.txt', 'w') as file:
        file.write(str(numeri))

# Funzione per leggere il file        
def leggi(percorso):
    with open(percorso, 'r') as file:
        contenuto = file.read()
    return contenuto

# Funzione con menù per giocare
def gioco():
    print('\nBenvenuto, prova ad indovinare 2 numeri')
    
    # Scelta del range da parte dell'utente
    range1 = int(input('I numeri saranno casuali, scegli il range \n'
                       'Digita da dove parte il range: '))
    range2 = int(input('Dove arriva: '))
    # Assegna numeri casuali nel range scelto dall'utente
    numeri_casuali = r.sample(range(range1, range2 + 1), 2)
    
    # Scrive nel file i numeri casuali
    scrivi(numeri_casuali)
        
    print('\nProva ad indovinare i due numeri generati: ')
    numero1 = int(input('Primo numero: '))
    numero2 = int(input('Secondo numero: '))
    
    # Numeri scelti dall'utente
    numeri = [numero1, numero2]
    
    # Calcola quanti numeri sono stati indovinati
    indovinati = len([n for n in numeri if n in numeri_casuali])

    
    if indovinati == 2:
        print('Hai indovinato due numeri')
    elif indovinati == 1:
        print('Hai indovinato un numero')
    else:
        print('Non hai indovinatoi nessun numero')
        
    print('I numeri generati erano:', numeri_casuali)
    
    print(leggi('file.txt')) # Legge il file con i numeri generati casualmente
gioco()
    
    
    
