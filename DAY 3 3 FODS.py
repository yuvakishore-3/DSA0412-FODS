import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
exam_scores = np.random.randint(40, 101, size=50)
plt.figure(figsize=(8, 6))
plt.hist(exam_scores, bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Exam Scores')
plt.xlabel('Exam Scores')
plt.ylabel('Frequency')
plt.grid(False)
plt.show()
