# Esercizio EXTRA: unire tutti gli es. precedenti in un unico menù

# Input utente
user_input = input('Inserisci una serie di numeri separati da una virgola: ')

# Separiamo l'input in numeri singoli da inserire nella lista
num_list = user_input.split(',')

# Convertire in interi
for n in range(len(num_list)):
    num_list[n] = int(num_list[n])

# Menù scelta da effettuare
menu = int(input('Seleziona l\'operazione da effettuare: \n'
                 '1) Visualizza il massimo nella lista \n'
                 '2) Visualizza la lunghezza della lista \n'
                 '3) Stampa il quadrato dei numeri i seriti'))

match menu:
# Visualizzare il massimo
    case 1:
        print(f'Il numero massimo della lista è {max(num_list)}')
    case 2:
        print(f'La lista è lunga {len(num_list)} numeri')
    case 3:
        for n in num_list:
            print(n ** 2)
    case _:
        print('Opzione errata')
                