from table import row_sums, column_sums, diagonal_pattern, transform


# --- row_sums / column_sums ---
assert row_sums([[1, 2, 3], [4, 5, 6]]) == [6, 15]
assert column_sums([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]

assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]

assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert column_sums([[1], [-1], [0]]) == [0]

assert row_sums([]) == []
assert column_sums([]) == []

# --- diagonal_pattern ---
assert diagonal_pattern(1) == [[0]]
assert diagonal_pattern(3) == [
    [0, 1, 1],
    [2, 0, 1],
    [2, 2, 0],
]

# --- transform (вариант 14: от -2 до 3 включительно возвести в квадрат) ---
control = [[-2, 0, 3], [4, -5, 6]]
assert transform(control) == [[4, 0, 9], [4, -5, 6]]
assert transform([]) == []

# Внутри диапазона: -2, 0, 3 → квадраты
assert transform([[-1, 1, 2]]) == [[1, 1, 4]]
# Вне диапазона: -3 и 4 не трогаем
assert transform([[-3, 4]]) == [[-3, 4]]

# Границы: -2 и 3 включены
assert transform([[-2]]) == [[4]]
assert transform([[3]]) == [[9]]

# --- Независимость новой матрицы от исходной ---
original = [[-2, 0, 3], [4, -5, 6]]
saved = [row.copy() for row in original]

result = transform(original)
assert original == saved                 # исходная не изменилась

result[0][0] = 999                       # меняем копию
assert original == saved                 # исходная всё ещё не изменилась

# --- Ошибка вложенного списка: [[0]*n]*m ---
bad = [[0] * 3] * 2
bad[0][0] = 7
assert bad == [[7, 0, 0], [7, 0, 0]]     # обе строки изменились — так делать нельзя

good = [[0] * 3 for _ in range(2)]
good[0][0] = 7
assert good == [[7, 0, 0], [0, 0, 0]]    # только первая строка изменилась

print("Все проверки пройдены")
