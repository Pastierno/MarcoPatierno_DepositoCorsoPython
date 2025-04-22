import numpy as np
import mysql.connector as sq
import db
import datetime
import random

# Sistema di gestione vendite e analisi dati clienti 

def menu():
    # Creazione del database e delle tabelle
    db.create_database()
    db.create_table()
    
    # Esempi di dati da inserire
    nomi_clienti = ["Mario", "Giulia", "Paolo", "Anna", "Giovanni", "Francesca", "Marco", "Laura"]
    regioni = ["Lombardia", "Lazio", "Campania", "Sicilia", "Toscana", "Veneto", "Piemonte"]
    prodotti = ["Smartphone", "Laptop", "Tablet", "Monitor", "Tastiera", "Mouse", "Cuffie", "Stampante"]
    categorie = ["Elettronica", "Informatica", "Accessori", "Audio"]
    
    # Dizionario per mappare le tabelle alle loro colonne numeriche
    tabelle_colonne = {
        "clienti": ["eta"],
        "prodotti": ["prezzo"],
        "vendite": ["quantita", "prezzo_totale"]
    }
    
    while True:
        print("\nGestionale Vendite.")
        print("1. Genera clienti random")
        print("2. Genera prodotti sequenziali")
        print("3. Genera vendite casuali")
        print("4. Calcoli statistici")
        print("5. Esci")
        
        try:
            choice = int(input("\nScegli un'opzione: "))
            
            if choice == 1: # Genera clienti random con random di numpy
                num = int(input("Inserisci il numero di clienti da generare: "))
                for i in range(num):
                    nome = random.choice(nomi_clienti)
                    eta = np.random.randint(18, 80)
                    regione = random.choice(regioni)
                    query = "INSERT INTO clienti (nome, eta, regione) VALUES (%s, %s, %s)"
                    db.cursor.execute(query, (nome, int(eta), regione))
                db.db.commit()
                print(f"{num} clienti inseriti nel database")
            
            elif choice == 2:
                num = int(input("Inserisci il numero di prodotti da generare: "))
                start_price = float(input("Inserisci il prezzo di partenza: "))
                stop_price = float(input("Inserisci il prezzo massimo: "))
                
                # Genera prezzi uniformemente distribuiti con linspace di numpy
                prezzi = np.linspace(start_price, stop_price, num)
                
                # Dizionario per tenere traccia del conteggio per ogni tipo di prodotto
                contatori_prodotti = {prodotto: 0 for prodotto in prodotti}
                
                # ciclo for per generare i prodotti
                for i in range(num):
                    # Seleziona un tipo di prodotto casuale
                    tipo_prodotto = random.choice(prodotti)
                    # Incrementa il contatore specifico per questo tipo di prodotto
                    contatori_prodotti[tipo_prodotto] += 1
                    # Crea il nome del prodotto con il contatore specifico
                    nome = f"{tipo_prodotto} {contatori_prodotti[tipo_prodotto]}"
                    
                    prezzo = round(float(prezzi[i]), 2)
                    categoria = random.choice(categorie)
                    query = "INSERT INTO prodotti (nome, prezzo, categoria) VALUES (%s, %s, %s)"
                    db.cursor.execute(query, (nome, prezzo, categoria))
                db.db.commit()
                print(f"{num} prodotti inseriti nel database")
            
            elif choice == 3:
                num = int(input("Inserisci il numero di vendite da generare: "))
                
                # Ottenere gli ID dei clienti e prodotti esistenti
                db.cursor.execute("SELECT id_cliente FROM clienti")
                clienti_ids = [row[0] for row in db.cursor.fetchall()]
                
                db.cursor.execute("SELECT id_prodotto, prezzo FROM prodotti")
                prodotti_info = [(row[0], row[1]) for row in db.cursor.fetchall()]
                
                if not clienti_ids or not prodotti_info:
                    print("Errore: Inserisci prima clienti e prodotti")
                    continue
                
                # Generare date di vendita distribuite negli ultimi 365 giorni
                date_base = datetime.datetime.now() - datetime.timedelta(days=365)
                date_range = np.arange(0, 365, 365/num).astype(int)
                
                # ciclo for per generare le vendite
                # Utilizzo di random.choice per selezionare casualmente un cliente e un prodotto
                for i in range(num):
                    id_cliente = random.choice(clienti_ids)
                    id_prodotto, prezzo_base = random.choice(prodotti_info)
                    quantita = np.random.randint(1, 10)
                    prezzo_totale = round(prezzo_base * quantita, 2)
                    data = (date_base + datetime.timedelta(days=int(date_range[i]))).strftime('%Y-%m-%d')
                    
                    query = """INSERT INTO vendite 
                               (id_cliente, id_prodotto, quantita, prezzo_totale, data_vendita) 
                               VALUES (%s, %s, %s, %s, %s)"""
                    db.cursor.execute(query, (id_cliente, id_prodotto, quantita, prezzo_totale, data))
                db.db.commit()
                print(f"{num} vendite inserite nel database")
                
            elif choice == 4:
                # Sottomenu per calcoli statistici
                print("\nCalcoli Statistici:")
                print("1. Media")
                print("2. Varianza")
                print("3. Deviazione standard")
                print("4. Minimo")
                print("5. Massimo")
                
                stat_choice = int(input("\nScegli il tipo di calcolo: "))
                if stat_choice not in range(1, 6): # controllo per opzioni valide
                    print("Opzione non valida.")
                    continue
                
                # Scelta della tabella
                print("\nScegli la tabella:")
                for i, tabella in enumerate(tabelle_colonne.keys(), 1):
                    print(f"{i}. {tabella}")
                
                tabella_choice = int(input("\nScegli la tabella: "))
                if tabella_choice not in range(1, len(tabelle_colonne) + 1):
                    print("Opzione non valida.")
                    continue
                
                tabella = list(tabelle_colonne.keys())[tabella_choice - 1]
                
                # Scelta della colonna
                print(f"\nScegli la colonna dalla tabella {tabella}:")
                colonne = tabelle_colonne[tabella]
                for i, colonna in enumerate(colonne, 1):
                    print(f"{i}. {colonna}")
                
                colonna_choice = int(input("\nScegli la colonna: "))
                if colonna_choice not in range(1, len(colonne) + 1):
                    print("Opzione non valida.")
                    continue
                
                colonna = colonne[colonna_choice - 1]
                
                # Esecuzione del calcolo statistico
                funzioni = {
                    1: "AVG",       # Media
                    2: "VARIANCE",  # Varianza
                    3: "STDDEV",    # Deviazione standard
                    4: "MIN",       # Minimo
                    5: "MAX"        # Massimo
                }
                
                nome_operazione = {
                    1: "Media",
                    2: "Varianza",
                    3: "Deviazione standard", 
                    4: "Minimo",
                    5: "Massimo"
                }
                
                # Formattazione per output monetario
                format_monetario = colonna in ["prezzo", "prezzo_totale"]
                
                query = f"SELECT {funzioni[stat_choice]}({colonna}) FROM {tabella}"
                db.cursor.execute(query)
                result = db.cursor.fetchone()
                
                if result[0] is None:
                    print(f"Nessun dato disponibile per calcolare {nome_operazione[stat_choice]}.")
                else:
                    if format_monetario:
                        print(f"{nome_operazione[stat_choice]} di {colonna} in {tabella}: €{result[0]:.2f}")
                    else:
                        print(f"{nome_operazione[stat_choice]} di {colonna} in {tabella}: {result[0]:.2f}")
            
            elif choice == 5:
                print("Chiusura del programma...")
                db.close_connection()
                break
                
            else:
                print("Opzione non valida. Riprova.")
                
        except ValueError:
            print("Inserisci un numero valido")
        except Exception as e:
            print(f"Errore: {e}")

if __name__ == "__main__":
    menu()



