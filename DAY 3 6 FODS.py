weather_data = {
    'Sunny': 120,
    'Rainy': 75,
    'Cloudy': 90,
    'Snowy': 50,
    'Windy': 30
}
def most_common_weather(data):
    max_frequency = max(data.values())
    most_common_weather_types = [weather for weather, freq in data.items() if freq == max_frequency]
    return most_common_weather_types
def calculate_frequency_distribution(data):
    total_occurrences = sum(data.values())
    frequency_distribution = {weather: freq / total_occurrences for weather, freq in data.items()}
    return frequency_distribution
print("Frequency distribution of weather conditions:")
for weather, frequency in calculate_frequency_distribution(weather_data).items():
    print(f"{weather}: {frequency:.2f}")
most_common = most_common_weather(weather_data)
if len(most_common) == 1:
    print(f"The most common weather type is: {most_common[0]}")
else:
    print(f"The most common weather types are: {', '.join(most_common)}")
