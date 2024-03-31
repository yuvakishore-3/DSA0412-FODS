weather_data = {
    "Sunny": 120,
    "Rainy": 80,
    "Cloudy": 100,
    "Snowy": 40,
}
most_common_weather = max(weather_data, key=weather_data.get)
most_common_count = weather_data[most_common_weather]
print(f"Most common weather: {most_common_weather} ({most_common_count} days)")
