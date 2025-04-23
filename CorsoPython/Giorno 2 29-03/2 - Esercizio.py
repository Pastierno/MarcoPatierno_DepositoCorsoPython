# Secondo esercizio

num1 = int(input('Inserisci il primo numero: '))
num2 = int(input('Inserisci il secondo numero: '))

# Menù scelta operazione
menu = int(input('Scegli l\'operazione da effettuare: \n'
                 '1) Addizione + \n'
                 '2) Sottrazione - \n'
                 '3) Moltiplicazione * \n'
                 '4) Divisione / \n'))

if menu == 1:
    print(f'{num1} + {num2} = {num1 + num2}')
elif menu == 2:
    print(f'{num1} - {num2} = {num1 - num2}')
elif menu == 3:
    print(f'{num1} * {num2} = {num1 * num2}')
elif menu == 4:
    # Condizione nel caso di denominatore = 0
    if num2 == 0:
        print('Errore: Divisione per zero')
    else:
        print(f'{num1} / {num2} = {num1 / num2}')
else:
    print('Scelta non valida')
    
