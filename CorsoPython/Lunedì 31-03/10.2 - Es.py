# Chiede all'utente se inserire due interi o due stringhe
user_input = int(input('Vuoi confrontare due numeri o stringhe? \n'
                        '1 - Numeri \n'
                        '2 - Stringhe \n'))

# Condizione per numeri o stringhe
if user_input == 1:
    
    # Input che chiede all'utente un intervallo
    num1 = int(input('Inserisci il primo numero: '))
    num2 = int(input('secondo numero: '))
    
    # Ordinamento minore => maggiore
    if num1 < num2:
        num1, num2 = num2, num1

    # Lista dove inserire i numeri nell'intervallo
    fact = []
    
    # Ciclo per determinare i fattori comuni
    for n in range(1, num1 + 1):
        if num1 % n == 0 and num2 % n == 0:
            fact.append(n)
            
    # Manda a schermo i risultati
    print(f'{fact} sono i fattori comuni')
    if fact == [1]:
        print('I numeri sono coprimi!')

# Stringhe
elif user_input == 2:
    
    # Input per due stringhe
    str1 = input('Inserisci una parola: ').lower()
    str2 = input('Inserisci una seconda parola: ').lower()
        
    # Controllo caratteri nelle due parole
    if sorted(str1) == sorted(str2):
        print('Sono complementari')
    else:
        print('Le due parole non sono complementari')
        
        


