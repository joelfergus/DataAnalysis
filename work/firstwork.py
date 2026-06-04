import numpy as np
sales =np.array([320000, 415000, 280000, 510000, 390000, 460000]) #numpy array
print(f"Total Sales:        ${format(sales.sum())}")
print(f"Average Sales:      ${format(sales.mean())}")
print(f"Highest Sales:      ${format(sales.max())}")
print(f"Lowest Sales:       ${format(sales.min())}")
print(f"5% increase:       ${format(sales * 0.05)}")
