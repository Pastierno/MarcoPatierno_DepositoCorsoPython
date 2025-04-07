
user_input = input('Inserisci una stringa: ')

lista = list(''.join(user_input)) # Crea lista con caratteri singoli

chiavi = set(lista)

dizionario = {}

for c in chiavi:
    dizionario[c] = lista.count(c)
print(dizionario)
    
#________________ 

# conto = {}

# for c in user_input:
#     if c in conto:
#         conto[c] += 1
#     else:
#         conto[c] = 1
        
# print(conto)
