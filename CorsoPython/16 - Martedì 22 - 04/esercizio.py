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
    stati = ["Italia", "Francia", "Germania", "Spagna", "Regno Unito", "Stati Uniti", "Canada", "Australia", "Giappone", "Cina"]
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
        print("5. Gestione stati")
        print("6. Esci")
        
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
                # Gestione stati
                print("\nGestione Stati:")
                print("1. Popola tabella stati")
                print("2. Aggiungi colonna stato a clienti")
                print("3. Aggiungi colonna stato a prodotti")
                print("4. Aggiungi colonna stato a vendite")
                
                stato_choice = int(input("\nScegli un'opzione: "))
                
                if stato_choice == 1:
                    # Popola tabella stati
                    try:
                        # Verifico se la tabella è già popolata
                        db.cursor.execute("SELECT COUNT(*) FROM stati")
                        count = db.cursor.fetchone()[0]
                        
                        if count > 0:
                            print(f"La tabella stati è già popolata con {count} record.")
                            continue
                        
                        # Inserisco gli stati
                        for stato in stati:
                            query = "INSERT INTO stati (nome) VALUES (%s)"
                            db.cursor.execute(query, (stato,))
                        db.db.commit()
                        print(f"{len(stati)} stati inseriti nel database")
                    except Exception as e:
                        print(f"Errore nel popolare la tabella stati: {e}")
                
                elif stato_choice == 2:
                    # Aggiungi colonna stato a clienti
                    try:
                        # Verifico se la colonna esiste già
                        db.cursor.execute("SHOW COLUMNS FROM clienti LIKE 'id_stato'")
                        if db.cursor.fetchone():
                            print("La colonna id_stato esiste già nella tabella clienti.")
                        else:
                            # Aggiungo la colonna
                            db.cursor.execute("ALTER TABLE clienti ADD COLUMN id_stato INT, ADD FOREIGN KEY (id_stato) REFERENCES stati(id_stato)")
                            db.db.commit()
                            print("Colonna id_stato aggiunta alla tabella clienti.")
                        
                        # Sottomenu per criteri di assegnazione
                        print("\nScegli criterio di assegnazione stati ai clienti:")
                        print("1. Assegna casualmente")
                        print("2. Assegna in base alla regione")
                        print("3. Assegna in base all'età")
                        
                        criterio = int(input("\nScegli un criterio: "))
                        
                        # Ottengo gli ID degli stati
                        db.cursor.execute("SELECT id_stato FROM stati")
                        stati_ids = [row[0] for row in db.cursor.fetchall()]
                        
                        if not stati_ids:
                            print("Errore: devi prima popolare la tabella stati.")
                            continue
                        
                        if criterio == 1:
                            # Assegnazione casuale
                            db.cursor.execute("SELECT id_cliente FROM clienti")
                            clienti_ids = [row[0] for row in db.cursor.fetchall()]
                            
                            for cliente_id in clienti_ids:
                                stato_id = random.choice(stati_ids)
                                db.cursor.execute("UPDATE clienti SET id_stato = %s WHERE id_cliente = %s", 
                                                 (stato_id, cliente_id))
                            
                            db.db.commit()
                            print("Stati assegnati casualmente ai clienti.")
                            
                        elif criterio == 2:
                            # Assegnazione in base alla regione
                            # Mappo le regioni del nord ai primi stati, quelle del centro ai secondi, ecc.
                            nord = ["Lombardia", "Veneto", "Piemonte"]
                            centro = ["Toscana", "Lazio"]
                            sud = ["Campania", "Sicilia"]
                            
                            regioni_mapping = {}
                            
                            # Divido gli stati_ids in tre parti uguali (approssimative)
                            n = len(stati_ids)
                            stati_nord = stati_ids[:n//3]
                            stati_centro = stati_ids[n//3:2*n//3]
                            stati_sud = stati_ids[2*n//3:]
                            
                            for regione in nord:
                                regioni_mapping[regione] = stati_nord
                            for regione in centro:
                                regioni_mapping[regione] = stati_centro
                            for regione in sud:
                                regioni_mapping[regione] = stati_sud
                            
                            # Aggiorno i clienti
                            db.cursor.execute("SELECT id_cliente, regione FROM clienti")
                            clienti_data = db.cursor.fetchall()
                            
                            for cliente_id, regione in clienti_data:
                                if regione in regioni_mapping:
                                    stato_id = random.choice(regioni_mapping[regione])
                                else:
                                    stato_id = random.choice(stati_ids)
                                
                                db.cursor.execute("UPDATE clienti SET id_stato = %s WHERE id_cliente = %s", 
                                                 (stato_id, cliente_id))
                            
                            db.db.commit()
                            print("Stati assegnati in base alla regione.")
                            
                        elif criterio == 3:
                            # Assegnazione in base all'età
                            db.cursor.execute("SELECT id_cliente, eta FROM clienti")
                            clienti_data = db.cursor.fetchall()
                            
                            # Divido gli stati per fasce d'età
                            n = len(stati_ids)
                            stati_giovani = stati_ids[:n//3]  # 18-35
                            stati_adulti = stati_ids[n//3:2*n//3]  # 36-60
                            stati_anziani = stati_ids[2*n//3:]  # 61+
                            
                            for cliente_id, eta in clienti_data:
                                if eta < 36:
                                    stato_id = random.choice(stati_giovani)
                                elif eta < 61:
                                    stato_id = random.choice(stati_adulti)
                                else:
                                    stato_id = random.choice(stati_anziani)
                                
                                db.cursor.execute("UPDATE clienti SET id_stato = %s WHERE id_cliente = %s", 
                                                 (stato_id, cliente_id))
                            
                            db.db.commit()
                            print("Stati assegnati in base all'età.")
                        
                        else:
                            print("Criterio non valido.")
                            
                    except Exception as e:
                        print(f"Errore nell'aggiunta della colonna stato alla tabella clienti: {e}")
                
                elif stato_choice == 3:
                    # Aggiungi colonna stato a prodotti
                    try:
                        # Verifico se la colonna esiste già
                        db.cursor.execute("SHOW COLUMNS FROM prodotti LIKE 'id_stato'")
                        if db.cursor.fetchone():
                            print("La colonna id_stato esiste già nella tabella prodotti.")
                        else:
                            # Aggiungo la colonna
                            db.cursor.execute("ALTER TABLE prodotti ADD COLUMN id_stato INT, ADD FOREIGN KEY (id_stato) REFERENCES stati(id_stato)")
                            db.db.commit()
                            print("Colonna id_stato aggiunta alla tabella prodotti.")
                        
                        # Sottomenu per criteri di assegnazione
                        print("\nScegli criterio di assegnazione stati ai prodotti:")
                        print("1. Assegna casualmente")
                        print("2. Assegna in base alla categoria")
                        print("3. Assegna in base al prezzo")
                        
                        criterio = int(input("\nScegli un criterio: "))
                        
                        # Ottengo gli ID degli stati
                        db.cursor.execute("SELECT id_stato FROM stati")
                        stati_ids = [row[0] for row in db.cursor.fetchall()]
                        
                        if not stati_ids:
                            print("Errore: devi prima popolare la tabella stati.")
                            continue
                        
                        if criterio == 1:
                            # Assegnazione casuale
                            db.cursor.execute("SELECT id_prodotto FROM prodotti")
                            prodotti_ids = [row[0] for row in db.cursor.fetchall()]
                            
                            for prodotto_id in prodotti_ids:
                                stato_id = random.choice(stati_ids)
                                db.cursor.execute("UPDATE prodotti SET id_stato = %s WHERE id_prodotto = %s", 
                                                 (stato_id, prodotto_id))
                            
                            db.db.commit()
                            print("Stati assegnati casualmente ai prodotti.")
                            
                        elif criterio == 2:
                            # Assegnazione in base alla categoria
                            # Mappo le categorie agli stati
                            db.cursor.execute("SELECT DISTINCT categoria FROM prodotti")
                            categorie_db = [row[0] for row in db.cursor.fetchall()]
                            
                            # Divido gli stati equamente tra le categorie
                            n_categorie = len(categorie_db)
                            n_stati = len(stati_ids)
                            stati_per_categoria = {}
                            
                            for i, categoria in enumerate(categorie_db):
                                start = (i * n_stati) // n_categorie
                                end = ((i + 1) * n_stati) // n_categorie
                                stati_per_categoria[categoria] = stati_ids[start:end] or stati_ids  # Fallback
                            
                            # Aggiorno i prodotti
                            db.cursor.execute("SELECT id_prodotto, categoria FROM prodotti")
                            prodotti_data = db.cursor.fetchall()
                            
                            for prodotto_id, categoria in prodotti_data:
                                if categoria in stati_per_categoria and stati_per_categoria[categoria]:
                                    stato_id = random.choice(stati_per_categoria[categoria])
                                else:
                                    stato_id = random.choice(stati_ids)
                                
                                db.cursor.execute("UPDATE prodotti SET id_stato = %s WHERE id_prodotto = %s", 
                                                 (stato_id, prodotto_id))
                            
                            db.db.commit()
                            print("Stati assegnati in base alla categoria.")
                            
                        elif criterio == 3:
                            # Assegnazione in base al prezzo
                            db.cursor.execute("SELECT id_prodotto, prezzo FROM prodotti")
                            prodotti_data = db.cursor.fetchall()
                            
                            # Trovo il min e max dei prezzi
                            db.cursor.execute("SELECT MIN(prezzo), MAX(prezzo) FROM prodotti")
                            min_prezzo, max_prezzo = db.cursor.fetchone()
                            
                            # Divido il range di prezzi in parti uguali come il numero di stati
                            n = len(stati_ids)
                            
                            for prodotto_id, prezzo in prodotti_data:
                                # Formula per assegnare uno stato in base al prezzo
                                # Normalizza il prezzo in un valore tra 0 e 1
                                if max_prezzo == min_prezzo:  # Evita divisione per zero
                                    norm_prezzo = 0
                                else:
                                    norm_prezzo = (prezzo - min_prezzo) / (max_prezzo - min_prezzo)
                                
                                # Calcola l'indice dello stato
                                stato_idx = min(int(norm_prezzo * n), n - 1)
                                stato_id = stati_ids[stato_idx]
                                
                                db.cursor.execute("UPDATE prodotti SET id_stato = %s WHERE id_prodotto = %s", 
                                                 (stato_id, prodotto_id))
                            
                            db.db.commit()
                            print("Stati assegnati in base al prezzo.")
                        
                        else:
                            print("Criterio non valido.")
                            
                    except Exception as e:
                        print(f"Errore nell'aggiunta della colonna stato alla tabella prodotti: {e}")
                
                elif stato_choice == 4:
                    # Aggiungi colonna stato a vendite
                    try:
                        # Verifico se la colonna esiste già
                        db.cursor.execute("SHOW COLUMNS FROM vendite LIKE 'id_stato'")
                        if db.cursor.fetchone():
                            print("La colonna id_stato esiste già nella tabella vendite.")
                        else:
                            # Aggiungo la colonna
                            db.cursor.execute("ALTER TABLE vendite ADD COLUMN id_stato INT, ADD FOREIGN KEY (id_stato) REFERENCES stati(id_stato)")
                            db.db.commit()
                            print("Colonna id_stato aggiunta alla tabella vendite.")
                        
                        # Sottomenu per criteri di assegnazione
                        print("\nScegli criterio di assegnazione stati alle vendite:")
                        print("1. Assegna casualmente")
                        print("2. Assegna in base alla data")
                        print("3. Assegna in base al prezzo totale")
                        print("4. Assegna in base allo stato del cliente")
                        
                        criterio = int(input("\nScegli un criterio: "))
                        
                        # Ottengo gli ID degli stati
                        db.cursor.execute("SELECT id_stato FROM stati")
                        stati_ids = [row[0] for row in db.cursor.fetchall()]
                        
                        if not stati_ids:
                            print("Errore: devi prima popolare la tabella stati.")
                            continue
                        
                        if criterio == 1:
                            # Assegnazione casuale
                            db.cursor.execute("SELECT id_vendita FROM vendite")
                            vendite_ids = [row[0] for row in db.cursor.fetchall()]
                            
                            for vendita_id in vendite_ids:
                                stato_id = random.choice(stati_ids)
                                db.cursor.execute("UPDATE vendite SET id_stato = %s WHERE id_vendita = %s", 
                                                 (stato_id, vendita_id))
                            
                            db.db.commit()
                            print("Stati assegnati casualmente alle vendite.")
                            
                        elif criterio == 2:
                            # Assegnazione in base alla data
                            db.cursor.execute("SELECT id_vendita, data_vendita FROM vendite")
                            vendite_data = db.cursor.fetchall()
                            
                            # Trovo la data minima e massima
                            db.cursor.execute("SELECT MIN(data_vendita), MAX(data_vendita) FROM vendite")
                            min_data, max_data = db.cursor.fetchone()
                            
                            min_date = datetime.datetime.strptime(min_data.strftime('%Y-%m-%d'), '%Y-%m-%d')
                            max_date = datetime.datetime.strptime(max_data.strftime('%Y-%m-%d'), '%Y-%m-%d')
                            
                            # Calcolo il range in giorni
                            total_days = (max_date - min_date).days
                            if total_days == 0:
                                total_days = 1  # Evita divisione per zero
                            
                            n = len(stati_ids)
                            
                            for vendita_id, data_vendita in vendite_data:
                                current_date = datetime.datetime.strptime(data_vendita.strftime('%Y-%m-%d'), '%Y-%m-%d')
                                days_from_min = (current_date - min_date).days
                                
                                # Calcola l'indice dello stato
                                stato_idx = min(int((days_from_min / total_days) * n), n - 1)
                                stato_id = stati_ids[stato_idx]
                                
                                db.cursor.execute("UPDATE vendite SET id_stato = %s WHERE id_vendita = %s", 
                                                 (stato_id, vendita_id))
                            
                            db.db.commit()
                            print("Stati assegnati in base alla data di vendita.")
                            
                        elif criterio == 3:
                            # Assegnazione in base al prezzo totale
                            db.cursor.execute("SELECT id_vendita, prezzo_totale FROM vendite")
                            vendite_data = db.cursor.fetchall()
                            
                            # Trovo il min e max dei prezzi
                            db.cursor.execute("SELECT MIN(prezzo_totale), MAX(prezzo_totale) FROM vendite")
                            min_prezzo, max_prezzo = db.cursor.fetchone()
                            
                            # Divido il range di prezzi in parti uguali come il numero di stati
                            n = len(stati_ids)
                            
                            for vendita_id, prezzo in vendite_data:
                                # Formula per assegnare uno stato in base al prezzo
                                if max_prezzo == min_prezzo:  # Evita divisione per zero
                                    norm_prezzo = 0
                                else:
                                    norm_prezzo = (prezzo - min_prezzo) / (max_prezzo - min_prezzo)
                                
                                # Calcola l'indice dello stato
                                stato_idx = min(int(norm_prezzo * n), n - 1)
                                stato_id = stati_ids[stato_idx]
                                
                                db.cursor.execute("UPDATE vendite SET id_stato = %s WHERE id_vendita = %s", 
                                                 (stato_id, vendita_id))
                            
                            db.db.commit()
                            print("Stati assegnati in base al prezzo totale.")
                            
                        elif criterio == 4:
                            # Assegnazione in base allo stato del cliente
                            # Verifico se i clienti hanno stati assegnati
                            db.cursor.execute("SELECT COUNT(*) FROM clienti WHERE id_stato IS NOT NULL")
                            count = db.cursor.fetchone()[0]
                            
                            if count == 0:
                                print("Errore: i clienti non hanno ancora stati assegnati.")
                                continue
                            
                            # Join tra vendite e clienti per ottenere lo stato del cliente
                            db.cursor.execute("""
                                UPDATE vendite v
                                JOIN clienti c ON v.id_cliente = c.id_cliente
                                SET v.id_stato = c.id_stato
                                WHERE c.id_stato IS NOT NULL
                            """)
                            
                            db.db.commit()
                            print("Stati assegnati in base allo stato del cliente.")
                        
                        else:
                            print("Criterio non valido.")
                            
                    except Exception as e:
                        print(f"Errore nell'aggiunta della colonna stato alla tabella vendite: {e}")
                
                else:
                    print("Opzione non valida.")
            
            elif choice == 6:
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



