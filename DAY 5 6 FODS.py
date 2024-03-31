import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['Location A', 'Location B', 'Location A', 'Location C', 'Location B'],
    'num_bedrooms': [3, 4, 5, 3, 4],
    'area_sq_ft': [1500, 1800, 2200, 1350, 2000],
    'listing_price': [250000, 300000, 350000, 275000, 320000]
}
property_data = pd.DataFrame(data)
average_price_by_location = property_data.groupby('location')['listing_price'].mean()
print("Average Listing Price by Location:")
print(average_price_by_location)
num_properties_more_than_four_bedrooms = property_data[property_data['num_bedrooms'] > 4].shape[0]
print("\nNumber of Properties with More than Four Bedrooms:", num_properties_more_than_four_bedrooms)
property_with_largest_area = property_data[property_data['area_sq_ft'] == property_data['area_sq_ft'].max()]
print("\nProperty with the Largest Area:")
print(property_with_largest_area)
