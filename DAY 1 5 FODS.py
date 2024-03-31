import pandas as pd
customer_demographics_df = pd.read_csv("customer_demographics.csv")
user_activity_logs_df = pd.read_csv("user_activity_logs.csv")
customer_support_df = pd.read_csv("customer_support.csv")
merged_df = pd.merge(customer_demographics_df, user_activity_logs_df, on="customer_id", how="left")
merged_df = pd.merge(merged_df, customer_support_df, on="customer_id", how="left")
print("Merged Dataset:")
print(merged_df.head())
merged_df.to_csv("consolidated_dataset.csv", index=False)
