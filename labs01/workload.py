
subject1 = input("Название первого предмета: ")
subject2 = input("Название второго предмета: ")

lessons1 = int(input(f"Количество занятий по предмету «{subject1}» за неделю: "))
minutes1 = int(input(f"Продолжительность одного занятия по «{subject1}» (мин): "))

lessons2 = int(input(f"Количество занятий по предмету «{subject2}» за неделю: "))
minutes2 = int(input(f"Продолжительность одного занятия по «{subject2}» (мин): "))

if lessons1 < 0 or lessons2 < 0:
    print("Ошибка: количество занятий не может быть отрицательным.")
    raise SystemExit

if minutes1 <= 0 or minutes2 <= 0:
    print("Ошибка: продолжительность занятия должна быть положительной.")
    raise SystemExit

total1 = lessons1 * minutes1
total2 = lessons2 * minutes2

total_minutes = total1 + total2
total_hours = total_minutes / 60

available_hours = float(input("Доступное время на неделю (часов): "))

if available_hours < total_hours:
    print("Ошибка: доступное время меньше суммарной нагрузки.")
    raise SystemExit

free_hours = available_hours - total_hours

four_weeks_hours = total_hours * 4

print()
print("=" * 45)
print("УЧЕБНАЯ НАГРУЗКА")
print("=" * 45)
print(f"{subject1}: {total1} мин")
print(f"{subject2}: {total2} мин")
print("-" * 45)
print(f"Общая нагрузка: {total_minutes} мин или {total_hours:.2f} ч")
print(f"Свободное время: {free_hours:.2f} ч")
print(f"Нагрузка за 4 недели: {four_weeks_hours:.2f} ч")
print("=" * 45)
