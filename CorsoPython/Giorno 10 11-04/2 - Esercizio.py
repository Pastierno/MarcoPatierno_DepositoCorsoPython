
def aggiungi_studente(my_cursor, table):  
    nome = input('\nInserisci il nome dell\'alunno: ').strip()
    cognome = input('\nInserisci il cognome dell\'alunno: ').strip()
    
    query = f'INSERT INTO {table} (NOME, COGNOME) VALUES(%s,%s)'
    values = (nome.upper(), cognome.upper())
    my_cursor.execute(query, values)
    db.commit()
    print(f"{nome.upper()} {cognome.upper()} aggiunto.")
    
def elimina_studente(my_cursor, table):
    while True:
        nome = input('\nInserisci il nome dell\'alunno: ').strip()
        cognome = input('\nInserisci il cognome dell\'alunno: ').strip()
        values = (nome.upper(), cognome.upper())
        query = f'SELECT * FROM {table} WHERE NOME = %s AND COGNOME = %s'
        my_cursor.execute(query, values)
        res = my_cursor.fetchone(query, values)
        print(res)
    
        conferma = int(input('Vuoi eliminare questo alunno? (1/Sì, 2/No)'))
        if conferma == 1:
            query = f'DELETE FROM {table} WHERE NOME = %s AND COGNOME = %s'
            res = my_cursor.execute(query, values)
            db.commit()
            print(f'{nome}, {cognome} eliminato.')
            break
        elif conferma == 2:
            print('Ripeto operazione')
            continue
        else:
            print('Errore, opzione non valida')
            continue

def crea_tabella_voti():
    query = """ CREATE TABLE IF NOT EXISTS VOTI (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        MATRICOLA INT,
        ESAME VARCHAR(50) NOT NULL,
        VOTO INT NOT NULL,
        FOREIGN KEY (MATRICOLA) REFERENCES STUDENTI(MATRICOLA) DELETE CASCADE
    )"""
    mycursor.execute(query)
    print("Tabella VOTI pronta.")
           
def aggiungi_voto(my_cursor, table):
    esame = input('Inserisci l\'esame: ').strip()
    matricola = int(input('\nInserisci la matricola dell\'alunno: '))
    values = (esame.upper(), matricola)
    while True:
        voto = int(input('Inserisci il voto (spazio per continuare): '))
        if voto == '':
            break
        if voto >= 18 and voto <= 30:
            query = f'INSERT INTO {table} (VOTO) WHERE MATRICOLA = %s'
            my_cursor.execute(query, values)
            db.commit()
            print(f'{voto} inserito alla matricola {matricola}')
            continue
        else:
            print('Voto non valido, riprova')
            continue
            
def media(table, my_cursor):
    matricola = int(input('\nInserisci la matricola dell\'alunno: '))
    query = f'''SELECT MATRICOLA, AVG(VOTO) 
            FROM {table} 
            WHERE MATRICOLA = %s GROUP BY MATRICOLA'''
    value = matricola
    my_cursor.execute(query, value)
    res = my_cursor.fetchone()
    print(f'{matricola} ha la media del {res}')
