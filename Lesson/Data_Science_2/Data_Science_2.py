import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Part 1
print(matplotlib.__version__)

# Part 2
x_points = np.array([0, 6])
y_points = np.array([0, 250])

plt.plot(x_points, y_points)
plt.show()

# Part 3
x_points = np.array([1, 8])
y_points = np.array([3, 10])

plt.plot(x_points, y_points)
plt.show()

# Part 4
x_points = np.array([1, 8])
y_points = np.array([3, 10])

plt.plot(x_points, y_points, 'o')
plt.show()

# Part 5
x_points = np.array([1, 2, 6, 8])
y_points = np.array([3, 8, 1, 10])

plt.plot(x_points, y_points)
plt.show()

# Part 6
plt.plot(y_points, marker='o')
plt.show()

# Part 7
plt.plot(y_points, color='r', marker='o')
plt.show()

# Part 8
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

# Part 9
x1 = np.array([3, 1, 2, 0])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

# Part 10
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel('Average Pulse')
plt.ylim('Calorie Burnage')

plt.show()

# Part 11
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title('Sports Watch Data')
plt.xlabel('Average Pulse')
plt.ylabel('Calorie Burnage')

plt.show()

# Part 11
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.show(x, y)

plt.title('Sports Watch Data')
plt.xlabel('Average Pulse')
plt.ylabel('Calorie Burnage')

plt.grid()
plt.show()

# Part 12
# Plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)

# Plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)

plt.show()

# Part 13
# Plot 1:
x = np. array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x, y)

# Plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt. plot(x, y)

plt.show()

# Part 14
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 11, 86, 103, 87, 94, 78, 77, 85, 86])

plt.scatter(x, y)
plt.show()

# Part 15
# Day one, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 11, 86, 103, 87, 94, 78, 77, 85, 86])

plt.scatter(x, y)

# Day two,the age and speed of 15 cars:
x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])

plt.scatter(x, y)
plt.show()

# Part 16
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 11, 86, 103, 87, 94, 78, 77, 85, 86])

plt.scatter(x, y, color= 'hotpink')

x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])

plt.scatter(x, y, color='#88c999')

plt.show()

# Part 17
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 11, 86, 103, 87, 94, 78, 77, 85, 86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')
plt.show()

# Part 18
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 11, 86, 103, 87, 94, 78, 77, 85, 86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap= 'viridis')
plt.colorbar()
plt.show()

# Part 19
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 11, 86, 103, 87, 94, 78, 77, 85, 86])
sizes = np.array([20, 50, 100, 200, 500 ,1000, 60, 90, 10, 300, 600, 800, 75])

plt.scatter(x, y, s=sizes)
plt.show()

# Part 20
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 11, 86, 103, 87, 94, 78, 77, 85, 86])
sizes = np.array([20, 50, 100, 200, 500 ,1000, 60, 90, 10, 300, 600, 800, 75])

plt.scatter(x, y, s=sizes, alpha=0.5)
plt.show()

# Part 21
x = np.random.randint(100, size=100)
y = np.random.randint(100, size=100)
colors = np.random.randint(100, size=100)
size = 10 * np.random.randint(100, size=100)

plt.scatter(x, y, c=colors, s=size, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.show()

# Part 22
x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.show()

# Part 23
x = np.random.normal(170, 10, 250)
print(x)

# Part 24
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()

# Part 25
y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show()

# Part 25
y = np.array([35, 25, 25, 15])
my_labels = ['Apples', 'Bananas', 'Cherries', 'Dates']

plt.pie(y, labels=my_labels)
plt.show()

# Part 26
y = np.array([35, 25, 25, 15])
my_labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
my_explode = [0.2, 0, 0, 0]

plt.pie(y, labels=my_labels, explode=my_explode)
plt.show()

# Part 26
y = np.array([35, 25, 25, 15])
my_labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
my_explode = [0.2, 0, 0, 0]

plt.pie(y, labels=my_labels, explode=my_explode, shadow=True)
plt.show()


