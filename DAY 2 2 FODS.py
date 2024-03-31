import numpy as np
np.random.seed(0)
house_data = np.random.randint(1, 10, size=(100, 3))  
houses_more_than_4_bedrooms = house_data[house_data[:, 0] > 4]
average_sale_price = np.mean(houses_more_than_4_bedrooms[:, 2])  
print("Average sale price of houses with more than four bedrooms:", average_sale_price)
