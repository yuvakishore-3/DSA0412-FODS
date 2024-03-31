import numpy as np
from scipy import stats
group1_scores = [85, 88, 90, 91, 82, 87, 89, 86, 83, 92]
group2_scores = [78, 80, 75, 85, 79, 82, 81, 83, 77, 84]
mean_group1 = np.mean(group1_scores)
mean_group2 = np.mean(group2_scores)
sem_group1 = np.std(group1_scores) / np.sqrt(len(group1_scores))
sem_group2 = np.std(group2_scores) / np.sqrt(len(group2_scores))
ci_group1 = stats.t.interval(0.95, len(group1_scores)-1, loc=mean_group1, scale=sem_group1)
ci_group2 = stats.t.interval(0.95, len(group2_scores)-1, loc=mean_group2, scale=sem_group2)
t_stat, p_value = stats.ttest_ind(group1_scores, group2_scores)
print("Group 1 Mean Score:", mean_group1)
print("Group 1 95% Confidence Interval:", ci_group1)
print("Group 2 Mean Score:", mean_group2)
print("Group 2 95% Confidence Interval:", ci_group2)
print("Hypothesis Test Results:")
print("t-statistic:", t_stat)
print("p-value:", p_value)
if p_value < 0.05:
    print("There is a significant difference between the two groups.")
else:
    print("There is no significant difference between the two groups.")
