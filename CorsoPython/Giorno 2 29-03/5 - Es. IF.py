# Esercizio 1: Pari o dispari

# Numero scelto dall'utente
user_input = int(input('Inserisci un numero intero: '))

# Verifica se pari o dispari
if user_input % 2 == 0:
    print(f'{user_input} è pari')
else:
    print(f'{user_input} è dispari')