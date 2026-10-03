from collections_lab import (
    word_counts,
    common_topics,
    all_topics,
    totals_by_category,
    titles_in_category,
)

assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}
assert word_counts("") == {}
assert word_counts("A a A!") == {"a": 3}
assert word_counts("один, два; три.") == {"один": 1, "два": 1, "три": 1}

assert common_topics(["python", "sql", "python"], ["sql", "git"]) == ["sql"]
assert all_topics(["python", "sql", "python"], ["sql", "git"]) == ["git", "python", "sql"]

assert common_topics([], ["sql", "git"]) == []
assert all_topics([], ["sql", "git"]) == ["git", "sql"]

assert common_topics([], []) == []
assert all_topics([], []) == []

records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]

assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
assert titles_in_category(records, "основное") == ["A", "C"]
assert titles_in_category(records, "нет") == []
assert totals_by_category([]) == {}
assert titles_in_category([], "основное") == []

saved = [record.copy() for record in records]
totals_by_category(records)
titles_in_category(records, "основное")
assert records == saved

record = {"title": "Python", "hours": 4}
record["hours"] = 6
record["completed"] = False
assert record == {"title": "Python", "hours": 6, "completed": False}

pair = (record["title"], record["hours"])
name, hours = pair
assert name == "Python"
assert hours == 6

print("Все проверки пройдены")
