disease_data = {
    "Common Cold": 320,
    "Diabetes": 120,
    "Bronchitis": 100,
    "Influenza": 150,
    "Kidney Stones": 60
}
most_common_disease = max(disease_data, key=disease_data.get)
most_common_count = disease_data[most_common_disease]
print(f"The most common disease: {most_common_disease} ({most_common_count} diagnosed patients)")

