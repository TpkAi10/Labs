import json
from pathlib import Path
from analysis import (
    validate_todos,
    completion_counts,
    top_users,
    leader_tasks,
    select_tasks,
)


def read_positive_integer(prompt):
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


def read_non_negative_integer(prompt):
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


def main():
    folder = Path(__file__).resolve().parent
    source = folder / "todos.json"
    leaders_file = folder / "leaders.json"
    selected_file = folder / "selected.json"

    # --- Чтение и проверка ---
    try:
        with open(source, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Файл не найден: {source}")
        return
    except UnicodeError:
        print("Ошибка кодировки: файл должен быть в UTF-8")
        return
    except json.JSONDecodeError as error:
        print(f"Ошибка JSON: {error}")
        return
    except OSError as error:
        print(f"Ошибка доступа: {error}")
        return

    try:
        validate_todos(data)
    except ValueError as error:
        print(f"Ошибка структуры: {error}")
        return

    # --- Анализ ---
    counts = completion_counts(data)
    leaders = top_users(counts)
    tasks = leader_tasks(data, leaders)

    print("Количество завершённых по пользователям:")
    for user in sorted(counts):
        print(f"  пользователь {user}: {counts[user]}")
    print(f"Лидеры: {leaders}")

    # --- Сохранение лидеров ---
    try:
        with open(leaders_file, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=2)
        print(f"Задачи лидеров сохранены: {leaders_file.name}")
    except OSError as error:
        print(f"Не удалось сохранить лидеров: {error}")
        return

    # --- Индивидуальный вариант ---
    user_id = read_positive_integer("Введите user_id: ")
    threshold = read_non_negative_integer("Минимальная длина названия: ")

    selected = select_tasks(data, user_id, threshold)

    print(f"Подходящих задач: {len(selected)}")
    for record in selected:
        print(f"  id={record['id']} title={record['title']}")

    try:
        with open(selected_file, "w", encoding="utf-8") as file:
            json.dump(selected, file, ensure_ascii=False, indent=2)
        print(f"Выборка сохранена: {selected_file.name}")
    except OSError as error:
        print(f"Не удалось сохранить выборку: {error}")


if __name__ == "__main__":
    main()
