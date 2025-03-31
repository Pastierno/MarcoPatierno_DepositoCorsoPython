# Controllo per il ciclo while
on = True

while on:
    # Scelta del numero intero
    user_input = int(input('Inserisci un numero intero: '))

    # Ciclo per conto alla rovescia
    for num in range(user_input, -1, -1):
        # Quando arriva a zero si ferma
        if num != 0:
            print(num)
            
        # Replay conto alla rovescia
        else:
            choose = int(input('Vuoi ripetere? \n'
                      '1) Si \n'
                      '2) No \n'))
            if choose == 1:
                break
            elif choose == 2:
                print('Ciao!')
                on = False
                break
            else:
                print('Opzione non esistente')
                on = False
                break

        

