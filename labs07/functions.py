def sum_digits(number):
    """Вернуть сумму цифр модуля числа. Для нуля — 0."""
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


def average(numbers):
    """Вернуть среднее списка или None, если список пуст.
    Исходный список не изменяется."""
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Нижний регистр, без пробелов по краям, один пробел между словами."""
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    """Вариант 14: числа, кратные (threshold + 1).
    Порядок и повторы сохраняются, исходный список не меняется."""
    result = []
    for number in numbers:
        if number % (threshold + 1) == 0:
            result.append(number)
    return result
