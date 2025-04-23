# Alunni, voti, media voti

dizionario = {} # Dizionario vuoto 

def media_voti(): # Calcola la media per ogni alunno e manda a schermo tutti i risultati
    for alunno, voti in dizionario.items():
         media = sum(voti) / len(voti)
         print(f"Media di {alunno}: {media:.2f}")
     
def inserimento():
    while True: # Ciclo per inserimento multiplo
        alunno = input('Inserisci un alunno: ').lower() # inserisce alunno e voto, se non c'è, lo aggiunge
        voto = float(input('Inserisci voto: '))
        if alunno in dizionario: 
            dizionario[alunno].append(voto)
        else:
            dizionario[alunno] = [voto]
                
        print(dizionario)
        loop = int(input('Vuoi continuare? (1, Si/ 2, No)')) # Per ripetere o stampa medie
        if loop == 1:
            continue
        else:
            media_voti()
            break

inserimento()




    


