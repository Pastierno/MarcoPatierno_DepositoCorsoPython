# Esercizio Base

# Liste vuote dove aggiungere input
num_list = []
str_list = []

# Controllo while
do = True
# Input utente per numero o stringa:
while do:
    user_input = int(input('Vuoi inserire un numero o una stringa? \n'
                        '1 - Numero \n'
                        '2 - Stringa \n'))

    match user_input:
        # In caso di scelta "numeri"
        case 1:
            num = int(input('Inserisci un numero: '))
            num_list.append(num)
            if num % 2 == 0:
                print('Il numero è pari')
                
                # Scelta di ripetere la selezione o stampare il risultato
                loop = int(input('Vuoi ripetere? (1 Si/ 2 No)'))
                if loop == 1:
                    continue
                elif loop == 2:
                    print(num_list)
                    break
                else:
                    print('Scelta errata, riprova')
                    continue
            else:
                print('Il numero è dispari')
                
                # Scelta di ripetere la selezione o stampare il risultato)
                loop = int(input('Vuoi ripetere? (1 Si/ 2 No)'))
                if loop == 1:
                    continue
                elif loop == 2:
                    print(num_list)
                    break
                else:
                    print('Scelta errata, riprova')
                    continue

        # In caso di scelta "stringhe"
        case 2:
            s = input('Inserisci una parola: ')
            str_list.append(s)
            
            # Scelta di ripetere la selezione o stampare il risultato)
            if len(s) % 2 == 0:
                print('La parola è pari')
                loop = int(input('Vuoi ripetere? (1 Si/ 2 No)'))
                if loop == 1:
                    continue
                elif loop == 2:
                    print(str_list)
                    break
                else:
                    print('Scelta errata, riprova')
                    continue
            else:
                print('La parola è dispari')
                
                # Scelta di ripetere la selezione o stampare il risultato)
                loop = int(input('Vuoi ripetere? (1 Si/ 2 No)'))
                if loop == 1:
                    continue
                elif loop == 2:
                    print(str_list)
                    break
                else:
                    print('Scelta errata, riprova')
                    continue
        # In caso di scelta errata       
        case _:
            ('Scelta non valida, riprova!')

