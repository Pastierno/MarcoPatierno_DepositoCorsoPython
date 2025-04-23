# Esercizio 2: while e range

# Input utente
user_input = int(input('Inserisci un numero intero: '))

# Contataore che prende come valore quello dell'input utente
count = user_input

# Ciclo while che stampa il valore finchè non arriva a zero il contatore
while count != -1:
    print(count)
    count -= 1
    
# Stessa cosa con range
if count != -1:
    for n in range(user_input, -1, -1):
        print(n)
        count -= 1
        
    