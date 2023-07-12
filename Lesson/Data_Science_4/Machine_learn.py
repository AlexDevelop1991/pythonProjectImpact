import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Part 1
data = pd.read_csv('https://raw.githubusercontent.com/amankharwal/Website-data/master/dataset.csv')
print(data.head())
print(data.columns)

languages = []
for lang in data['language']:
    languages.append(lang)

print(set(languages))
print(len(set(languages)))

# Part 2
print(data.isnull().sum())

# Part 3
x = np.array(data['Text'])
y = np.array(data['language'])

cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))

user = input('Enter a Text: ')
data = cv.transform([user]).toarray()
output = model.predict(data)
print(output)