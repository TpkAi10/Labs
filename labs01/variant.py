
order_name = input("Название заказа: ")
customer = input("Имя заказчика: ")


item1 = input("Название первой позиции: ")
qty1 = int(input(f"Количество «{item1}»: "))
price1 = float(input(f"Цена за единицу «{item1}» (руб): "))


item2 = input("Название второй позиции: ")
qty2 = int(input(f"Количество «{item2}»: "))
price2 = float(input(f"Цена за единицу «{item2}» (руб): "))


delivery = float(input("Стоимость доставки (руб): "))
discount_percent = float(input("Скидка в процентах от стоимости товаров (0–100): "))
paid = float(input("Внесённая сумма (руб): "))


cost1 = qty1 * price1
cost2 = qty2 * price2
goods_total = cost1 + cost2     
discount_rub = goods_total * discount_percent / 100
goods_after_discount = goods_total - discount_rub
total_with_delivery = goods_after_discount + delivery
total_qty = qty1 + qty2
change = paid - total_with_delivery


print()
print("=" * 55)
print(f"ЗАКАЗ: {order_name}")
print(f"Заказчик: {customer}")
print("=" * 55)
print(f"{item1} | {qty1} | {price1:.2f} | {cost1:.2f}")
print(f"{item2} | {qty2} | {price2:.2f} | {cost2:.2f}")
print("-" * 55)
print(f"Товары без доставки: {goods_total:.2f} руб.")
print(f"Скидка {discount_percent:.2f}%: {discount_rub:.2f} руб.")
print(f"Товары со скидкой: {goods_after_discount:.2f} руб.")
print(f"Доставка: {delivery:.2f} руб.")
print(f"Итого с доставкой: {total_with_delivery:.2f} руб.")
print(f"Общее количество единиц: {total_qty}")
print(f"Внесено: {paid:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
print("=" * 55)
