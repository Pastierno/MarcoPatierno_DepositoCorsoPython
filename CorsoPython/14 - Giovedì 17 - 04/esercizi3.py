import numpy as np
import sqlite3

# Crea una matrice 2d 6x6 contenente interi casuali tra 1 e 100
arr2d = np.random.randint(1, 101, (6, 6))
print("Matrice originale:\n", arr2d)

# estgrai la sottomatrice 4x4 centrale
matrice_centrale = arr2d[1:5, 1:5]
print("Sottomatrice centrale:\n", matrice_centrale)

# inverti le righe della matrice estratta
matrice_invertita = matrice_centrale[::-1]
print("Matrice invertita:\n", matrice_invertita)

# estrai la diagonale principaòe invertita e crea un array 1d contenente questi elementi
diagon= np.diag(matrice_invertita)
print("Diagonale principale invertita:\n", diagon)

# sostituisci gli elementi della matrice invertita che sono multipli di 3 con il valore -1
matrice_invertita[matrice_invertita % 3 == 0] = -1

print("Matrice invertita modificata:\n", matrice_invertita)
    



# collegamento riempimento dell'array a una tabella reale
conn = sqlite3.connect('matrice.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS matrice (
    r INTEGER,
    c INTEGER,
    val INTEGER,
    PRIMARY KEY (r, c)
    
)''')

conn.commit()

cursor.execute('DELETE FROM matrice')
conn.commit()

# inserimento dei dati nella tabella
righe, colonne = arr2d.shape # ottiene il numero di righe e colonne della matrice
inserire = [
    (i, j, int(arr2d[i, j]))
    for i in range(righe)
    for j in range(colonne)
] 

# inserimento dei dati nella tabella matrice       
cursor.executemany('INSERT INTO matrice (r, c, val) VALUES (?, ?, ?)', inserire)
conn.commit()

#letturew dei dati dalla tabella

cursor.execute('SELECT r,c,val FROM matrice ORDER BY r, c')
righe = cursor.fetchall()

for r, c, v in righe:
    print(f"riga {r}, colonna {c}, valore {v}")
conn.close()