from functions import average, normalize_text, sum_digits, select_numbers


def main():
    # 1. Сумма цифр
    number = int(input("Целое число: "))
    print(f"Сумма цифр: {sum_digits(number)}")

    # 2. Среднее списка
    line = input("Целые числа через пробел: ")
    numbers = []
    for part in line.split():
        numbers.append(int(part))

    avg = average(numbers)
    if avg is None:
        print("Среднее: Нет данных")
    else:
        print(f"Среднее: {avg:.2f}")

    # 3. Нормализация текста
    text = input("Произвольный текст: ")
    print(f"Нормализованный текст: {normalize_text(text)}")

    # 4. Индивидуальный вариант
    threshold = int(input("Порог (целое >= 0): "))
    selected = select_numbers(numbers, threshold)
    print(f"Выборка по варианту: {selected}")


if __name__ == "__main__":
    main()
