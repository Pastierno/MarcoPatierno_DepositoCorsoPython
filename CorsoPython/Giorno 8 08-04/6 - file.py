# def scrittura(metodo, stringa):
#     with open('prova.txt', 'a') as file: # r = read, w = write, a = append, x = create
#         file.write(stringa)

# def lettura():
#     with open('prova.txt', 'r') as file:
#         contenuto = file.read()
#         return contenuto
# def lettura_linea():
#     with open('prova.txt', 'r') as file:
#         contenuto = file.readlines()
#         return contenuto
    
# scrittura('w', 'nuova')
# print(lettura_linea())

clienti = [['nome','cognome','via'],
           ['marco', 'patierno','via amendola'],
           ['pippo', 'pelo', 'via ciao']]

righe = []

##############################
 
for riga in clienti:
    righe.append(','.join(riga))

file = '\n'.join(righe)

print(righe)
print(file)