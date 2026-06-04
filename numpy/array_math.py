import numpy as np

salary = np.array([50000, 60000, 55000, 70000, 65000, 60000, 30000, 100000]) # Create a NumPy array of salaries
print(f"Total Payroll:       ${salary.sum()}")
print(f"Average Salary:      ${salary.mean()}")
print(f"Highest Salary:      ${salary.max()}")
print(f"Lowest Salary:       ${salary.min()}")
print(f"standard deviation:  ${salary.std()}")
print(f"median salary:       ${np.median(salary)}")

print("this is for bonus")
bonus = salary * 0.10 # Calculate a 10% bonus for each salary
total_package = salary + bonus # Calculate the total package by adding the bonus to the original salary
print(f"bonuses: {bonus}")
print(f"total packages: {total_package}")