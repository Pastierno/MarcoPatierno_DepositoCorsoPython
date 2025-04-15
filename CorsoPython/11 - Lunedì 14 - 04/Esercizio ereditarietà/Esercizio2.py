import sqlite3
import random
import datetime

# Creazione della connessione al database
conn = sqlite3.connect('squadra.db')
cursor = conn.cursor()

# Definizione delle classi
# Membro_squadra è la classe base
class Membro_squadra():
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def __str__(self):
        return f"{self.nome} ({self.eta})"
    
    def descrivi(self):
        return f"{self.nome} di {self.eta} anni"

# Giocatore, Allenatore e Assistente ereditano da Membro_squadra    
class Giocatore(Membro_squadra):
    def __init__(self, nome, eta, squadra, ruolo, numero_maglia, punteggio): 
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
        self.squadra = squadra
        self.punteggio = punteggio 
        
    def gioca_partita(self):
        print(f"{self.nome} sta giocando una partita!")
    
    # metodo per aggiungere il giocatore al database
    def aggiungi_db(self):
        cursor.execute("INSERT INTO SQUADRA (nome, eta, squadra, ruolo, numero_maglia, punteggio) VALUES (?, ?, ?, ?, ?, ?)",
                       (self.nome, self.eta, self.squadra, self.ruolo, self.numero_maglia, self.punteggio))
        conn.commit()
        
class Allenatore(Membro_squadra):
    def __init__(self, nome, eta, squadra, esperienza):
        super().__init__(nome, eta)
        self.squadra = squadra
        self.esperienza = esperienza # esperienza dell'allenatore
        
    def dirige_allenamento(self):
        print(f"{self.nome} sta allenando la squadra!")
    
    # metodo per aggiungere l'allenatore al database
    def aggiunbi_db(self):
        cursor.execute("INSERT INTO SQUADRA (nome, eta, squadra, ruolo) VALUES (?, ?, ?, ?)",
                       (self.nome, self.eta, self.squadra, "Allenatore"))
        conn.commit()
    
class Assistente(Membro_squadra):
    def __init__(self, nome, eta, squadra, specializzazione):
        super().__init__(nome, eta)
        self.squadra = squadra
        self.specializzazione = specializzazione # specializzazione dell'assistente
        
    def supporta_team(self):
        print(f"{self.nome} sta aiutando nell'allenamento!")
        
    def aggiungi_db(self):
        cursor.execute("INSERT INTO SQUADRA (nome, eta, squadra, ruolo) VALUES (?, ?, ?, ?)",
                       (self.nome, self.eta, self.squadra, "Assistente"))
        conn.commit()
        
# Creazione della tabella nel database
def crea_tabella():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SQUADRA (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        eta INTEGER NOT NULL,
        squadra TEXT NOT NULL,
        ruolo TEXT NOT NULL,
        numero_maglia INTEGER,
        punteggio INTEGER
    )''')
    conn.commit()

# Funzione per comporre la squadra    
def componi_squadra():
    crea_tabella()
    
    while True:
        print("Benvenuto nel programma di gestione della squadra!")
        user_input = int(input("Vuoi aggiungere un Giocatore (1) \n"
                               "Allenatore (2)\n"
                               "Assistente (3) \n"
                               "Uscire (0)? "))
        if user_input == 0:
            print("Uscita dal programma.")
            break
        # Aggiunta di un Giocatore
        elif user_input == 1:
            nome = input("Inserisci il nome del giocatore: ")
            eta = int(input("Inserisci l'età del giocatore: "))
            squadra = input("Inserisci la squadra del giocatore: ")
            ruolo = input("Inserisci il ruolo del giocatore: ")
            numero_maglia = int(input("Inserisci il numero di maglia del giocatore: "))
            punteggio = int(input("Inserisci il punteggio del giocatore: "))
            
            giocatore = Giocatore(nome, eta, squadra, ruolo, numero_maglia, punteggio)
            giocatore.aggiungi_db()
            print(f"{giocatore.nome} è stato aggiunto alla squadra.")
        
        # Aggiunta di un Allenatore    
        elif user_input == 2:
            nome = input("Inserisci il nome dell'allenatore: ")
            eta = int(input("Inserisci l'età dell'allenatore: "))
            squadra = input("Inserisci la squadra dell'allenatore: ")
            esperienza = int(input("Inserisci gli anni di esperienza dell'allenatore: "))
            
            allenatore = Allenatore(nome, eta, squadra, esperienza)
            allenatore.aggiunbi_db()
            print(f"{allenatore.nome} è stato aggiunto alla squadra.")
            
        elif user_input == 3:
            nome = input("Inserisci il nome dell'assistente: ")
            eta = int(input("Inserisci l'età dell'assistente: "))
            squadra = input("Inserisci la squadra dell'assistente: ")
            specializzazione = input("Inserisci la specializzazione dell'assistente: ")
            
            assistente = Assistente(nome, eta, squadra, specializzazione)
            assistente.aggiungi_db()
            print(f"{assistente.nome} è stato aggiunto alla squadra.")
            
    conn.close()

# Funzione per creare la tabella delle partite   
def crea_tabella_partite():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PARTITE (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        squadra1 TEXT NOT NULL,
        squadra2 TEXT NOT NULL,
        gol1 INTEGER NOT NULL,
        gol2 INTEGER NOT NULL,
        data_partita TEXT NOT NULL
    )''')
    conn.commit()

