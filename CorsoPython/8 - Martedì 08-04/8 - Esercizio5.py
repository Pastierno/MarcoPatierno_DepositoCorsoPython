# Trasformate il programma che abbiamo creato in
# precedenza per la gestione dei voti degli alunni in un
# programma per la gestione di una classe che utilizza un
# file come database:
# All’avvio il programma chiede se si vuole leggere l’elenco
# degli alunni e i loro voti e medie, se si vuole aggiungere un
# alunno con i voti

db = 'registro.txt' # Variabile con path file registro

def carica_dati(database): # Per caricare un dizionario con dati del file
    dati = {}
    try:
        with open(database, 'r') as file:
            righe = file.readlines()
    except:
        print('Registro non trovato')
        return {}
            
# carica_dati(db) # Controllo

    if not righe: # Controllo se file esiste ma non è scritto nulla
        print('Il registro è vuoto')
        return {}
        
    for riga in righe: # per ogni riga separa il nome dai voti in due variabili
        riga = riga.strip()
        if riga:
            parti = riga.split(':')
            nome = parti[0].strip()
            voti = parti[1].strip()
            
            voti_num = []
            if voti:
                # Conversione in float per caricare dati su dizionario
                voti_num = [float(v.replace(',', '.')) for v in voti.split(',')]
            dati[nome] = voti_num
                
    return dati

def apri_registro(database): # Funzione che apre un file passato come argomento
    dati = carica_dati(database)
    
    print('\n Elenco degli alunni e voti: ')
    for nome, voti in dati.items():
        media = calcola_media(voti)
        print(f'Alunno: {nome}, Voti: {', '.join(str(v) for v in voti)}, Media: {media:.2f}')

def calcola_media(voti): # Calcolo della media

                
                
                
    return sum(voti)/len(voti)

def scrivi_registro(database, dati): # solo per write su file
    # Scrive su file le righe con nome e relativi voti
    with open(database, 'w') as file:
        for nome, voti in dati.items():
            voti_stringa = ','.join(str(v) for v in voti)
            riga = f"\n{nome}: {voti_stringa}"
        file.write(riga) 
                 
def aggiungi_alunno(database):
    dati = carica_dati(database)   
    
    nome = input('\nInserisci il nome dell\'alunno: ').strip()
    if not nome.isalpha(): # Controllo per avere solo caratteri alfanumerici
        print('Non valido, riprova.')
        return
    
    print('\nInserisci i voti uno alla volta. Premi invio senza compilare per inserire.')
    lista_voti = []
    while True:
        voto_stringa = input('Inserisci un voto: ').strip() #float(input('\nInserisci un voto: '))
        if voto_stringa == '':
            break
        voto = float(voto_stringa)
        try:
            if 18 <= voto <= 30:
                lista_voti.append(voto)
            else:
                print('Voto non valido (18 - 30).')
        except ValueError:
            print('Non valido, inserisci un numero.')
            
    if not lista_voti:
        return
    
    
    dati[nome] = lista_voti
    scrivi_registro(database, dati) 

def menu():
    while True:
        print("\nRegistro: ")
        print("1) Leggi elenco alunni e voti (media)")
        print("2) Aggiungi un alunno con i voti")
        print("3) Esci")

        scelta = input("\nScegli un'opzione (1/2/3): ").strip()
        if scelta == '1':
            apri_registro(db)
        elif scelta == '2':
            aggiungi_alunno(db)
        elif scelta == '3':
            print("Ciao!")
            break
        else:
            print("Scelta non valida")

menu()