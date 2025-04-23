from class_Persona import Person
from class_Prof import Prof
from class_Student import Student
import sqlite3

def menu():
    # Connessione al database, creazione tabelle se non esistono
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, votes TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS professors
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, subject TEXT)''')
    conn.commit()
    
    print("Benvenuto nel sistema di gestione studenti e professori.")
    while True:
        # Stampa il menu
        print("\nMenu:")
        print("1. Aggiungi studente")
        print("2. Aggiungi professore")
        print("3. Visualizza studenti")
        print("4. Visualizza professori")
        print("5. Mostra media voti studente (ID)")
        print("6. Esci")
        user_input = int(input("Scegli un'opzione: "))
        
        
        if user_input == 1: # Aggiungi studente
            nome = input("Inserisci il nome dello studente: ")
            eta = int(input("Inserisci l'età dello studente: "))
            voti = input("Inserisci i voti dello studente (separati da virgola o spazio): ")
            
            cursor.execute("INSERT INTO students (name, age, votes) VALUES (?, ?, ?)", (nome, eta, voti))
            conn.commit()
            print(f"Studente {nome} aggiunto con successo.")
        elif user_input == 2:
            nome = input("Inserisci il nome del professore: ")
            eta = int(input("Inserisci l'età del professore: "))
            materia = input("Inserisci la materia del professore: ")
            
            cursor.execute("INSERT INTO professors (name, age, subject) VALUES (?, ?, ?)", (nome, eta, materia))
            conn.commit()
            print(f"Professore {nome} aggiunto con successo.")
        elif user_input == 3:
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()
            print("\nLista studenti:")
            for student in students:
                print(f"ID: {student[0]}, Nome: {student[1]}, Età: {student[2]}, Voti: {student[3]}")
        elif user_input == 4:
            cursor.execute("SELECT * FROM professors")
            professors = cursor.fetchall()
            print("\nLista professori:")
            for professor in professors:
                print(f"ID: {professor[0]}, Nome: {professor[1]}, Età: {professor[2]}, Materia: {professor[3]}")
        elif user_input == 5:
            stud_id = int(input("Inserisci l'ID dello studente: "))
            cursor.execute("SELECT votes FROM students WHERE id = ?", (stud_id,))
            result = cursor.fetchone()
            name = result[0] if result else None
            age = result[1] if result else None
            student = Student(name, age, [])
            if result:
                student.set_votes(list(map(int, result[2].split(','))))
                print(f"La media dei voti dello studente con ID {stud_id} è: {student.speach()}")
            else:
                print("Studente non trovato.")
        elif user_input == 6:
            print("Uscita dal programma.")
            break
    conn.close()
        
menu()          
    
    