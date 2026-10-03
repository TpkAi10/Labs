line = input("Целые числа через пробел: ")

numbers = []
for part in line.split():
    numbers.append(int(part))


transformed = []
for number in numbers:
    if number < 0:
        transformed.append(-number)
    else:
        transformed.append(number)

print(f"Исходный список: {numbers}")
print(f"Новый список: {transformed}")
