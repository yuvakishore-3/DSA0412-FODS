import pandas as pd
order_data = pd.DataFrame({
    'customer_id': [1, 2, 3, 1, 2],
    'order_date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-01', '2024-01-02'],
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B'],
    'order_quantity': [5, 3, 2, 4, 6]
})

orders_per_customer = order_data.groupby('customer_id').size()
avg_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()
print("Total number of orders made by each customer:\n", orders_per_customer)
print("\nAverage order quantity for each product:\n", avg_order_quantity_per_product)
print("\nEarliest Order Date:", earliest_order_date)
print("Latest Order Date:", latest_order_date)
