import numpy as np
house_data = np.array([
    [3, 1500, 200000],
    [2, 1200, 150000],
    [4, 2000, 300000],
    [5, 2500, 350000],
])
weather_data = np.array([
    [10, 50],  
    [15, 60],
    [20, 70],
    [25, 65],
])
filtered_data = house_data[house_data[:, 0] > 4]
average_price = np.mean(filtered_data[:, 2])
correlation_matrix = np.corrcoef(weather_data.T)
print("Correlation matrix for weather data:")
print(correlation_matrix)
print("Average sale price for houses with more than 4 bedrooms:", average_price)
