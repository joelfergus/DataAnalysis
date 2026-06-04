import numpy as np


revenue = np.array([
    [120000, 135000, 98000, 160000],
    [200000, 185000, 210000, 225000],
    [75000, 82000, 79000, 95000],
    [310000, 290000, 325000, 340000]
    ])
print(revenue.shape)
print(f"total revenue per product: {revenue.sum(axis=0)}")
print(f"best quarter overall: {revenue.sum(axis=1).max()}")
print(f"75th percentile of revenue: {np.percentile(revenue, 75)}")
