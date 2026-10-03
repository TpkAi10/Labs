text = input("Введите текст: ")

normalized = " ".join(text.split())

original_length = len(text)
new_length = len(normalized)

words = normalized.split()
word_count = len(words)

print()
print(f"Исходная длина: {original_length}")
print(f"Новая длина: {new_length}")
print(f"Нормализованный текст: {normalized}")
print(f"Количество слов: {word_count}")
