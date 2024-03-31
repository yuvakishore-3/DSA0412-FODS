import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
np.random.seed(0)
control_group = np.random.normal(loc=50, scale=10, size=100)
treatment_group = np.random.normal(loc=55, scale=10, size=100)
t_stat, p_value = stats.ttest_ind(treatment_group, control_group)
plt.hist(control_group, alpha=0.5, label='Control Group')
plt.hist(treatment_group, alpha=0.5, label='Treatment Group')
plt.xlabel('Measurement')
plt.ylabel('Frequency')
plt.legend()
plt.title('Distribution of Measurements')
plt.text(40, 20, f'p-value = {p_value:.4f}', fontsize=12)
plt.show()
print("P-value:", p_value)
