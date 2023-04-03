# Создать функцию и задать два параметра
def merge_list_to_dict(my_list, new_list):
    # В функии должна быть встроенная функция ZIP для объединения двух списков
    total_list = zip(my_list, new_list)
    # Конвертируй объект ZIP в словарь
    total_list = dict(total_list)
    # Вернуть из функции
    return total_list
# Вызвать функцию передав ей в качестве аргумента два списка
my_list = ['Orange', 'Kiwi']
new_list = [35, 40]
# total_list = (my_list, new_list)
total_list = merge_list_to_dict(my_list, new_list)
# Вывести результат вызова функции в терминал
print(total_list)
