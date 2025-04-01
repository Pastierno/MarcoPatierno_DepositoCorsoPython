# Input utente
user_input = int(input('Inserisci un numero intero: '))

# Verifica numero pari
if user_input % 2 == 0:
    print(f'Il numero {user_input} è pari')
else:
    print(f'Il numero {user_input} è dispari')
    
# Verifica numero primo
if user_input < 2:
    print(f"{user_input} non è primo.")
else:
    primary = True
    # Verifica divisore
    for i in range(2, int(user_input ** 0.5) + 1):
        if user_input % i == 0:
            primary = False
            break
    
    # Risultato
    if primary:
        print(f"{user_input} è primo.")
    else:
        print(f"{user_input} non è primo.")

    