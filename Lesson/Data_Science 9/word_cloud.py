import  re
import string

import nltk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from wordcloud import WordCloud, STOPWORDS


data = pd.read_csv('https://raw.githubusercontent.com/amankharwal/Website-data/master/stress.csv')
print(data.head())
print(data.info())

nltk.download('stopwords')
stemmer = nltk.SnowballStemmer('english')
stopword = set(stopwords.words('english'))


def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\s+|www\.\s+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text = ' '.join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text = ' '.join(text)
    return text


data['text'] = data['text'].apply(clean)
text = ' '.join(i for i in data.text)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color='white').generate(text)
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

data['label'] = data['label'].map({0: 'No Stress', 1: 'Stress'})
data = data[['text', 'label']]
print(data.head())

x = np.array(data['text'])
y = np.array(data['label'])

cv = CountVectorizer()
X = cv.fit_transform(x)

xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.33, random_state=42)

model = BernoulliNB()
model.fit(xtrain, ytrain)

user = input('Enter a Text: ')
data = cv.transform([user]).toarray()
output = model.predict(data)
print(output)
