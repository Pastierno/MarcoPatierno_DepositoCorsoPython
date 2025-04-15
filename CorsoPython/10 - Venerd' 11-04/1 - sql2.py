import mysql.connector


myDB = mysql.connector.connect( # Salvare in una variabile la connessione al DB
  host="localhost",
  user="root",
  password="",
  database = 'corso_python'
  #port=9999 in caso di porta diversa dal default
)

#print(myDB)

# Chiamare cursore per eseguire query

my_cursor = myDB.cursor()
#########################################
# query = 'CREATE DATABASE corso_python'
# query = 'SHOW DATABASES'
# my_cursor.execute(query) # Esegue query

# for db in my_cursor:
#   print(db)
########################################

# query = 'CREATE TABLE utenti(ID int AUTO_INCREMENT PRIMARY KEY, NOME VARCHAR(50), COGNOME VARCHAR(50))'
# def insertRow():
#   query = 'INSERT INTO utenti(NOME, COGNOME) VALUES(%s, %s)' # segnaposti per sicurezza
#   value = ('Marco', 'Patierno')
#   my_cursor.execute(query, value)
#   myDB.commit()
#   print('riga inserita: ', my_cursor.rowcount)

def insertRows():
  query = 'INSERT INTO utenti(NOME, COGNOME) VALUES(%s, %s)' # segnaposti per sicurezza
  values = [('Mario', 'Rossi'), ('Anna', 'Neri')]
  my_cursor.executemany(query, values)
  myDB.commit()
  print('righe inserite: ', my_cursor.rowcount)
  
#insertRows()

def select_rows():
  query = 'SELECT * FROM utenti'
  my_cursor.execute(query)
  res = my_cursor.fetchone() #fetchall() per +
  # for row in res:
  print(res)
    
select_rows()

myDB.close()