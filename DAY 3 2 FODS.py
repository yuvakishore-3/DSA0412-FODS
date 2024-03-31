import numpy as np
from scipy.stats import skew, kurtosis
def asymmetry_measure(data):
    skewness = skew(data)
    kurt = kurtosis(data)
    tail_behavior = np.percentile(data, 95) - np.percentile(data, 5)  # Using the 95th and 5th percentiles
    asymmetry = (skewness + kurt + tail_behavior) / 3   
    return asymmetry
gene_expression_data = np.random.normal(loc=0, scale=1, size=1000)  # Example gene expression data
asymmetry_score = asymmetry_measure(gene_expression_data)
print("Asymmetry Score:", asymmetry_score)
