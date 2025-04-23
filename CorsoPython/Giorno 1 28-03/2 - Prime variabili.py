nome = 'Marco'
eta = 26
print('Il mio nome è', nome, 'e ho', eta, 'anni.')

nome = input('Inserisci il nome: ')
eta = int(input('Inserisci età: '))
print('Ciao, ' + nome + '! Benvenuto in Python!')

print(1+3, 4-2, 7*8, 10/2, 3**2)

# interi
a = 5
b = -3
print(a, b)

# float
a = 1.1
b = - 5.4
print(a, b)

# stringhe
a = 'Marco'
b = "Prova"
print(a, b)

stringa = "Posizione"
print(stringa[0])
print(stringa[-1])
# print(stringa[100]) #Output: Index error

saluto = 'Ciao'
nome = 'Pippo'
messaggio = saluto + ' ' + nome
print(messaggio)

# manipolazione stringa
s = 'Hello, World!'
print(len(s))
print(s.upper())
print(s.split(','))
print(s.replace('World', 'Mondo'))

# booleani
a = 7
b = 20
c = 1
print(a < b and b > a and b > c)
print(a < b or b < a)
print(not(a > c))

print(a > b and b < a)
print(a > b or b < a)
print(not(a > c))

print(a>=1)
print(a<=10)
print(a==10)
print(a!=c)
