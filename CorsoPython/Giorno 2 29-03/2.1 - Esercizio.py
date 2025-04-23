num1 = int(input('Inserisci il primo numero: '))
num2 = int(input('Inserisci il secondo numero: '))

# Operazioni
sum = (f'{num1} + {num2} = {num1+num2}')
diff = (f'{num1} - {num2} = {num1-num2}')
mult = (f'{num1} * {num2} = {num1*num2}')
divis = (f'{num1} / {num2} = {num1/num2}')


# Menù scelta operazione
menu = int(input('Scegli l\'operazione da effettuare: \n'
                 '1) Addizione + \n'
                 '2) Sottrazione - \n'
                 '3) Moltiplicazione * \n'
                 '4) Divisione / \n'))

match menu:
    case 1:
        # Scelta per aggiungere operazione
        add_op = int(input('Vuoi aggiungere un\'altra operazione? \n'
                  '1) No \n'
                  '2) Sottrazione - \n'
                  '3) Moltiplicazione * \n'
                  '4) Divisione / '))
        if add_op == 1:
            print(sum)
        # Operazioni doppie
        elif add_op == 2:
            print(sum, diff)
        elif add_op == 3:
            print(sum, mult)
        elif add_op == 4:
            if num2 != 0:
                print(sum, divis)
            else:
                print('Errore, divisione per zero')
            
    case 2:
        add_op = int(input('Vuoi aggiungere un\'altra operazione? \n'
                  '1) No \n'
                  '2) Addizione + \n'
                  '3) Moltiplicazione * \n'
                  '4) Divisione / '))
        if add_op == 1:
            print(diff)
        # Operazioni doppie
        elif add_op == 2:
            print(diff, sum)
        elif add_op == 3:
            print(diff, mult)
        elif add_op == 4:
            if num2 != 0:
                print(diff, divis)
            else:
                print('Errore, divisione per zero')
    case 3:
        add_op = int(input('Vuoi aggiungere un\'altra operazione? \n'
                  '1) No \n'
                  '2) Addizione + \n'
                  '3) Sottrazione * \n'
                  '4) Divisione / '))
        if add_op == 1:
            print(mult)
        # Operazioni doppie
        elif add_op == 2:
            print(mult, sum)
        elif add_op == 3:
            print(mult, diff)
        elif add_op == 4:
            if num2 != 0:
                print(mult, divis)
            else:
                print('Errore, divisione per zero')
    case 4:
        add_op = int(input('Vuoi aggiungere un\'altra operazione? \n'
                  '1) No \n'
                  '2) Addizione +'
                  '3) Moltiplicazione * \n'
                  '4) Sottrazione - '))
        if add_op == 1:
            if num2 != 0:
                print(divis)
            else:
                print('Errore, divisione per zero')
        # Operazioni doppie
        elif add_op == 2:
            if num2 != 0:
                print(divis, sum)
            else:
                print('Errore, divisione per zero')
        elif add_op == 3:
            if num2 != 0:
                print(divis, mult)
            else:
                print('Errore, divisione per zero')
        elif add_op == 4:
            if num2 != 0:
                print(divis, diff)
            else:
                print('Errore, divisione per zero')
        
    case _:
        print('Errore nella scelta')
        
    
