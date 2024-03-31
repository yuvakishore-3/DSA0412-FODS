import numpy as np
from scipy import stats
conversion_rate_design_A = [0, 1, 0, 1, 1, 1, 0, 0, 0, 1]  
conversion_rate_design_B = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]  
t_statistic, p_value = stats.ttest_ind(conversion_rate_design_A, conversion_rate_design_B)
alpha = 0.05
if p_value < alpha:
    print("There is a statistically significant difference between the mean conversion rates (p < 0.05).")
else:
    print("There is no statistically significant difference between the mean conversion rates (p >= 0.05).")
