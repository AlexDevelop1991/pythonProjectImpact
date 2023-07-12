import matplotlib.pyplot as plt
import numpy as np


# Круговая диаграмма
time = np.array([49, 35, 14, 7, 4])
my_labels = ['Sleep', 'Work', 'Studies', 'Sport', 'Hobby']
my_explode = [0.1, 0, 0, 0, 0]
plt.title('Weekly Report')

def absolute_value(val):
    a = np.round(val/100 * time.sum())
    return a


plt.pie(time, labels=my_labels, explode=my_explode, shadow=True, autopct=absolute_value)
plt.show()