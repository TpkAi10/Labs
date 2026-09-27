attempts = 0
value = int(input("Введите целое число: "))

while value <= 0:
    attempts += 1
    value = int(input("Число должно быть положительным, попробуйте снова: "))

square = value * value
print(f"Квадрат: {square}")
print(f"Отклонено попыток: {attempts}")
