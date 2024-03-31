from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import numpy as np
def get_car_data():
    car_data = load_iris()
    X = car_data.data
    y = car_data.target
    feature_names = car_data.feature_names
    target_names = car_data.target_names
    return X, y, feature_names, target_names
def get_user_input(feature_names):
    user_input = []
    print("Enter the features of the car:")
    for feature in feature_names:
        value = input(f"{feature}: ")
        user_input.append(float(value))
    return np.array(user_input).reshape(1, -1)
def predict_car_price(X_train, y_train, user_input):
    regressor = DecisionTreeRegressor()
    regressor.fit(X_train, y_train)
    predicted_price = regressor.predict(user_input)
    return predicted_price
def main():
    X, y, feature_names, _ = get_car_data()
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    user_input = get_user_input(feature_names)
    predicted_price = predict_car_price(X_train, y_train, user_input)
    print(f"Predicted price of the car: {predicted_price[0]}")
if __name__ == "__main__":
    main()
