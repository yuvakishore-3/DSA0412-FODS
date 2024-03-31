import matplotlib.pyplot as plt
import numpy as np
time_spent = [8, 12, 5, 15, 10, 20, 7, 18, 25, 8, 12, 22, 15, 10, 30, 7, 18, 15, 20, 12]
plt.figure(figsize=(8, 6))
plt.boxplot(time_spent)
plt.title('Distribution of Time Spent on Website')
plt.xlabel('Time Spent (minutes)')
plt.ylabel('Frequency')
plt.grid(False)
plt.show()
