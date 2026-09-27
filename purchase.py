price = int(input("Цена одной тетради (целых рублей >= 0): "))
count = int(input("Количество тетрадей (>= 0): "))
paid = int(input("Переданная сумма (руб): "))

if price < 0 or count < 0:
    print("Ошибка: цена и количество не могут быть отрицательными.")
    raise SystemExit

if paid < price * count:
    print("Ошибка: переданной суммы недостаточно.")
    raise SystemExit

cost = price * count
change = paid - cost

print(f"Стоимость: {cost} руб.")
print(f"Сдача: {change} руб.")
