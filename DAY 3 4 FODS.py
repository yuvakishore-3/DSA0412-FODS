import numpy as np
import matplotlib.pyplot as plt
scores = [85, 78, 92, 89, 67, 76, 94, 82, 91, 88, 75, 81, 96, 90, 79, 83, 77, 85, 98, 72]
mean_score = np.mean(scores)
median_score = np.median(scores)
quartiles = np.percentile(scores, [25, 50, 75])
lower_quartile, median_quartile, upper_quartile = quartiles
iqr = upper_quartile - lower_quartile
lower_bound = lower_quartile - 1.5 * iqr
upper_bound = upper_quartile + 1.5 * iqr
outliers = [score for score in scores if score < lower_bound or score > upper_bound]
plt.figure(figsize=(8, 6))
plt.boxplot(scores, vert=False)
plt.title('Distribution of Scores')
plt.xlabel('Scores')
plt.yticks([])
plt.grid(False)
plt.show()
print("Mean:", mean_score)
print("Median:", median_score)
print("Lower Quartile:", lower_quartile)
print("Median Quartile:", median_quartile)
print("Upper Quartile:", upper_quartile)
print("Potential outliers:", outliers)
