import matplotlib.pyplot as plt
months = range(1, 13)
sales = [100, 120, 150, 130, 160, 180, 200, 220, 240, 260, 280, 300]
plt.plot(months, sales, marker='o')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Product Sales Over Time')
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt
months = range(1, 13)
sales = [100, 120, 150, 130, 160, 180, 200, 220, 240, 260, 280, 300]
plt.scatter(months, sales, color='blue')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Sales Prediction')
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [100, 120, 150, 130, 160, 180, 200, 220, 240, 260, 280, 300]
plt.bar(months, sales, color='green')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')
plt.grid(True)
plt.show()


