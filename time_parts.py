total_seconds = int(input("Всего секунд (целое >= 0): "))

if total_seconds < 0:
    print("Ошибка: число секунд не может быть отрицательным.")
    raise SystemExit

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{hours} ч {minutes} мин {seconds} с")
