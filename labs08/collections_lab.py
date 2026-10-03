def word_counts(text):
    """Словарь «слово → количество».
    Нижний регистр, разбиение по пробелам, удаление .,!?;: по краям."""
    result = {}
    for word in text.lower().split():
        cleaned = word.strip(".,!?;:")
        if cleaned == "":
            continue
        result[cleaned] = result.get(cleaned, 0) + 1
    return result


def print_counts(counts):
    """Выводит пары по алфавиту."""
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    """Отсортированный список общих тем."""
    return sorted(set(first) & set(second))


def all_topics(first, second):
    """Отсортированный список всех уникальных тем."""
    return sorted(set(first) | set(second))


def totals_by_category(records):
    """Словарь сумм amount по категориям."""
    result = {}
    for record in records:
        category = record["category"]
        result[category] = result.get(category, 0) + record["amount"]
    return result


def titles_in_category(records, category):
    """Названия записей в исходном порядке для данной категории."""
    result = []
    for record in records:
        if record["category"] == category:
            result.append(record["title"])
    return result


def main():
    # 1. Частоты слов
    text = input("Введите текст: ")
    counts = word_counts(text)
    print("Частоты слов:")
    print_counts(counts)

    # 2. Темы
    first = input("Темы первого списка (через пробел): ").split()
    second = input("Темы второго списка (через пробел): ").split()
    print(f"Общие темы: {common_topics(first, second)}")
    print(f"Все темы: {all_topics(first, second)}")

    # 3. Запись и пара
    record = {"title": "Python", "hours": 4}
    record["hours"] = 6                 
    record["completed"] = False         
    print(f"Запись: {record}")

    pair = (record["title"], record["hours"])
    name, hours = pair
    print(f"Пара: {name}, {hours}")

    # 4. Индивидуальный вариант
    records = [
        {"title": "A", "category": "основное", "amount": 4},
        {"title": "B", "category": "дополнительное", "amount": 2},
        {"title": "C", "category": "основное", "amount": 3},
    ]
    totals = totals_by_category(records)
    print("Сводка по категориям:")
    for category in sorted(totals):
        print(f"  {category}: {totals[category]}")

    category = input("Введите категорию: ")
    titles = titles_in_category(records, category)
    print(f"Названия: {titles}")


if __name__ == "__main__":
    main()
