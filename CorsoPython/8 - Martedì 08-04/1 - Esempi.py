def funzione(a, b = 0): # Così rendiamo opzionale b. Se il primo è opzionale lo devono essere tutti
    valore = a + b
    print(valore)
    return valore, 10

valore, altrovalore = funzione()
print(altrovalore)
    
#_____________________________________________________________

def funzione(*args): # Rende tutti gli argomenti in una tupla
    print(args)
    print(args[0] + args[2])
    
funzione(10, 11, 12, 4) 

#_____________________________________________________________

def funzione(**args): # Dizionario
    print(args)
    print(args['nome'])
    
funzione(nome = 'Marco', cognome = 'Patierno', eta = 26)

#____________________________________________________________
#Spazio globale e locale
eta = 26
def funzione():
    print(eta)

eta = 26
def funzione():
    global eta # Non posso modificare variabili globali in spazio locale senza definire global
    eta + 1
    print(eta)

eta = 26
def funzione():
    nuova_eta = eta + 1 # Non esiste variabile senza return
    return nuova_eta

nuova_eta = funzione()

#___________________________________________________________

# Funzione su elementi di un iterabile

lista = [1, 2, 3, 4, 5]

def func(a):
    return a*2

for i in range(len(lista)):
    lista[i] = func(lista[i])

lista = list(map(func,lista))    # Trasforma in base all'input


print(lista)

####################

def pari(a):
    return a % 2 == 0

lista2 = []

for i in lista:
    if pari(i):
        lista2.append(i)

lista2 = list(filter(pari, lista))    # Filtra in base all'input
        
print(lista2)

####################

lista = [1, 2, 3, 4, 5]

stringa = '-'.join(lista) # Funziona solo se sono stringhe gli elementi

