import numpy
import matplotlib.pyplot as plt
from scipy import stats

# speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
#
# x = numpy.mean(speed) # Среднее арифметическое
# print(x)
#
# y = numpy.median(speed)  # Срединное значение (после сортировки от меньшего к большему)
# print(y)
#
# z = stats.mode(speed)  # Наиболее распространеное значение(количествро повторений)
# print(z)

# speed_a = [86, 87, 88, 86, 87, 85, 86]
# speed_b = [32, 111, 138, 28, 59, 77, 97]
#
# a = numpy.std(speed_a)
# a1 = numpy.mean(speed_a)
# b = numpy.std(speed_b)
# b1 = numpy.mean(speed_b)
# print(a)
# print('среднее значения', a1)
# print(b)
# print('среднее значения', b1)
#
#
# va = numpy.var(speed_a)
# vb = numpy.var(speed_b)
# print(va)
# print(vb)

# ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
# x = numpy.percentile(ages, 75)
# print(x)

# x = numpy.random.uniform(0.0, 5.0, 250)
# print(x)
# #
# plt.hist(x, 5)
# plt.show()

# x = numpy.random.normal(5.0, 1.0, 100000)
# print(x)
#
# plt.hist(x, 100)
# plt.show()

# xd = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
# yd = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
# plt.scatter(xd, yd)
# plt.show()

# x = numpy.random.normal(5.0, 1.0, 1000)
# y = numpy.random.normal(10.0, 2.0, 1000)
# plt.scatter(x, y)
# plt.show()
# #
# slope, intercept, r, p, std_err = stats.linregress(xd, yd)
# #
# #
# def my_func(x):
#     return  slope * x + intercept
#
#
# my_model = list(map(my_func, xd))
#
# plt.scatter(xd, yd)
# plt.plot(xd, my_model)
# plt.show()
#
# print(r)
# #
# speed = my_func(10)
# print(speed)
# #
x = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20, 26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
y = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def my_func(x):
    return slope * x + intercept


my_model = list(map(my_func, x))

plt.scatter(x, y)
plt.plot(x, my_model)
plt.show()

print(r)