# Prime funzioni

def saluta(nome):
    print('Ciao', nome)
    print('Benvenuto nel nostro programma!')
    
saluta('Marco')

#________________
def somma(x, y):
    res = x + y
    print('La somma è: ', res)

somma(3, 6)

#________________
def quadrato(n):
    return n ** 2

res = quadrato(14)
print(res)