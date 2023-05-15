import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

csv = pd.read_csv('ds_salaries.csv')
print(csv['work_year'])

sns.displot(csv['work_year'])
plt.show()

