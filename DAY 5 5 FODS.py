import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
X = np.array([[100, 12, 2], [200, 24, 1], [50, 6, 3], [300, 36, 2], [150, 18, 1]])
y = np.array([0, 1, 0, 1, 0])
model = LogisticRegression()
model.fit(X, y)
def get_input_features():
    usage_minutes = float(input("Enter usage minutes: "))
    contract_duration = int(input("Enter contract duration (in months): "))
    monthly_charge = float(input("Enter monthly charge: "))
    return np.array([[usage_minutes, contract_duration, monthly_charge]])
new_customer_features = get_input_features()
prediction = model.predict(new_customer_features)
if prediction == 0:
    print("The new customer is predicted to not churn.")
else:
    print("The new customer is predicted to churn.")
