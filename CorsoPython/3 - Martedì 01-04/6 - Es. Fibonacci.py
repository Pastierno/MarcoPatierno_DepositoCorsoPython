# Sequenza di Fibonacci
def fibonacci(n):
    x = 0
    y = 1
    seq = []
    
    # Iterazione sequenza
    for i in range(n):
        seq.append(x)
        x, y = y, x + y
    return seq
        
        
        
n = int(input('Inserisci un numero: '))
print('Ecco la sequenza: ')
print(fibonacci(n))
