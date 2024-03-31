import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.datasets import load_iris  # You can replace this with any other dataset
from sklearn.linear_model import LogisticRegression  # You can replace this with any other model
def main():
    dataset = load_iris()  # Example dataset
    X = dataset.data
    y = dataset.target
    print("Available features:", dataset.feature_names)
    features_input = input("Enter names of features (separated by comma): ").strip().split(',')
    feature_indices = [dataset.feature_names.index(feature.strip()) for feature in features_input]
    print("Available target variable:", dataset.target_names)
    target_variable = input("Enter name of the target variable: ").strip()
    X_train, X_test, y_train, y_test = train_test_split(X[:, feature_indices], y, test_size=0.2, random_state=42)
    model = LogisticRegression()  # Example model
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    print("\nEvaluation Metrics:")
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)
if __name__ == "__main__":
    main()
