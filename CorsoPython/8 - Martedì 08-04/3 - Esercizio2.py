# Input lungo, verifica duplicati e dice frequenza e lunghezza

def duplicate(text):
    # Restituisce una lista con ogni parola separata
    return [''.join(c for c in word if c.isalnum()) for word in text.lower().split()]
    
def word_count(text):
    # Prende per ogni parola assegna il numero di occorrenze e il numero di caratteri
    word_dict = {w: (duplicate(text).count(w), len(w)) for w in duplicate(text)}
    for k, (v1, v2) in word_dict.items():
        # Controllo che manda a schermo solo i duplicati
        if v1 > 1:
            print(f'{k} ha {v1} occorrenze e {v2} è il numero di caratteri')
        
            
    
word_count('Python,,,,,, 12 12 123 Python python forza Napoli')


    

        
    