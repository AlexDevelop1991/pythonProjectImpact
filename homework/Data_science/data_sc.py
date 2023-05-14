import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# Круговая диаграмма
time = np.array([37, 54, 16])
my_labels = ['Work', 'Sleep', 'Computer']
my_explode = [0, 0.2, 0]
plt.title('Weekly Report')

def absolute_value(val):
    a = np.round(val/100 * time.sum())
    return a


plt.pie(time, labels=my_labels, explode=my_explode, shadow=True, autopct=absolute_value)
plt.show()

# Гистограмма
work = np.array([8, 7, 8, 6, 8, 0, 0])

plt.title('Weekly Work')
plt.xlabel('Time(hours)')
plt.ylabel('Quantity')
plt.hist(work)
plt.show()

sleep = np.array([8, 6, 9, 6, 8, 7, 10])

plt.title('Weekly Sleep')
plt.xlabel('Time(hours)')
plt.ylabel('Quantity')
plt.hist(sleep)
plt.show()

computer = np.array([2, 1, 4, 3, 2, 3, 1])

plt.title('Weekly Computer')
plt.xlabel('Time(hours)')
plt.ylabel('Quantity')
plt.hist(computer)
plt.show()





