import numpy as np

sales = np.array([50000, 60000, 55000, 70000, 65000, 60000, 30000, 100000])
print(np.sort(sales))
print(np.sort(sales)[::-1]) # this sorts the sales array in descending order

print(np.percentile(sales, 25)) # this calculates the 25th percentile of the sales array
print(np.percentile(sales, 50)) # this calculates the 50th percentile of the sales array
print(np.percentile(sales, 75)) # this calculates the 75th percentile of the sales array
average_sales = sales.mean() # this calculates the average of the sales array
print(average_sales) # this prints the average of the sales array
high_sales = np.where(sales > average_sales) # this finds the indices of the sales that are above the average
print(high_sales) 
print(sales[high_sales]) # this prints the sales that are above the average
departments = np.array(["HR", "Finance", "IT", "Marketing", "HR", "IT", "HR", "IT"])
print(np.unique(departments)) # this prints the unique values in the departments array)