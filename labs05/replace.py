text = input("Введите текст: ")

count = text.count(":")

new_text = text.replace(":", "-")

print(f"Замен: {count}")
print(f"Новая строка: {new_text}")
