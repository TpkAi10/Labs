def validate_todos(data):
    """Проверить структуру. При нарушении — ValueError."""
    if not isinstance(data, list):
        raise ValueError("Корень должен быть списком")

    seen_ids = set()
    for index, record in enumerate(data):
        prefix = f"Запись {index}"
        if not isinstance(record, dict):
            raise ValueError(f"{prefix}: должна быть словарём")

        # id — положительное целое, уникальное
        if "id" not in record:
            raise ValueError(f"{prefix}: отсутствует id")
        if type(record["id"]) is not int:
            raise ValueError(f"{prefix}: id должен быть целым")
        if record["id"] <= 0:
            raise ValueError(f"{prefix}: id должен быть положительным")
        if record["id"] in seen_ids:
            raise ValueError(f"{prefix}: повторяющийся id {record['id']}")
        seen_ids.add(record["id"])

        # userId — положительное целое
        if "userId" not in record:
            raise ValueError(f"{prefix}: отсутствует userId")
        if type(record["userId"]) is not int:
            raise ValueError(f"{prefix}: userId должен быть целым")
        if record["userId"] <= 0:
            raise ValueError(f"{prefix}: userId должен быть положительным")

        # title — непустая строка
        if "title" not in record:
            raise ValueError(f"{prefix}: отсутствует title")
        if not isinstance(record["title"], str):
            raise ValueError(f"{prefix}: title должен быть строкой")
        if record["title"] == "":
            raise ValueError(f"{prefix}: title не должен быть пустым")

        # completed — логическое
        if "completed" not in record:
            raise ValueError(f"{prefix}: отсутствует completed")
        if type(record["completed"]) is not bool:
            raise ValueError(f"{prefix}: completed должен быть bool")


def completion_counts(todos):
    """Словарь userId → число завершённых задач (для всех пользователей)."""
    counts = {}
    for record in todos:
        user = record["userId"]
        if user not in counts:
            counts[user] = 0
        if record["completed"]:
            counts[user] += 1
    return counts


def top_users(counts):
    """Отсортированный список userId с максимумом завершённых.
    Пустой словарь или максимум 0 → []."""
    if len(counts) == 0:
        return []
    maximum = max(counts.values())
    if maximum == 0:
        return []
    return sorted(user for user, value in counts.items() if value == maximum)


def leader_tasks(todos, leaders):
    """Завершённые задачи лидеров, исходный порядок."""
    result = []
    for record in todos:
        if record["userId"] in leaders and record["completed"]:
            result.append(record)
    return result


def select_tasks(todos, user_id, parameter=None):
    """Вариант 14: незавершённые задачи пользователя с длиной title >= порога.
    parameter — целое неотрицательное число. Порядок сохраняется."""
    result = []
    for record in todos:
        if record["userId"] != user_id:
            continue
        if record["completed"]:
            continue
        if len(record["title"]) >= parameter:
            result.append(record)
    return result
