import numpy as np

salaries = [50000, 60000, 55000, 70000, 65000] # Create a list of salaries
#bonus_list = [s + 5000 for s in salaries] # Create a list of bonuses by adding 5000 to each salary
#print(bonus_list) # Print the list of bonuses
salaries_array = np.array(salaries) # Convert the list of salaries to a NumPy array
bonus_array = salaries_array + 5000 # Add 5000 to each element in the NumPy array to create a new array of bonuses
print(bonus_array) # Print the array of bonuses