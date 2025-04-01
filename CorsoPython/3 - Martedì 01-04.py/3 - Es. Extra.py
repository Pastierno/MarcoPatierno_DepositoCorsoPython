import random as rnd

# Funzione per determinare se n è primo
def is_primary(n):
    if n > 2:
        primary = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                primary = False
                return False
        if primary:
            return True
        
# print(is_primary(6))

# Controllo ciclo whiule
positive = True

# Ciclo che continua in caso di intero positivo
while positive:
    
    # Input utente
    user_input = int(input('Inserisci un numero intero positivo: '))
    user_input2 = int(input('Inserisci un altro numero intero positivo: '))
    
    # Se non è intero positivo, manda errore e ripete la domanda
    if user_input < 0 or user_input2 < 0:
        print('Errore')
        continue
    else:
        # Liste vuore per somma e lista numeri dispari e numeri casuali da 1 a n
        random_list = [rnd.randint(user_input, user_input2) for i in range(user_input, user_input2)]    
        num_sum = []
        num_odd = []
        
        # Ciclo per inserire i numeri da 1 a input utente nelle liste
        for n in range(user_input, user_input2 + 1):
            if n % 2 == 0:
                num_sum.append(n)
            else:
                num_odd.append(n)
        
        print(f'Somma numeri pari è: {sum(num_sum)}')
        print(f'Lista numeri dispari: {num_odd}')
        
        # Manda a schermo se il numero inserito dall'utente è primo o no
        if is_primary(user_input):
            print(f'{user_input} è un numero primo')
        else:
            print(f'{user_input} non è un numero primo')
            
        # Manda a schermo tutti i numeri primi nella lista randomica
        primary_list = []
        for n in random_list:
            if is_primary(n):
                primary_list.append(n)
                
        print(f'La lista contiene i seguenti numeri primi: {primary_list}')
        
        # Somma di tutti i numeri è un numero primo?
        if is_primary(sum(random_list)):
            print(f'La somma di tutti i numeri è {sum(random_list)} ed è primo')
        else:
            print(f'La somma di tutti i numeri è {sum(random_list)} e non è primo')
        positive = False