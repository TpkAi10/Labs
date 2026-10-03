line = input("Целые числа через пробел: ")

numbers = []
for part in line.split():
    numbers.append(int(part))

selected = []
for number in numbers:
    if number % 5 == 0:
        selected.append(number)

count = len(selected)
total = sum(selected)
sorted_copy = sorted(selected)

print(f"Выборка: {selected}")
print(f"Количество: {count}")
print(f"Сумма: {total}")
print(f"Сортированная копия: {sorted_copy}")
