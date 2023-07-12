import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = pd.read_csv('https://raw.githubusercontent.com/amankharwal/Website-data/master/IRIS.csv')
# Splitting the dataset
x = iris.drop('species', axis=1)
y = iris['species']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Training the model
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train, y_train)
# Giving inputs to the machine learning model
# features = [[sepal_length, sepal_width, petal_length, petal_width]]
features = np.array([[5, 2.9, 1, 0.2]])
# Using inputs to predict the output
prediction = knn.predict(features)
print(f"Prediction: {prediction}")



