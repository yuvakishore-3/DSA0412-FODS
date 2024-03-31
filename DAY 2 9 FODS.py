import matplotlib.pyplot as plt
def plot_temperature(months, temperatures):
    plt.plot(months, temperatures, marker='o', color='b')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.title('Monthly Temperature Variation')
    plt.grid(True)
    plt.show()
def plot_rainfall(months, rainfall):
    plt.scatter(months, rainfall, marker='o', color='r')
    plt.xlabel('Month')
    plt.ylabel('Rainfall (mm)')
    plt.title('Monthly Rainfall Variation')
    plt.grid(True)
    plt.show()
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperatures = [25, 28, 30, 32, 34, 33, 31, 30, 29, 28, 26, 24]
rainfall = [50, 40, 60, 70, 80, 90, 100, 110, 100, 80, 60, 50]
plot_temperature(months, temperatures)
plot_rainfall(months, rainfall)
