from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix, selected_sum


def expect_value_error(path):
    """Проверить, что read_matrix(path) бросает ValueError."""
    try:
        read_matrix(path)
    except ValueError:
        pass
    else:
        assert False, "Ошибка не обнаружена"


# --- Обычное чтение ---
with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(path) == [[7, -1]]

# --- 1×1 ---
with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("1 1\n0\n", encoding="utf-8")
    assert read_matrix(path) == [[0]]

# --- Пустой файл ---
with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("", encoding="utf-8")
    expect_value_error(path)

# --- Заголовок 0 3 ---
with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("0 3\n", encoding="utf-8")
    expect_value_error(path)

# --- Заголовок 1 2, одна строка ---
with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("1 2\n1\n", encoding="utf-8")
    expect_value_error(path)

# --- Нечисловая ячейка ---
with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("1 2\n1 x\n", encoding="utf-8")
    expect_value_error(path)

# --- Две строки данных при rows=1 ---
with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("1 1\n7\n8\n", encoding="utf-8")
    expect_value_error(path)

# --- Отсутствующий файл ---
with TemporaryDirectory() as directory:
    path = Path(directory) / "no_such_file.txt"
    try:
        read_matrix(path)
    except FileNotFoundError:
        pass
    else:
        assert False, "FileNotFoundError не возник"

# --- selected_sum: вариант 14 ---
assert selected_sum([[1, -2, 3], [4, 0, -6]]) == 0
assert selected_sum([[1, 2, 3], [4, 5, 6]]) == 7      # 2 + 5
assert selected_sum([[-1, -2, -3]]) == 0
assert selected_sum([[1]]) == 0                        # нет нечётных столбцов
assert selected_sum([[0, 1]]) == 1
assert selected_sum([]) == 0

# --- Один обычный перевод строки после данных допустим ---
with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("1 2\n7 -1\n\n", encoding="utf-8")
    assert read_matrix(path) == [[7, -1]]

print("Все проверки пройдены")
