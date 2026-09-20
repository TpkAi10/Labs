
print("=" * 50)
print("ФРАГМЕНТ А")
print("=" * 50)

first = "10"
second = "25"

print(f"Тип first до преобразования: {type(first)}")
print(f"Тип second до преобразования: {type(second)}")

first = int(first)
second = int(second)

print(f"Тип first после преобразования: {type(first)}")
print(f"Тип second после преобразования: {type(second)}")

print(f"Сумма чисел: {first + second}")


print()
print("=" * 50)
print("ФРАГМЕНТ Б")
print("=" * 50)

age_str = input("Возраст: ")
print(f"Тип age до преобразования: {type(age_str)}")

age = int(age_str)
print(f"Тип age после преобразования: {type(age)}")

print(f"Возраст через год: {age + 1}")


print()
print("=" * 50)
print("ФРАГМЕНТ В")
print("=" * 50)


first = 10
second = 20
third = 30

average = (first + second + third) / 3
print(f"Среднее трёх чисел: {average}")
