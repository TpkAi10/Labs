import json
from pathlib import Path
from tempfile import TemporaryDirectory
from storage import load_records, save_records


with TemporaryDirectory() as directory:
    path = Path(directory) / "data.json"

    # --- Файла нет ---
    try:
        load_records(path)
    except FileNotFoundError:
        pass
    else:
        assert False, "FileNotFoundError не возник"

    # --- Сохранение и чтение ---
    records = [
        {"id": 1, "title": "A", "category": "учёба", "amount": 4, "completed": False},
    ]
    save_records(path, records)
    restored = load_records(path)
    assert restored == records

    # --- Пустой список ---
    save_records(path, [])
    assert load_records(path) == []

    # --- Повреждённый JSON ---
    path.write_text("{не json}", encoding="utf-8")
    try:
        load_records(path)
    except ValueError:
        pass
    else:
        assert False, "ValueError не возник"

    # --- Корень не список ---
    path.write_text('{"id": 1}', encoding="utf-8")
    try:
        load_records(path)
    except ValueError:
        pass
    else:
        assert False, "ValueError не возник"

print("Все проверки storage пройдены")
