# Input che chiede all'utente un intervallo
num1 = int(input('Inserisci un intervallo, il primo numero: '))
num2 = int(input('secondo numero: '))

check_list = []

# Calcolo numeri primi nell'intervallo
for n in range(num1, num2 + 1):
    if n < 2:
        continue
    
    primary = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primary = False
            break
        
    # Se primo, aggiunge a lista check_list
    if primary:
        check_list.append(n)


print(check_list)
    
