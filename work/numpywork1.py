import numpy as np
sales =np.array([320000, 415000, 280000, 510000, 390000, 460000])
average_sales = sales.mean()
print(f"branches that exceeded 400000:           {sales[sales > 400000]}")
print(f"branches with sales below average:       {sales[sales < average_sales]}")
print(f"percentage of branches exceeding 400000: {np.sum(sales > 400000) / sales.size * 100}%")
