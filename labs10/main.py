from pathlib import Path
from files_lab import read_matrix, selected_sum
from table import row_sums, column_sums


def read_positive_integer():
    """Повторять ввод, пока не получено целое > 0.
    Различать «не целое» и «не больше нуля»."""
    while True:
        text = input("Введите положительное целое: ")
        try:
            value = int(text)
        except ValueError:
            print("Это не целое число. Попробуйте снова.")
            continue
        if value <= 0:
            print("Число должно быть больше нуля. Попробуйте снова.")
            continue
        return value


def main():
    folder = Path(__file__).resolve().parent
    source = folder / "matrix.txt"
    report = folder / "report.txt"

    try:
        matrix = read_matrix(source)
    except FileNotFoundError:
        print(f"Файл не найден: {source}")
        return
    except UnicodeError:
        print("Ошибка кодировки: файл должен быть в UTF-8")
        return
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
        return
    except ValueError as error:
        print(f"Ошибка формата: {error}")
        return

    # Все данные проверены — только теперь пишем отчёт
    rows = row_sums(matrix)
    cols = column_sums(matrix)
    variant = selected_sum(matrix)

    try:
        with open(report, "w", encoding="utf-8") as file:
            file.write("Суммы строк: " + " ".join(str(x) for x in rows) + "\n")
            file.write("Суммы столбцов: " + " ".join(str(x) for x in cols) + "\n")
            file.write(f"Результат варианта: {variant}\n")
    except OSError as error:
        print(f"Не удалось записать отчёт: {error}")
        return

    print(f"Отчёт записан в {report}")


if __name__ == "__main__":
    main()
