import json


def load_records(path):
    """Прочитать JSON. Возвращает список.
    FileNotFoundError — файла нет.
    ValueError — ошибка формата (JSONDecodeError — подкласс).
    UnicodeError — не UTF-8.
    OSError — доступ."""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("Корень JSON должен быть списком")
    return data


def save_records(path, records):
    """Записать список в JSON UTF-8. При ошибке — OSError."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
