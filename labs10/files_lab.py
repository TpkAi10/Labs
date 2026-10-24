def read_matrix(path):
    """Прочитать матрицу из файла UTF-8.
    Формат: первая строка — rows cols (положительные),
    далее ровно rows строк по cols целых чисел.
    При ошибке формата — ValueError с номером строки."""
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Убираем переводы строк, но сохраняем пустые строки как ошибку
    lines = [line.rstrip("\n") for line in lines]

    # Один обычный перевод строки после последней строки данных допустим
    while lines and lines[-1] == "":
        lines.pop()

    if len(lines) == 0:
        raise ValueError("Файл пуст")

    # --- Заголовок ---
    header = lines[0].split()
    if len(header) != 2:
        raise ValueError("Строка 1: ожидалось два числа (строки и столбцы)")

    try:
        rows = int(header[0])
        cols = int(header[1])
    except ValueError:
        raise ValueError("Строка 1: ожидались целые числа")

    if rows <= 0 or cols <= 0:
        raise ValueError("Строка 1: количество строк и столбцов должно быть положительным")

    # --- Строки данных ---
    data_lines = lines[1:]
    if len(data_lines) != rows:
        raise ValueError(
            f"Ожидалось {rows} строк данных, получено {len(data_lines)}"
        )

    matrix = []
    for index, line in enumerate(data_lines, start=2):
        parts = line.split()
        if len(parts) != cols:
            raise ValueError(
                f"Строка {index}: ожидалось {cols} чисел, получено {len(parts)}"
            )
        row = []
        for part in parts:
            try:
                row.append(int(part))
            except ValueError:
                raise ValueError(f"Строка {index}: «{part}» не является целым числом")
        matrix.append(row)

    return matrix


def selected_sum(matrix):
    """Вариант 14: сумма положительных элементов с нечётным индексом столбца.
    Индексы с нуля. Если подходящих нет — 0."""
    total = 0
    for row in matrix:
        for col in range(len(row)):
            value = row[col]
            if col % 2 == 1 and value > 0:
                total += value
    return total
