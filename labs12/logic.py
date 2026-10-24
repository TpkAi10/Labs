def validate_records(records):
    """Проверить список записей. При нарушении — ValueError."""
    if not isinstance(records, list):
        raise ValueError("Корень должен быть списком")

    seen_ids = set()
    for index, record in enumerate(records):
        prefix = f"Запись {index}"
        if not isinstance(record, dict):
            raise ValueError(f"{prefix}: должна быть словарём")

        if "id" not in record:
            raise ValueError(f"{prefix}: отсутствует id")
        if type(record["id"]) is not int:
            raise ValueError(f"{prefix}: id должен быть целым")
        if record["id"] <= 0:
            raise ValueError(f"{prefix}: id должен быть положительным")
        if record["id"] in seen_ids:
            raise ValueError(f"{prefix}: повторяющийся id {record['id']}")
        seen_ids.add(record["id"])

        for key in ("title", "category"):
            if key not in record:
                raise ValueError(f"{prefix}: отсутствует {key}")
            if not isinstance(record[key], str):
                raise ValueError(f"{prefix}: {key} должен быть строкой")
            if record[key].strip() == "":
                raise ValueError(f"{prefix}: {key} не должен быть пустым")

        if "amount" not in record:
            raise ValueError(f"{prefix}: отсутствует amount")
        if type(record["amount"]) is not int:
            raise ValueError(f"{prefix}: amount должен быть целым")
        if record["amount"] < 0:
            raise ValueError(f"{prefix}: amount не может быть отрицательным")

        if "completed" not in record:
            raise ValueError(f"{prefix}: отсутствует completed")
        if type(record["completed"]) is not bool:
            raise ValueError(f"{prefix}: completed должен быть bool")


def next_id(records):
    """Следующий id: max + 1, для пустого — 1."""
    if len(records) == 0:
        return 1
    return max(record["id"] for record in records) + 1


def add_record(records, title, category, amount):
    """Добавить запись. Возвращает новую запись.
    Исходный список изменяется."""
    title = title.strip()
    category = category.strip()
    if title == "":
        raise ValueError("Название не должно быть пустым")
    if category == "":
        raise ValueError("Категория не должна быть пустой")
    if type(amount) is not int or amount < 0:
        raise ValueError("Количество должно быть целым неотрицательным")

    record = {
        "id": next_id(records),
        "title": title,
        "category": category,
        "amount": amount,
        "completed": False,
    }
    records.append(record)
    return record


def find_records(records, query):
    """Поиск по непустой подстроке названия без учёта регистра.
    Возвращает новый список, исходный не меняется."""
    query = query.strip()
    if query == "":
        raise ValueError("Поисковый запрос не должен быть пустым")
    query_lower = query.lower()
    return [record for record in records if query_lower in record["title"].lower()]


def set_completed(records, record_id, completed):
    """Установить статус. True при успехе, False если id не найден."""
    for record in records:
        if record["id"] == record_id:
            record["completed"] = completed
            return True
    return False


def delete_record(records, record_id):
    """Удалить по id. True при успехе, False если id не найден."""
    for index, record in enumerate(records):
        if record["id"] == record_id:
            records.pop(index)
            return True
    return False


def statistics(records):
    """Словарь со статистикой. Исходный список не меняется."""
    total = len(records)
    completed = sum(1 for record in records if record["completed"])
    not_completed = total - completed
    total_amount = sum(record["amount"] for record in records)

    by_category = {}
    for record in records:
        category = record["category"].strip()
        by_category[category] = by_category.get(category, 0) + record["amount"]

    return {
        "total": total,
        "completed": completed,
        "not_completed": not_completed,
        "total_amount": total_amount,
        "by_category": by_category,
    }
