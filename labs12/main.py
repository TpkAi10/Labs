from pathlib import Path
from logic import (
    validate_records,
    add_record,
    find_records,
    set_completed,
    delete_record,
    statistics,
)
from storage import load_records, save_records


def read_non_empty(prompt):
    """Повторять ввод, пока не получена непустая строка после strip()."""
    while True:
        text = input(prompt).strip()
        if text == "":
            print("Значение не должно быть пустым. Попробуйте снова.")
            continue
        return text


def read_non_negative_int(prompt):
    """Повторять ввод, пока не получено целое >= 0."""
    while True:
        text = input(prompt)
        try:
            value = int(text)
        except ValueError:
            print("Это не целое число. Попробуйте снова.")
            continue
        if value < 0:
            print("Число должно быть неотрицательным. Попробуйте снова.")
            continue
        return value


def read_positive_int(prompt):
    """Повторять ввод, пока не получено целое > 0."""
    while True:
        text = input(prompt)
        try:
            value = int(text)
        except ValueError:
            print("Это не целое число. Попробуйте снова.")
            continue
        if value <= 0:
            print("Число должно быть больше нуля. Попробуйте снова.")
            continue
        return value


def show_records(records):
    if len(records) == 0:
        print("Нет записей")
        return
    for record in sorted(records, key=lambda r: r["id"]):
        status = "выполнено" if record["completed"] else "не выполнено"
        print(
            f"{record['id']}. {record['title']} | "
            f"{record['category']} | "
            f"{record['amount']} участников | {status}"
        )


def show_statistics(records):
    stats = statistics(records)
    print(f"Всего записей: {stats['total']}")
    print(f"Выполнено: {stats['completed']}")
    print(f"Не выполнено: {stats['not_completed']}")
    print(f"Сумма участников: {stats['total_amount']}")
    print("По категориям:")
    for category in sorted(stats["by_category"]):
        print(f"  {category}: {stats['by_category'][category]}")


def main():
    folder = Path(__file__).resolve().parent
    path = folder / "data.json"

    # --- Загрузка ---
    try:
        records = load_records(path)
    except FileNotFoundError:
        print("Файл data.json не найден. Начинаем с пустого списка.")
        records = []
    except UnicodeError:
        print("Ошибка кодировки: файл должен быть в UTF-8. Запуск прекращён.")
        return
    except ValueError as error:
        print(f"Ошибка формата JSON: {error}. Запуск прекращён.")
        return
    except OSError as error:
        print(f"Ошибка доступа: {error}. Запуск прекращён.")
        return

    try:
        validate_records(records)
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}. Запуск прекращён.")
        return

    # --- Меню ---
    while True:
        print()
        print("1. Показать записи")
        print("2. Добавить запись")
        print("3. Найти записи")
        print("4. Изменить статус")
        print("5. Удалить запись")
        print("6. Показать статистику")
        print("7. Сохранить данные")
        print("0. Выйти")
        choice = input("Команда: ").strip()

        if choice == "1":
            show_records(records)
        elif choice == "2":
            title = read_non_empty("Название: ")
            category = read_non_empty("Категория: ")
            amount = read_non_negative_int("Количество участников: ")
            record = add_record(records, title, category, amount)
            print(f"Добавлена запись id={record['id']}")
        elif choice == "3":
            query = read_non_empty("Подстрока названия: ")
            found = find_records(records, query)
            if len(found) == 0:
                print("Ничего не найдено")
            else:
                for record in found:
                    print(f"{record['id']}. {record['title']}")
        elif choice == "4":
            record_id = read_positive_int("ID записи: ")
            answer = read_non_empty("Отметить как выполнено? (да/нет): ").lower()
            if answer not in ("да", "нет"):
                print("Ответ должен быть «да» или «нет»")
                continue
            completed = answer == "да"
            if set_completed(records, record_id, completed):
                print("Статус изменён")
            else:
                print(f"Запись с id={record_id} не найдена")
        elif choice == "5":
            record_id = read_positive_int("ID записи: ")
            answer = input(f"Удалить запись id={record_id}? (да/нет): ").strip().lower()
            if answer != "да":
                print("Удаление отменено")
                continue
            if delete_record(records, record_id):
                print("Запись удалена")
            else:
                print(f"Запись с id={record_id} не найдена")
        elif choice == "6":
            show_statistics(records)
        elif choice == "7":
            try:
                save_records(path, records)
                print("Данные сохранены")
            except OSError as error:
                print(f"Не удалось сохранить: {error}")
        elif choice == "0":
            while True:
                answer = input("Сохранить данные перед выходом? (да/нет): ").strip().lower()
                if answer == "да":
                    try:
                        save_records(path, records)
                        print("Данные сохранены")
                        return
                    except OSError as error:
                        print(f"Не удалось сохранить: {error}. Остаёмся в меню.")
                        break
                elif answer == "нет":
                    print("Выход без сохранения")
                    return
                else:
                    print("Ответ должен быть «да» или «нет»")
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()
