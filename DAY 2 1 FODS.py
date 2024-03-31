import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
dates = pd.date_range('2020-01-01', '2024-12-31', freq='D')
temperature = np.random.normal(loc=20, scale=5, size=len(dates))
precipitation = np.random.exponential(scale=2, size=len(dates))
weather_data = pd.DataFrame({'Date': dates, 'Temperature': temperature, 'Precipitation': precipitation})
weather_data['Month'] = weather_data['Date'].dt.month
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'
weather_data['Season'] = weather_data['Month'].apply(get_season)
seasonal_avg_temp = weather_data.groupby(['Season', 'Month'])['Temperature'].mean().unstack()
seasonal_avg_temp.plot(kind='line', marker='o')
plt.title('Average Temperature Trends Over Different Seasons')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(np.arange(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend(title='Season')
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))
plt.plot(weather_data['Date'], weather_data['Precipitation'], color='blue')
plt.title('Precipitation Over Time')
plt.xlabel('Date')
plt.ylabel('Precipitation')
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))
weather_data['Temperature'].plot(kind='hist', bins=30, color='skyblue', edgecolor='black')
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
