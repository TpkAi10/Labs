def row_sums(matrix):
    """Список сумм строк. Для [] возвращает []."""
    result = []
    for row in matrix:
        result.append(sum(row))
    return result


def column_sums(matrix):
    """Список сумм столбцов. Для [] возвращает [].
    Непустая матрица прямоугольная, хотя бы один столбец."""
    if len(matrix) == 0:
        return []
    columns = len(matrix[0])
    result = []
    for col in range(columns):
        total = 0
        for row in matrix:
            total += row[col]
        result.append(total)
    return result


def diagonal_pattern(size):
    """Квадратная таблица size×size:
    на диагонали 0, выше — 1, ниже — 2."""
    matrix = []
    for row in range(size):
        line = []
        for col in range(size):
            if row == col:
                line.append(0)
            elif row < col:
                line.append(1)
            else:
                line.append(2)
        matrix.append(line)
    return matrix


def transform(matrix):
    """Вариант 14: элементы от -2 до 3 включительно возвести в квадрат.
    Возвращает новую матрицу той же формы, исходная не меняется."""
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            if -2 <= value <= 3:
                new_row.append(value ** 2)
            else:
                new_row.append(value)
        result.append(new_row)
    return result
