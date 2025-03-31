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

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers.range(0, 9, 2))