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

# Tuple
point = (3, 4)
rgb_color = (255, 128, 0)
person = ('Marco', 26, 'Maschio')

print(point)
print(rgb_color)
print(person)

# Set
set1 = {5, 5, 2, 3}
set2 = set([4,5,6,3])
set3 = {2,1,3,3,4,4,5}
print(set3)

# Unione
union1 = set1 | set2
union2 = set1.union(set3)
print(union1)
print(union2)

# Intersezione
intersection1 = set1.intersection(set2)
intersection2 = set1 & set3

# Differenza
difference1 = set2.difference(set1)
difference2 = set2 - set1

# Differenza simmetrica
symmetric_difference1 = set3.symmetric_difference(set1)
symmetric_difference2 = set3 ^ set1
