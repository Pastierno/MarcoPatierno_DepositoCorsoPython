# if
num = 100
if num > 0:
    print('Numero è positivo')
    if num == 100:
        print('jolly')
elif num < 0:
    print('Numero negativo')        
else:
    print('Zero')


# match
user_input = input('Inserisci un comando: ').lower()

match user_input:
    case 'start':
        print('Avvio programma')
    case 'stop':
        print('Chiusura programma')
    case 'pausa':
        print('Programma in pausa')
    case _:
        print('Comando non riconosciuto')