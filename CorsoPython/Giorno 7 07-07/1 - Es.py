
# user_input = input('Inserisci una stringa: ')

# lista = list(''.join(user_input)) # Crea lista con caratteri singoli

# chiavi = set(lista) # set per prendere solo le chiavi

# dizionario = {} # dict vuoto

# for c in chiavi:
#     dizionario[c] = lista.count(c) # Per ogni carattere nelle chiavi, aggiunge al dizionario con chiave il carattere il conto
    
# print(dizionario)
    
#________________ 

# conto = {}

# for c in user_input:
#     if c in conto:
#         conto[c] += 1
#     else:
#         conto[c] = 1
        
# print(conto)

# #________________

# for l in user_input:
#     dizionario[l] = user_input.count(l)
    
# print(dizionario)

#_____________
stringa = "banana"
lista = list(stringa)
dizi = {}

for i in lista:
    dizi.setdefault(i, lista.count(i))

print(dizi)