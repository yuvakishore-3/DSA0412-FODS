import numpy as np
from sklearn.cluster import KMeans
customer_ids = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
total_spent = [150, 200, 50, 300, 100, 250, 80, 400, 180, 350]
visit_frequency = [5, 3, 8, 2, 6, 4, 7, 3, 5, 2]
X = np.array(list(zip(total_spent, visit_frequency)))
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(X)
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_
print("Cluster Centers:")
print(cluster_centers)
print("\nCluster Labels:")
print(labels)
customer_clusters = {}
for i, customer_id in enumerate(customer_ids):
    customer_clusters[customer_id] = labels[i]
print("\nCustomer Clusters:")
for customer_id, cluster in customer_clusters.items():
    print(f"Customer ID: {customer_id}, Cluster: {cluster}")
