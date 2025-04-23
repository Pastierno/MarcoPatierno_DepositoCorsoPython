# Crea una funzione che restituisce il quadrato di un numero

def quadrato(n):
    return n ** 2

print(quadrato(7))

# Funzione che restituisce la somma di elementi in una lista

def somma_lista(lista):
    count = 0
    for e in lista:
        count += e
    return count

lista = [1, 2, 3]
print(somma_lista(lista))