from class_ba import BankAccount
import sqlite3

def menu():
    conn = sqlite3.connect('bank.db') # Connessione al database SQLite
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS accounts
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    owner TEXT NOT NULL,
                    balance REAL)''') # Creazione della tabella accounts se non esiste
    conn.commit() # Salvataggio delle modifiche nel database
    
    print("Benvenuto nella tua Bank App")
    while True:
        user_input = input("Vuoi creare un nuovo account? (s/n, spazio per uscire): ").lower()
        if user_input == "s":
            nome = input("Inserisci il tuo nome: ") # Nome dell'utente
            saldo = 0 # Saldo iniziale
            account = BankAccount(nome, saldo) # Creazione dell'oggetto BankAccount
            cursor.execute("INSERT INTO accounts (owner, balance) VALUES (?, ?)", (nome, saldo)) # Inserimento nel database
            conn.commit() # Salvataggio delle modifiche nel database
            print(f"Account creato per {nome} con saldo iniziale di {saldo}")
        elif user_input == "n":
            nome = input("Inserisci il tuo nome: ")
            cursor.execute("SELECT * FROM accounts WHERE owner=?", (nome,))
            result = cursor.fetchone() # Recupero dell'account dal database
            if nome in result: # Controlla se l'account esiste
                print(f"Benvenuto {nome}, il tuo saldo attuale è {account.get_balance()}")
                while True:
                    action = input("Vuoi depositare (d), prelevare (w) o uscire (q)? ").lower()
                    if action == "d":
                        amount = float(input("Quanto vuoi depositare? "))
                        account.deposit(amount)
                        cursor.execute("UPDATE accounts SET balance=? WHERE owner=?", (account.get_balance(), nome)) # Aggiornamento del saldo nel database
                        conn.commit() # Salvataggio delle modifiche nel database
                    elif action == "w":
                        amount = float(input("Quanto vuoi prelevare? "))
                        account.withdraw(amount)
                        cursor.execute("UPDATE accounts SET balance=? WHERE owner=?", (account.get_balance(), nome))
                        conn.commit() # Salvataggio delle modifiche nel database
                    elif action == "q":
                        break
                    else:
                        print("Azione non valida. Riprova.")
            else:
                print("Account non trovato.")
        elif user_input == "":
            break
            
    
menu()