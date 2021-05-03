price_list = [87.0, 90.87, 34.76, 12, 34, 65, 98.87, 65.9, 45.78, .6, 12.34, 43.3, 6.8, 43.86, 85.8]
price_list_new = []
for i in price_list:
    i = str(float(i))
    i = f'{int(i.split(".")[0]):02d} руб. {int(i.split(".")[-1]):02d} коп.'
    price_list_new.append(i)
# Цены через запятую на экран
print(','.join(price_list_new))
# Цены по возрастанию
print(id(price_list_new)) #проверка id
price_list_new.sort()
print(price_list_new)
print(id(price_list_new)) #проверяем что id не изменился
# новый список отсортированный по убыванию
price_list_desc = list(reversed(price_list_new))
print(price_list_desc)
# Вывести цены пяти самых дорогих товаров
print(price_list_new[len(price_list_new) - 5:])
