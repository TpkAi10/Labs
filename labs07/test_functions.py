from functions import average, normalize_text, sum_digits, select_numbers


# --- Базовые проверки из условия ---
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

# --- Дополнительные проверки sum_digits ---
assert sum_digits(1) == 1
assert sum_digits(9999) == 36
assert sum_digits(-100) == 1

# --- Дополнительные проверки average ---
assert average([5]) == 5
assert abs(average([1, 2]) - 1.5) < 1e-9
assert average([-2, 2]) == 0

# --- Дополнительные проверки normalize_text ---
assert normalize_text("одно") == "одно"
assert normalize_text("А  Б  В") == "а б в"
assert normalize_text("") == ""

# --- Проверки варианта 14: select_numbers ---

# Обычный случай: контрольный список [-5, 0, 2, 5], порог 2
# Кратны (2+1)=3: 0 → [0]
assert select_numbers([-5, 0, 2, 5], 2) == [0]

# Пустой список
assert select_numbers([], 2) == []

# Без совпадений
assert select_numbers([1, 2, 4, 5], 2) == []

# С совпадениями: кратны 3
assert select_numbers([3, 6, 9, -3], 2) == [3, 6, 9, -3]

# Граница: порог 0 → кратны 1, то есть все числа
assert select_numbers([1, 2, 3], 0) == [1, 2, 3]

# Повторы сохраняются
assert select_numbers([3, 3, 6], 2) == [3, 3, 6]

# Ноль кратен любому ненулевому
assert select_numbers([0, 1, 2], 2) == [0]

# Исходный список не изменяется
original = [-5, 0, 2, 5]
saved = original.copy()
select_numbers(original, 2)
assert original == saved

print("Базовые проверки пройдены")
