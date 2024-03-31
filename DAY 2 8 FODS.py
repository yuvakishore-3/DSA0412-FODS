import matplotlib.pyplot as plt
months = ['January', 'February', 'March', 'April', 'May']
sales_values = [10000, 12000, 15000, 18000, 200000]
plt.plot(months, sales_values, marker='o', linestyle='-')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales Value')
plt.xticks(rotation=45)
plt.grid(False)
plt.show()
plt.bar(months, sales_values, color='skyblue')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

