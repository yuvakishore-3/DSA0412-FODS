import pandas as pd
import numpy as np
from scipy.stats import t
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'brand': ['Brand X', 'Brand Y', 'Brand X', 'Brand Y', 'Brand Z'],
    'categories': ['Category A', 'Category B', 'Category A', 'Category B', 'Category A'],
    'reviews_rating': [4.5, 3.8, 4.2, 4.0, 4.7]
}
df = pd.DataFrame(data)
category = 'Category A'
category_df = df[df['categories'] == category]
sample_mean = category_df['reviews_rating'].mean()
sample_std = category_df['reviews_rating'].std()
n = len(category_df)
df = n - 1
confidence_level = 0.95
t_score = t.ppf((1 + confidence_level) / 2, df)
margin_of_error = t_score * (sample_std / np.sqrt(n))
lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error
print(f"Sample Mean: {sample_mean:.2f}")
print(f"Sample Standard Deviation: {sample_std:.2f}")
print(f"Sample Size: {n}")
print(f"Degrees of Freedom: {df}")
print(f"Confidence Level: {confidence_level}")
print(f"T-Score: {t_score:.2f}")
print(f"Margin of Error: {margin_of_error:.2f}")
print(f"Confidence Interval: ({lower_bound:.2f}, {upper_bound:.2f})")
