# Programma che accetta un input di parole e restituisce se è palindroma o no


def is_pal(a): # Funzione che verifica se l'argomento è palindromo
    return  a == a[::-1]

def pulisci_stringa(stringa): # Pulisce la stringa da caratteri speciali e spazi
    return ''.join(c for c in stringa if c.isalnum())


user_input = input('Inserisci una parola o una frase: ') # Input utente in minuscolo
stringa_pulita = pulisci_stringa(user_input.lower()) # Stringa pulita dalla funzione
if is_pal(stringa_pulita):
    print(f'\'{user_input}\' è palindroma')
else:
    print(f'\'{user_input}\' non è palintroma')
    

