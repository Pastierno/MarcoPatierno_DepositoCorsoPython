numbers = [1,2,3,4,5]
names = ['Marco', 'Pippo', 'Pasquale']
mixed = [1, 'due', True, 4.5]

print(numbers[1])
print(mixed[2])

numbers[2] = 5
names[0] = 'Gianfranco'

print(numbers)
print(names)

# metodi

numbers = [3,1,4,2,5]
print(len(numbers))

numbers.append(6)
print(numbers)

numbers.pop()
print(numbers)

numbers.insert(2,10)
print(numbers)

numbers.remove(1)
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=False)
print(numbers)

numbers.reverse()
print(numbers)
