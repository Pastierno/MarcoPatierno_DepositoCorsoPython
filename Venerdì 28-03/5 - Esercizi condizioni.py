# Primo esercizio

# Input che inserisce utente
user_input = int(input('Inserisci un numero: '))

# Primo controllo
if user_input > 0:
    print('Numero positivo')
    user_input = int(input('Inserisci un altro numero: '))
    # Secondo controllo
    if user_input > 50:
        print('Numero maggiore di 50')
        user_input = int(input('Inserisci un ultimo numero: '))
        # Terzo controllo e bonus sul 100
        if user_input == 100:
            print('Super')
        elif user_input > 100:
            print('Numero maggiore di 100')
        else:
            print('Numero minore di 100')
    else:
        print('Numero minore di 50')
else:
    print('Numero negativo')
    
# Secondo esercizio

# Stampa contenuto lista
num = [1,2,3,4,5]
print(num) 

# Scelta operazione da effettuare tramite input
user_input = int(input('Che operazione vuoi effettuare? Digita 0 per aggiungere, 1 per rimuovere l\'ultimo elemento della lista, 2 per svuotare la lista: '))

# Aggiunta numero scelto dall'utente
if user_input == 0:
    input_num = int(input('Digita il numero (intero) che vuoi aggiungere: '))
    num.append(input_num)

# Eliminare ultimo elemento della lista
elif user_input == 1:
    print('Elemento eliminato')
    num.pop()
    
# Svuotare lista
elif user_input == 2:
    print('Lista svuotata')
    num.clear()

# Errore nella scelta nel menù
else:
    print('Scelta non corretta')
    
    
# Terzo esercizio

accounts = []

user_input = int(input('Vuoi creare un nuovo account o accedere? (0 creare, 1 accedere)'))

if user_input == 0:
    email = input('Inserisci email: ').lower()
    password = input('Inserisci una password: ')
    print('Account creato!')
    account.append([email, password])

elif user_input == 1:
    account = []
    email = input('Inserisci email: ')
    password = input('Inserisci password: ')
    account.append([email, password])
    if account[0] == accounts[0]:
        print(f'Accesso effettuato {email}')
else:
    print('Credenziali errate')    
    
    
      
    

    