# Funzione per gestire la partita   
def partita():
    crea_tabella_partite()
    
    # Creazione della squadra
    squadra1 = input("Inserisci il nome della prima squadra: ")
    squadra2 = input("Inserisci il nome della seconda squadra: ")
    
    # Recupero dei giocatori e punteggi dal database
    cursor.execute("SELECT * FROM SQUADRA WHERE squadra = ?", (squadra1,))
    squadra1 = cursor.fetchall()
    
    cursor.execute("SELECT * FROM SQUADRA WHERE squadra = ?", (squadra2,))
    squadra2 = cursor.fetchall()
    
    # Filtraggio dei giocatori
    # Escludendo allenatori e assistenti
    giocatori1 = [giocatore for giocatore in squadra1 if squadra1[4] not in ("Allenatore", "Assistente")]
    giocatori2 = [giocatore for giocatore in squadra2 if squadra2[4] not in ("Allenatore", "Assistente")]
    
    if len(giocatori1) < 5 or len(giocatori2) < 5:
        print("Errore: ogni squadra deve avere esattamente 5 giocatori.")
        return
    # Calcolo del punteggio totale
    if squadra1 and squadra2:
        punteggio_totale1 = sum([giocatore[6] for giocatore in squadra1 if giocatore[6] is not None]) 
        punteggio_totale2 =  sum([giocatore[6] for giocatore in squadra2 if giocatore[6] is not None])
    
    print(f"Punteggio totale di della prima squadra: {punteggio_totale1}")
    print(f"Punteggio totale di della seconda squadra: {punteggio_totale2}")
    
    # Simulazione della partita
    tentativi_attacco = 15
    gol1 = 0
    gol2 = 0
    
    
    for i in range(tentativi_attacco):
        if punteggio_totale1 + punteggio_totale2 > 0: # controllo per evitare divisione per zero
            vantaggio_team1 = punteggio_totale1 / (punteggio_totale1 + punteggio_totale2)
        else:
            vantaggio_team1 = 0.5
            
        if random.random() < vantaggio_team1:
            gol1 += 1
        else:
            gol2 += 1
            
        data_partita = datetime.datetime.now().isoformat()
        cursor.execute("INSERT INTO PARTITE (squadra1, squadra2, gol1, gol2, data_partita) VALUES (?, ?, ?, ?, ?)",
                       (squadra1[0][3], squadra2[0][3], gol1, gol2, data_partita))
        conn.commit()
        
        print(f"Partita tra {squadra1[0][3]} e {squadra2[0][3]}: {gol1} - {gol2}")
    conn.close()
    
    
def menu_principale():
    while True:
        print("\nBenvenuto nel FantaPy")
        print("1. Gestisci Squadra (Aggiungi membri)")
        print("2. Simula Partita")
        print("3. Esci")
        try:
            scelta = int(input("Inserisci la tua scelta: "))
        except ValueError:
            print("Inserisci un valore numerico valido.")
            continue
        
        if scelta == 1:
            componi_squadra()
        elif scelta == 2:
            partita()
        elif scelta == 3:
            print("Uscita dal programma. Arrivederci!")
            break
        else:
            print("Opzione non valida. Riprova.")
        
        
menu_principale()
    
    