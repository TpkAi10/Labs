
first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")


print()
print("До обмена:")
print(f"first_room  = {first_room}")
print(f"second_room = {second_room}")


temp = first_room
first_room = second_room
second_room = temp


print()
print("После обмена:")
print(f"first_room  = {first_room}")
print(f"second_room = {second_room}")
