import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

data = pd.read_csv('https://raw.githubusercontent.com/amankharwal/Website-data/master/electricity.csv')
print(data.head())
print(data.info())

data['ForecastWindProduction'] = pd.to_numeric(data['ForecastWindProduction'], errors='coerce')
data['SystemLoadEA'] = pd.to_numeric(data['SystemLoadEA'], errors='coerce' )
data['SMPEA'] = pd.to_numeric(data['SMPEA'], errors='coerce')
data['ORKTemperature'] = pd.to_numeric(data['ORKTemperature'], errors='coerce')
data['ORKWindspeed'] = pd.to_numeric(data['ORKWindspeed'], errors='coerce')
data['CO2Intensity'] = pd.to_numeric(data['CO2Intensity'], errors='coerce')
data['ActualWindProduction'] = pd.to_numeric(data['ActualWindProduction'], errors='coerce')
data['SystemLoadEP2'] = pd.to_numeric(data['SystemLoadEP2'], errors='coerce')
data['SMPEP2'] = pd.to_numeric(data['SMPEP2'], errors='coerce')

print(data.isnull().sum())
data = data.dropna()

correlations = data.corr(method='pearson', numeric_only=True)
plt.figure(figsize=(16, 12))
sns.heatmap(correlations, cmap='coolwarm', annot=True)
plt.show()

x = data[['Day', 'Month', 'ForecastWindProduction', 'SystemLoadEA', 'SMPEA', 'ORKTemperature', 'ORKWindspeed',
          'CO2Intensity', 'ActualWindProduction', 'SystemLoadEP2']]
y = data['SMPEP2']

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(xtrain, ytrain)

features = np.array([[10, 12, 54.10, 4241.05, 49.56, 9.0, 14.8, 491.32, 54.0, 4426.84]])
model.predict(features)