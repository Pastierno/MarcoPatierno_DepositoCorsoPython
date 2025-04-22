import mysql.connector as sq
# Extra, aggiungo tabella con nomi di stati nel mondo per far scegliere all'utente come collegarli alla tabella
# Connessione globale al database
db = None
cursor = None

# Creazione database
def create_database():
    global db, cursor
    db = sq.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS vendite")
    cursor.execute("USE vendite")
    
def create_table():
    global db, cursor
    # Creazione delle tabelle
    cursor.execute("""CREATE TABLE IF NOT EXISTS clienti (
        id_cliente INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        eta INT,
        regione VARCHAR(50)
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS prodotti (
        id_prodotto INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        prezzo FLOAT,
        categoria VARCHAR(50)
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS vendite (
        id_vendita INT AUTO_INCREMENT PRIMARY KEY,
        id_cliente INT,
        id_prodotto INT,
        quantita INT,
        prezzo_totale FLOAT,
        data_vendita DATE,
        FOREIGN KEY (id_cliente) REFERENCES clienti(id_cliente),
        FOREIGN KEY (id_prodotto) REFERENCES prodotti(id_prodotto)
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS stati (
        id_stato INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100)
    )""")
    
    db.commit()

def close_connection():
    global db, cursor
    if cursor:
        cursor.close()
    if db:
        db.close()