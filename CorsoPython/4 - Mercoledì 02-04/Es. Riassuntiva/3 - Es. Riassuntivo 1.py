def recap():
    print('Ciao! Questo è un recap di tutti gli argomenti studiati nel corso \n')
    print('Argomenti trattati:')
    print('1 - Variabili e tipi di dati')
    print('2 - Liste, Tuple e Set')
    print('3 - Operatori')
    print('4 - if, elif, else')
    print('5 - match, case')
    print('6 - Cicli for e while')
    print('7 - Funzioni')
    print('8 - Decoratori')
    print('0 - Esci')
    
    # Scelta utente:
    while True:
        user_input = int(input('Scegli cosa vuoi ripetere: '))
        
        # Varie scelte
        match user_input:
            case 0:
                return False
            # Variabili e tipi di dati
            case 1:
                print('\nLe variabili sono dei contenitori per valori di diversi tipi: \n')
                print('Esempi:')
                print('- stringa = \'Marco\'')
                print('- numero = 70')
                print('- booleano = True')
                print('Puoi usare lettere, numeri e underscore (es: stringa_testo).')
                print('Non possono avere spazi (es. stringa testo) \n')
            
            # Liste, tuple e set   
            case 2:
                print('\nSono collezioni di dati')
                print('- Liste: struttura ordinata e mutabile, es: lista = [1, 2, \'ciao\']')
                print('- Tuple: struttura ordinata ma immutabile, es: tupla = (1, 2, 3)')
                print('- Set: struttura non ordinata e senza duplicati, es: insieme = {1, 2, 2, 3}') 
                
            # Operatori
            case 3:
                print('\nGli operatori sono simboli che consentono di eseguire operazioni su uno o più operanti')
                print('- Aritmetici: +, -, *, /, //, %, **')
                print('- Confronto: ==, !=, >, <, >=, <=')
                print('- Logici: and, or, not')
                print('- Appartenenza: in, not in')
                print('- Identità: is, is not')
            
            # if, elif, else
            case 4:
                print('\nIstruzioni per eseguire un blocco di codice se una condizione è verificata')
                print('Esempio di struttura:')
                print('if condizione1:')
                print('      codice1')
                print('elif condizione2:')
                print('      codice2')
                print('else:')
                print('      se non rientra nei casi precedenti')
                
            # match, case
            case 5:
                print('\nIstruzione che consente di confrontare il valore di una variabile con diversi \'casi\'')
                print('Da Python 3.10, usato come uno switch-case di altri linguaggi.')
                print('Esempio:')
                print('match variabile:')
                print('    case \'valore1\':')
                print('          azione 1')
                print('    case \'valore2\':')
                print('          azione 2')
                print('    case _:')
                print('          caso di default')
                
                
            # for e while
            case 6:
                print('\nIl for è un\'istruzione per iterare su una sequenza di elementi o su un oggetto')
                print('  es. for i in range(5):')
                print('              print(i)')
                print('Il while è un\'istruzione per eseguire un blocco di codice finchè una determinata condizione è vera')
                print('  es. while True:')
                print('           count += 1')
            
            # Funzioni
            case 7:
                print('\n Le funzioni sono blocchi di codice autonomi che possono essere richiamati all\'interno del programma')
                print('def saluta(nome):')
                print('    print(\'Ciao,\', nome)')
                print('Le funzioni possono anche essere di ritorno con la parola chiave return.')

            # Decoratori
            case 8:
                print('\nSono funzioni che modificano il comportamento di altre funzioni, senza alterarne il codice.')
                print('Esempio:')
                print('@decoratore')
                print('def saluta():')
                print('    print(\'ciao\')')
                print('Dove \'decoratore\' è un\'altra funzione che prende e ritorna una funzione wrapper.')
                print('def decoratore(funzione):')
                print('    def wrapper():')
                print('        print(\'Prima dell\'esecuzione della funzione\')')
                print('        funzione()')
                print('        print(\'Dopo l\'esecuzione della funzione\')')
                print('    return wrapper')

            case _:
                print('Scelta non valida. Riprova.')
recap()