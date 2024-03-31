import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
california_housing = fetch_california_housing()
X = california_housing.data
y = california_housing.target
selected_feature_index = 5
selected_feature_name = california_housing.feature_names[selected_feature_index]
X_selected = X[:, selected_feature_index].reshape(-1, 1)
plt.scatter(X_selected, y, alpha=0.5)
plt.title("Bivariate Analysis: {} vs House Price".format(selected_feature_name))
plt.xlabel(selected_feature_name)
plt.ylabel("House Price")
plt.show()
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Model Evaluation:")
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)
