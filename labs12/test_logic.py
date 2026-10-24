from logic import (
    validate_records,
    next_id,
    add_record,
    find_records,
    set_completed,
    delete_record,
    statistics,
)


# --- validate_records ---
sample = [
    {"id": 1, "title": "A", "category": "учёба", "amount": 4, "completed": False},
    {"id": 2, "title": "B", "category": "учёба", "amount": 2, "completed": True},
]
validate_records(sample)
validate_records([])


def expect_value_error(data):
    try:
        validate_records(data)
    except ValueError:
        pass
    else:
        assert False, "ValueError не возник"


expect_value_error({})
expect_value_error([1])
expect_value_error([{"id": 1, "title": "A", "category": "C", "amount": -1, "completed": False}])
expect_value_error([{"id": 1, "title": "A", "category": "C", "amount": 1, "completed": "false"}])
expect_value_error([{"id": True, "title": "A", "category": "C", "amount": 1, "completed": False}])
expect_value_error([
    {"id": 1, "title": "A", "category": "C", "amount": 1, "completed": False},
    {"id": 1, "title": "B", "category": "C", "amount": 1, "completed": False},
])

# --- next_id ---
assert next_id([]) == 1
assert next_id(sample) == 3
assert next_id([{"id": 5}]) == 6

# --- add_record ---
records = []
r1 = add_record(records, "  Python  ", "  учёба  ", 4)
assert r1 == {"id": 1, "title": "Python", "category": "учёба", "amount": 4, "completed": False}
r2 = add_record(records, "SQL", "учёба", 2)
assert r2["id"] == 2
assert len(records) == 2

# --- find_records ---
assert [r["id"] for r in find_records(records, "PY")] == [1]
assert [r["id"] for r in find_records(records, "python")] == [1]
assert find_records(records, "zzz") == []
try:
    find_records(records, "   ")
except ValueError:
    pass
else:
    assert False, "ValueError не возник"

# --- set_completed ---
assert set_completed(records, 1, True) is True
assert records[0]["completed"] is True
assert set_completed(records, 999, True) is False

# --- delete_record ---
assert delete_record(records, 1) is True
assert len(records) == 1
assert records[0]["id"] == 2
assert delete_record(records, 999) is False

# --- statistics ---
stats = statistics(sample)
assert stats["total"] == 2
assert stats["completed"] == 1
assert stats["not_completed"] == 1
assert stats["total_amount"] == 6
assert stats["by_category"] == {"учёба": 6}

empty_stats = statistics([])
assert empty_stats["total"] == 0
assert empty_stats["total_amount"] == 0
assert empty_stats["by_category"] == {}

print("Все проверки logic пройдены")
