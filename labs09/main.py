from table import row_sums, column_sums, diagonal_pattern, transform


def read_matrix():
    """Ввод прямоугольной матрицы с проверкой длины строк."""
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))

    matrix = []
    for _ in range(rows):
        row = [int(part) for part in input("Строка таблицы: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    """Вывод матрицы по строкам."""
    for row in matrix:
        print(*row)


def main():
    # 1. Ввод матрицы
    matrix = read_matrix()

    print("\nИсходная матрица:")
    print_matrix(matrix)

    # 2. Суммы строк и столбцов
    print(f"\nСуммы строк: {row_sums(matrix)}")
    print(f"Суммы столбцов: {column_sums(matrix)}")

    # 3. Диагональный узор
    size = int(input("\nРазмер узора (>= 1): "))
    pattern = diagonal_pattern(size)
    print("Диагональный узор:")
    print_matrix(pattern)

    # 4. Индивидуальный вариант
    new_matrix = transform(matrix)
    print("\nИсходная матрица:")
    print_matrix(matrix)
    print("Новая матрица:")
    print_matrix(new_matrix)


if __name__ == "__main__":
    main()
