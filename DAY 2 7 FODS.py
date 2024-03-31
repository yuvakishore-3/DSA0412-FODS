import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['A', 'B', 'A', 'C', 'B'],
    'number_of_bedrooms': [3, 4, 2, 5, 3],
    'area_in_square_feet': [1500, 1800, 1200, 2200, 1600],
    'listing_price': [200000, 250000, 180000, 300000, 220000]
}
property_data = pd.DataFrame(data)
average_price_per_location = property_data.groupby('location')['listing_price'].mean()
num_properties_more_than_4_bedrooms = (property_data['number_of_bedrooms'] > 4).sum()
property_with_largest_area = property_data.loc[property_data['area_in_square_feet'].idxmax()]
print("Average listing price of properties in each location:")
print(average_price_per_location)
print("\nNumber of properties with more than four bedrooms:", num_properties_more_than_4_bedrooms)
print("\nProperty with the largest area:")
print(property_with_largest_area)
