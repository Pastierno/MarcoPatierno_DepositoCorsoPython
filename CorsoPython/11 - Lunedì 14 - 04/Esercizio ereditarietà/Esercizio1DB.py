import sqlite3

# Funzione per creare la tabella
def crea_tabella(conn):
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Animali (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        eta INTEGER NOT NULL,
        tipo TEXT NOT NULL,
        velocita REAL,
        peso REAL
    )
    ''')
    conn.commit()

# Classe padre
class Animale:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def fai_suono(self):
        print(f"{self.nome} emette un suono.")

    def salva_in_db(self, conn):
        # Metodo base per salvare i dati comuni.
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO Animali (nome, eta, tipo)
            VALUES (?, ?, ?)
        ''', (self.nome, self.eta, self.__class__.__name__))
        conn.commit()

# Classe Capibara
class Capibara(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)


    def fai_suono(self):
        print("'Nome di verso sconosciuto'")

    def nuota(self):
        print(f"{self.nome} sta nuotando.")

    def salva_in_db(self, conn):
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO Animali (nome, eta, tipo)
            VALUES (?, ?, ?)
        ''', (self.nome, self.eta, "Capibara"))
        conn.commit()

# Classe Ermellino (con attributo velocita)
class Ermellino(Animale):
    def __init__(self, nome, eta, velocita):
        super().__init__(nome, eta)
        self.velocita = velocita

    def fai_suono(self):
        print("Neanche di questo si trova il verso?!")

    def caccia(self):
        print(f"{self.nome} caccia con una velocità di {self.velocita} km/h")

    def salva_in_db(self, conn):
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO Animali (nome, eta, tipo, velocita)
            VALUES (?, ?, ?, ?)
        ''', (self.nome, self.eta, "Ermellino", self.velocita))
        conn.commit()

# Classe Rinoceronte
class Rinoceronte(Animale):
    def __init__(self, nome, eta, peso):
        super().__init__(nome, eta)
        self.peso = peso

    def fai_suono(self):
        print("'Tipo grugniti e soffi'")

    def carica(self):
        print(f"{self.nome}, dal peso di {self.peso} tonnellate, carica.")

    def salva_in_db(self, conn):
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO Animali (nome, eta, tipo, peso)
            VALUES (?, ?, ?, ?)
        ''', (self.nome, self.eta, "Rinoceronte", self.peso))
        conn.commit()

# Funzione principale
def main():
    # Collegamento al database (crea il file se non esiste)
    conn = sqlite3.connect('animali.db')
    
    crea_tabella(conn)

    # Esempio da inserire un metodo per inserire tramite input
    Capi = Capibara("Mellino", 4)
    Erme = Ermellino("Elmo", 2, velocita=45)
    Rino = Rinoceronte("Rino", 10, peso=2.5)

    # Salvataggio delle istanze nel database
    Capi.salva_in_db(conn)
    Erme.salva_in_db(conn)
    Rino.salva_in_db(conn)

    # Stampa di tutti i record dalla tabella
    cur = conn.cursor()
    cur.execute("SELECT * FROM Animali")
    record = cur.fetchall()
    print("Record presenti nel database:")
    for r in record:
        print(r)

    conn.close()

main()
