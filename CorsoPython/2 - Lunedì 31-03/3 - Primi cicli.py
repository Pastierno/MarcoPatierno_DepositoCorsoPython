# Ciclo while

# matematico
count = 0

while count < 5:
    print(count)
    count += 1

# booleano
controllor = True

while controllor:
    
    scelta = input('Vuoi continuare? ')
    if scelta.lower() == 'no':
        controllor = False
    else:
        print('Stai continuanto')
        
# Ciclo for

list = [1,2,3,4,5]
for num in list:
    print(num)
    
string = 'pippo'
for letter in string:
    print(letter)
    
# for in range

for i in range(5, 15, 2):
    print(i)

