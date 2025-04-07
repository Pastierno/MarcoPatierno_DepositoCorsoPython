# Alunni, voti, media voti

dizionario = {}
def media_voti():
    for alunno, voti in dizionario.items():
         media = sum(voti) / len(voti)
         print(f"Media di {alunno}: {media:.2f}")
     
def inserimento():
    while True:
        alunno = input('Inserisci un alunno: ').lower()
        voto = float(input('Inserisci voto: '))
        if alunno in dizionario: 
            dizionario[alunno].append(voto)
        else:
            dizionario[alunno] = [voto]
                
        print(dizionario)
        loop = int(input('Vuoi continuare? (1, Si/ 2, No)')) 
        if loop == 1:
            continue
        else:
            media_voti()
            break

inserimento()




    


