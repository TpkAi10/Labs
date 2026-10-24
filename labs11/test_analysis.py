import json
from pathlib import Path
from tempfile import TemporaryDirectory

from analysis import (
    validate_todos,
    completion_counts,
    top_users,
    leader_tasks,
    select_tasks,
)


# --- Учебный набор ---
sample = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]

validate_todos(sample)
assert completion_counts(sample) == {5: 2, 10: 2}
assert top_users({5: 2, 10: 2}) == [5, 10]
leaders = top_users(completion_counts(sample))
assert [r["id"] for r in leader_tasks(sample, leaders)] == [1, 3, 4, 5]

# --- Пустой список ---
assert completion_counts([]) == {}
assert top_users({}) == []
assert leader_tasks([], []) == []

# --- Только completed=False ---
only_false = [
    {"id": 1, "userId": 5, "title": "A", "completed": False},
    {"id": 2, "userId": 5, "title": "B", "completed": False},
]
assert completion_counts(only_false) == {5: 0}
assert top_users(completion_counts(only_false)) == []
assert leader_tasks(only_false, []) == []

# --- Единственный лидер ---
single = [
    {"id": 1, "userId": 1, "title": "A", "completed": True},
    {"id": 2, "userId": 1, "title": "B", "completed": True},
    {"id": 3, "userId": 2, "title": "C", "completed": False},
]
assert top_users(completion_counts(single)) == [1]

# --- Несколько лидеров ---
assert top_users({1: 3, 2: 3, 3: 1}) == [1, 2]

# --- Вариант 14: незавершённые, длина title >= порога ---
# Для sample, user_id=5, threshold=5: задача id=2 «Циклы» — длина 5, не завершена → [2]
assert [r["id"] for r in select_tasks(sample, 5, 5)] == [2]
# Порог 6: «Циклы» длиной 5 не подходит
assert select_tasks(sample, 5, 6) == []
# Неизвестный пользователь
assert select_tasks(sample, 999, 0) == []
# Непустой набор без совпадений
assert select_tasks(sample, 10, 100) == []
# Равенство границе: длина «Циклы» = 5
assert [r["id"] for r in select_tasks(sample, 5, 5)] == [2]
# Все незавершённые пользователя 5
assert [r["id"] for r in select_tasks(sample, 5, 0)] == [2]

# --- Ошибки валидации ---
def expect_value_error(data):
    try:
        validate_todos(data)
    except ValueError:
        pass
    else:
        assert False, "ValueError не возник"


expect_value_error({"id": 1})                    # не список
expect_value_error([1, 2])                        # элемент не словарь
expect_value_error([{"userId": 5, "title": "A", "completed": True}])   # нет id
expect_value_error([{"id": 1, "title": "A", "completed": True}])        # нет userId
expect_value_error([{"id": 1, "userId": 5, "completed": True}])         # нет title
expect_value_error([{"id": 1, "userId": 5, "title": "A"}])              # нет completed
expect_value_error([{"id": True, "userId": 5, "title": "A", "completed": True}])  # id=True
expect_value_error([{"id": 1, "userId": 5, "title": "", "completed": True}])      # пустой title
expect_value_error([{"id": 1, "userId": 5, "title": "A", "completed": "false"}])  # completed строка

# Повторный id
dup = [
    {"id": 1, "userId": 5, "title": "A", "completed": True},
    {"id": 1, "userId": 5, "title": "B", "completed": True},
]
expect_value_error(dup)

# --- Запись и повторное чтение JSON ---
with TemporaryDirectory() as directory:
    path = Path(directory) / "selected.json"
    selected = select_tasks(sample, 5, 0)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(selected, file, ensure_ascii=False, indent=2)
    with open(path, "r", encoding="utf-8") as file:
        restored = json.load(file)
    assert restored == selected

print("Все проверки пройдены")
