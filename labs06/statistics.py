line = input("Целые числа через пробел: ")

numbers = []
for part in line.split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    count = len(numbers)
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total / count

    print(f"Количество: {count}")
    print(f"Сумма: {total}")
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Среднее: {average:.2f}")
