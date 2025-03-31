# Esercizio 4: combinazione if, while e for

# Chiede lista di numeri
user_input = input('Inserisci una serie di numeri separati da una virgola: ')

# Separiamo l'input in numeri singoli da inserire nella lista
num_list = user_input.split(',')

# Convertire in interi
for n in range(len(num_list)):
    num_list[n] = int(num_list[n])

# Controllo per tipo nella lista
#print(type(num_list[1]))
#print(num_list)

# Trovare il massimo nella lista
num_max = []
for n in num_list:
    num_max.append(n)

print(max(num_max))

# Controllo numeri nella lista
control = True
count = 0
while control:
    if count != len(num_list):
        count += 1
    else:
        print(count)
        control = False
        

# Controllo lista vuota o stampa numero massimo e lunghezza lista
if len(num_list) != 0:
    print(f'La lista ha {len(num_list)} elementi e {count} è il numero massimo')

    
    
    
    