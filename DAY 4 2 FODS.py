import numpy as np
from scipy import stats
product_type_A = np.array([10, 12, 14, 16, 18])
product_type_B = np.array([11, 13, 15, 17, 19])
mean_A = np.mean(product_type_A)
mean_B = np.mean(product_type_B)
std_err_A = stats.sem(product_type_A)
std_err_B = stats.sem(product_type_B)
conf_interval_A = stats.t.interval(0.90, len(product_type_A)-1, loc=mean_A, scale=std_err_A)
conf_interval_B = stats.t.interval(0.90, len(product_type_B)-1, loc=mean_B, scale=std_err_B)
print("Product Type A:")
print(f"Mean Lifespan: {mean_A}")
print(f"90% Confidence Interval: {conf_interval_A}")
print("\nProduct Type B:")
print(f"Mean Lifespan: {mean_B}")
print(f"90% Confidence Interval: {conf_interval_B}")
t_stat, p_value = stats.ttest_ind(product_type_A, product_type_B)
alpha = 0.05 
print("\nHypothesis Test:")
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")
if p_value < alpha:
    print("Reject the null hypothesis: There is a statistically significant difference in lifespans.")
else:
    print("Fail to reject the null hypothesis: There is no statistically significant difference in lifespans.")
