
surname = input("Фамилия: ")
name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст (целое от 1 до 120): "))
subject = input("Любимый предмет: ")
hours_per_week = float(input("Часов подготовки в неделю (неотрицательное число): "))

if age < 1 or age > 120:
    print("Ошибка: возраст должен быть от 1 до 120.")
    raise SystemExit

if hours_per_week < 0:
    print("Ошибка: часы подготовки не могут быть отрицательными.")
    raise SystemExit

age_in_4_years = age + 4
hours_in_4_weeks = hours_per_week * 4
hours_per_day = hours_per_week / 7

print()
print("=" * 40)
print("КАРТОЧКА СТУДЕНТА")
print("=" * 40)
print(f"Полное имя: {name} {surname}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age}")
print(f"Любимый предмет: {subject}")
print(f"Часов подготовки в неделю: {hours_per_week:.2f}")
print("-" * 40)
print(f"Возраст через 4 года: {age_in_4_years}")
print(f"Подготовка за 4 недели: {hours_in_4_weeks:.2f} ч")
print(f"Среднее в день: {hours_per_day:.2f} ч")
print("=" * 40)
