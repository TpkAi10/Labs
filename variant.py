total = int(input("Общее количество плиток (>= 0): "))
capacity = int(input("Плиток в одной упаковке (> 0): "))

if total < 0:
    print("Ошибка: количество плиток не может быть отрицательным.")
    raise SystemExit

if capacity <= 0:
    print("Ошибка: вместимость упаковки должна быть положительной.")
    raise SystemExit


full_units = total // capacity              
remainder = total % capacity                     
total_units = (total + capacity - 1) // capacity   

print()
print("=" * 40)
print("РАСЧЁТ УПАКОВОК")
print("=" * 40)
print(f"Всего плиток: {total}")
print(f"Плиток в упаковке: {capacity}")
print("-" * 40)
print(f"Полных упаковок: {full_units}")
print(f"Остаток плиток: {remainder}")
print(f"Всего упаковок: {total_units}")
print("=" * 40)
