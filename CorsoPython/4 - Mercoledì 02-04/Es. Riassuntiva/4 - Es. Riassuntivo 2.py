def decoratore1(func):
    def wrapper(*args, **kwargs):
        print(f'\nStai visualizzando: {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Hai visualizzato: {func.__name__}\n')
        return result
    return wrapper

def decoratore2(func):

    def wrapper(*args, **kwargs):
        while True:
            func(*args, **kwargs)
            ripeti = int(input('Vuoi ripetere questa spiegazione?: \n'
                           '1 - Si \n'
                           '2 - No \n'))
            if ripeti == 2:
                break
    return wrapper


@decoratore2
@decoratore1
def variabili_e_tipi():
    print('\nLe variabili sono dei contenitori per valori di diversi tipi:\n')
    print('Esempi:')
    print('- stringa = \'Marco\'')
    print('- numero = 70')
    print('- booleano = True')
    print('Puoi usare lettere, numeri e underscore (es: stringa_testo).')
    print('Non possono avere spazi (es. stringa testo)\n')

@decoratore2
@decoratore1
def liste_tuple_set():
    print('\nSono collezioni di dati:')
    print('- Liste: struttura ordinata e mutabile, es: lista = [1, 2, \'ciao\']')
    print('- Tuple: struttura ordinata ma immutabile, es: tupla = (1, 2, 3)')
    print('- Set: struttura non ordinata e senza duplicati, es: insieme = {1, 2, 2, 3}')

@decoratore2
@decoratore1
def operatori():
    print('\nGli operatori sono simboli che consentono di eseguire operazioni su uno o più operandi.')
    print('- Aritmetici: +, -, *, /, //, %, **')
    print('- Confronto: ==, !=, >, <, >=, <=')
    print('- Logici: and, or, not')
    print('- Appartenenza: in, not in')
    print('- Identità: is, is not')

@decoratore2
@decoratore1
def if_elif_else():
    print('\nIstruzioni per eseguire un blocco di codice se una condizione è verificata.')
    print('Esempio di struttura:')
    print('\nif condizione1:')
    print('      codice1')
    print('elif condizione2:')
    print('      codice2')
    print('else:')
    print('      se non rientra nei casi precedenti')

@decoratore2
@decoratore1
def match_case():
    print('\nIstruzione che consente di confrontare il valore di una variabile con diversi "casi".')
    print('Esempio:')
    print('\nmatch variabile:')
    print('    case \'valore1\':')
    print('          azione 1')
    print('    case \'valore2\':')
    print('          azione 2')
    print('    case _:')
    print('          caso di default')

@decoratore2
@decoratore1
def cicli():
    print('\nIl for è un\'istruzione per iterare su una sequenza di elementi o su un oggetto.')
    print('  es. for i in range(5):')
    print('              print(i)')
    print('Il while è un\'istruzione per eseguire un blocco di codice finché una determinata condizione è vera.')
    print('  es. while True:')
    print('           count += 1')

@decoratore2
@decoratore1
def funzioni():
    print('\nLe funzioni sono blocchi di codice autonomi che possono essere richiamati all\'interno del programma.')
    print('\ndef saluta(nome):')
    print('    print(\'Ciao,\', nome)')
    print('Le funzioni possono anche essere di ritorno con la parola chiave return.')

@decoratore2
@decoratore1
def decoratori():
    print('\nSono funzioni che modificano il comportamento di altre funzioni, senza alterarne il codice.')
    print('Esempio:')
    print('\n@decoratore')
    print('def saluta():')
    print('    print(\'ciao\')')
    print('Dove \'decoratore\' è un\'altra funzione che prende e ritorna una funzione wrapper.')
    print('def decoratore(funzione):')
    print('    def wrapper():')
    print('        print(\'Prima dell\'esecuzione della funzione\')')
    print('        funzione()')
    print('        print(\'Dopo l\'esecuzione della funzione\')')
    print('    return wrapper')

# Funzione principale
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

        # Scelte
        match user_input:
            case 0:
                print('Ciao!')
                return False

            case 1:
                variabili_e_tipi()
            case 2:
                liste_tuple_set()
            case 3:
                operatori()
            case 4:
                if_elif_else()
            case 5:
                match_case()
            case 6:
                cicli()
            case 7:
                funzioni()
            case 8:
                decoratori()
            case _:
                print('Scelta non valida. Riprova.')

recap()
