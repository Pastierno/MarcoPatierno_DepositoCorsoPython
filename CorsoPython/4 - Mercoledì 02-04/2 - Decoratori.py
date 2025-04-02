def decorator(func):
    def wrapper():
        print('Prima della funzione')
        func()
        print('Dopo la funzione')
    return wrapper
    
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


    