import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"],
    "department": ["HR", "IT", "Finance", "Finance", "HR", "IT", "Finance", "Finance", "HR", "IT"],
    "salary": [50000, 100000, 50000, 60000, 55000, 70000, 55000, 65000, 58000, 72000],
    "age": [25, 30, 35, 28, 32, 29, 27, 31, 33, 26]
}

df = pd.DataFrame(data)

highestToLowest = df.sort_values(by="salary", ascending=False) # Sort the DataFrame by the "salary" column in descending order
print(highestToLowest)