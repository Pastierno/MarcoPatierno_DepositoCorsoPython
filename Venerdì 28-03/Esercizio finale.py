# Esercizio finale
#____________________________________________________________________________________________________________________


# Credenziali di accesso e domanda/risposta segreta 
login = ['admin', '12345']
secret_question = []

# Messaggio di benvenuto ed input utente
print(
    'Benvenuto! \n'
    'Per continuare inserisci le credenziali di accesso \n'
)
username = input('Inserisci nome utente: ').lower()
password = input('Inserisci password: ')

# Authentication con condizioni
if username == login[0] and password == login[1]:
    print(f'Ciao {username}!\n')
    
    #Scelta domanda segreta per continuare
    question = int(input('Scegli la domanda di sicurezza (1/2): \n'
                  '1) Qual è il tuo colore preferito? \n'
                  '2) Qual è il cognome da nubile di tua madre? \n'))
    
    # Scelta risposta segreta
    if question == 1:
            secret_question.append('Qual è il tuo colore preferito? \n')
            answer = input('Inserisci la tua risposta segreta: \n').lower()
            print('Risposta salvata! \n')
            secret_question.append(answer)
    elif question == 2:
            secret_question.append('Qual è il cognome da nubile di tua madre? \n')
            answer = input('Inserisci la tua risposta segreta: \n').lower()
            print('Risposta salvata! \n')
            secret_question.append(answer)
    else:
            print('Opzione non esistente')
            
            
    # Menu cambio username o password           
    menu = int(input('Che operazione vuoi effettuare? \n'
              '1) Modifica nome utente \n'
              '2) Modifica password \n'))
    if menu == 1:
            new_username = input('Inserisci il nuovo nome utente: \n').lower()
            print('Nome utente modificato con successo! \n')
            login[0] = new_username
    elif menu == 2:
            new_password = input('Inserisci la nuova password: \n').lower()
            print('Password modificata con successo! \n')
            login[1] = new_password
    else:
            print('Opzione non esistente')
else:
    print('Credenziali errate, ritenta')
    

