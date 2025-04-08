# Input lungo, verifica duplicati e dice frequenza e lunghezza

def duplicate(text):
    # Restituisce una lista con ogni parola separata
    return [''.join(c for c in word if c.isalnum()) for word in text.lower().split()]
    
def word_count(text):
    words = duplicate(text) # Richiama la funzione che resitutisce il testo separato parola per parola
    word_dict = {w: (words.count(w), len(w)) for w in words}
    print(word_dict)
    
word_count('Python,,,,,, 12 12 123 Python python forza Napoli napoli')


    

        
    