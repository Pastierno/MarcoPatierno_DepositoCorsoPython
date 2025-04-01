# Esercizio 3: for

# Chiede lista di numeri
user_input = input('Inserisci una serie di numeri separati da una virgola: ')

# Separiamo l'input in numeri singoli da inserire nella lista
num_list = user_input.split(',')

# Ciclo per calcolare il quadrato degli elementi
for n in num_list:
    print(int(n) ** 2)

