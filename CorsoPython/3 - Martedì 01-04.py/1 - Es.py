# Controllo ciclo while
positive = True

# Ciclo che continua in caso di intero positivo
while positive:
    
    # Input utente
    user_input = int(input('Inserisci un numero intero positivo: '))
    # Se non è intero positivo, manda errore e ripete la domanda
    if user_input < 0:
        print('Errore')
        continue
    else:
        # Primo controllo numero primo
        if user_input > 2:
            primary = True
            for i in range(2, int(user_input**0.5) + 1):
                if user_input % i == 0:
                    primary = False
                    print('Il numero non è primo')
                    break
            if primary:
                print('Il numero è primo')    
        # Liste vuore per somma e lista numeri dispari    
        num_sum = []
        num_odd = []
        for n in range(0, user_input + 1):
            if n % 2 == 0:
                num_sum.append(n)
            else:
                num_odd.append(n)
        
        print(f'Somma numeri pari fino a {user_input}: {sum(num_sum)}')
        print(f'Lista numeri dispari: {num_odd}')
        positive = False
        
        
