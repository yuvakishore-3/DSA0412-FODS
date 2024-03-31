import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(0)
X = np.arange(1, 11)
Y = np.arange(2, 12) + np.random.normal(0, 1, 10)
df = pd.DataFrame({'X': X, 'Y': Y})
mean_X = df['X'].mean()
mean_Y = df['Y'].mean()
variance_X = df['X'].var()
variance_Y = df['Y'].var()
covariance = df[['X', 'Y']].cov().iloc[0, 1]
correlation = df[['X', 'Y']].corr().iloc[0, 1]
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='X', y='Y')
plt.title('Scatter Plot of X vs Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
print("Summary Statistics:")
print(f"Mean of X: {mean_X}")
print(f"Mean of Y: {mean_Y}")
print(f"Variance of X: {variance_X}")
print(f"Variance of Y: {variance_Y}")
print(f"Covariance between X and Y: {covariance}")
print(f"Correlation coefficient between X and Y: {correlation}")
