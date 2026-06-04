import numpy as np

employee_data = np.array([
    [50000, 23, 4],
    [75000, 30, 8],
    [45000, 32, 9],
    [155000, 53, 4],
    [35000, 23, 2],
    [45000, 25, 6],
    [25000, 35, 1],
    [65000, 32, 2],
    [55000, 19, 3],
    [115000, 25, 7],
    [85000, 39, 5],
    [95000, 29, 2],
])

print(f"shape: {employee_data.shape}") # this prints out the shape of the array employee_data
print(f"rows: {employee_data.shape[0]}") # this prints out the number of rows in the array employee_data
print(f"columns: {employee_data.shape[1]}") # this prints out the number of columns in the array employee_data
print(f"the salary of employees are: {employee_data[:, 0]}")
print(f"the age of employees are: {employee_data[:, 1]}")
print(f"the years of experience of employees are: {employee_data[:, 2]}")

print("------------------useful array properties------------------")
print(employee_data.dtype) # this prints out the data type of the array employee_data
print(employee_data.size) # this prints out the total number of elements in the array employee_data 
print(employee_data.ndim) # this prints out the number of dimensions of the array employee_data
