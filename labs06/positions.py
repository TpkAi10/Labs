line = input("Целые числа через пробел: ")

numbers = []
for part in line.split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    maximum = max(numbers)

    positions = []
    for index, value in enumerate(numbers):
        if value == maximum:
            positions.append(index)

    print(f"Максимум: {maximum}")
    print(f"Индексы: {positions}")
