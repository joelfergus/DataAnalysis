import numpy as np
salary = np.array([50000, 60000, 55000, 70000, 65000, 60000, 30000, 100000]) # Create a NumPy array of salaries
average_salary = salary.mean() # Calculate the average salary
high_earners = salary[salary > average_salary] # Filter the salaries to include only those above the average
low_earners = salary[salary < average_salary] # Filter the salaries to include only those below the average 
print(f"Average Salary: ${average_salary}")
print(f"The above average salaries are: ${high_earners}")
print(f"The below average salaries are: ${low_earners}")