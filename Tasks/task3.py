# Список товаров
name_product = ['soap', 'cream', 'shampoo']
# Список цен товаров
price = [10, 15, 40]
# Объедите два списка с помощью ZIP
finally_prod_price = zip(name_product, price)
# Конвертировать в список
finally_prod_price = list(finally_prod_price)
# Вывод в терминал
print(finally_prod_price)
# Конвертировать в словарь
finally_prod_price = dict(finally_prod_price)
# Вывод в терминал
print(finally_prod_price)