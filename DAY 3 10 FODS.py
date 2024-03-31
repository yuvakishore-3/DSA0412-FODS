import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {'Age': [23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61],
        'BodyFatPercentage': [9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]}
df = pd.DataFrame(data)
age_stats = df['Age'].describe()
fat_stats = df['BodyFatPercentage'].describe()
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['Age'])
plt.title('Boxplot of Age')
plt.subplot(1, 2, 2)
sns.boxplot(y=df['BodyFatPercentage'])
plt.title('Boxplot of Body Fat Percentage')
plt.show()
plt.figure(figsize=(6, 6))
sns.scatterplot(x='Age', y='BodyFatPercentage', data=df)
plt.title('Scatter Plot of Age vs Body Fat Percentage')
plt.xlabel('Age')
plt.ylabel('Body Fat Percentage')
plt.show()
plt.figure(figsize=(6, 6))
sns.regplot(x='Age', y='BodyFatPercentage', data=df, fit_reg=True)
plt.title('Q-Q Plot of Age vs Body Fat Percentage')
plt.xlabel('Age')
plt.ylabel('Body Fat Percentage')
plt.show()
