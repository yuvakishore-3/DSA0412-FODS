likes_data = [10, 5, 15, 20, 10, 5, 10]
frequency_distribution = {}
for likes in likes_data:
    if likes in frequency_distribution:
        frequency_distribution[likes] += 1
    else:
        frequency_distribution[likes] = 1
print("Frequency Distribution of Likes:")
print("Likes\tFrequency")
for likes, frequency in sorted(frequency_distribution.items()):
    print(f"{likes}\t{frequency}")
