value = int(input("Значение от 0 до 100: "))

if value < 0 or value > 100:
    print("Ошибка диапазона")
elif value <= 19:
    print("Малый запас")
elif value <= 64:
    print("Средний запас")
else:
    print("Большой запас")
