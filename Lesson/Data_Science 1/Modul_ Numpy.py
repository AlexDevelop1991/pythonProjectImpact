import numpy as np
from numpy import random

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
#
# print(arr)
#
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
#
# print(arr2)
#
# arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#
# print(arr3)
# print('2nd element on 1st row', arr3[0, 1])
# print('last element from 2nd dim: ', arr3[1, -1])
# print(arr[1:5])
# print(arr[-3:-1])
# print(arr[1:5:2])
#
# # Сложение
# arrr = np.array([1, 2, 3])
# arrr2 = np.array([4, 5, 6])
# total = np.concatenate((arrr, arrr2))
# print(total)
#
# # Разделение
# array1 = np.array([1, 2, 3, 4, 5, 6])
# new_array = np.array_split(array1, 3)
# print(new_array)
# print(new_array[0])
# print(new_array[1])
# print(new_array[2])


# Поиск( выдает их индекс)
# masiv = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(masiv == 4)
# print(x)

# Генерация случайного числа
x = random.randint(100)
print(x)
y = random.rand()
print(y)
z = random.randint(100, size=(5))
print(z)
a = random.rand(5)
print(a)
b = random.choice([3, 5, 7, 9])
print(b)
w = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(w)
