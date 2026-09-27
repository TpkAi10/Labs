n = int(input("Сколько чисел ввести (n >= 0): "))

if n < 0:
    print("Ошибка: n не может быть отрицательным.")
    raise SystemExit

count = 0
total = 0

for i in range(n):
    value = int(input(f"Число {i + 1}: "))
    if value % 5 == 0:
        count += 1
        total += value

print()
print(f"Количество кратных 5: {count}")
print(f"Сумма кратных 5: {total}")
