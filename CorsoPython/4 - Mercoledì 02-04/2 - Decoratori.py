def decorator(func):
    def wrapper():
        print('Prima della funzione')
        func()
        print('Dopo la funzione')
    return wrapper # Questo restituisce la funzione decorata
    
@decorator
def saluta():
    print('Ciao')
    

saluta()

# Decoratore con parametri
def decorator_arg(funzione):
    def wrapper(*args, **kwargs):
        print('Before')
        result = funzione(*args, **kwargs)
        print('After')
        return result + 2
    return wrapper

@decorator_arg
def somma(a, b):
    print(a+b)
    return a+b
print(somma(3,4))


# Esempio login
def logger(funzione):
    def wrapper(*args, **kwargs):
        print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
        risultato = funzione(*args, **kwargs)
        print(f"Risultato di {funzione.__name__}: {risultato}")
        return risultato
    return wrapper

@logger
def moltiplica(a, b):
    return a * b

# Chiamata alla funzione decorata
moltiplica(3, 4)