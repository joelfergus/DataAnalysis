import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"],
    "department": ["HR", "IT", "Finance", "Finance", "HR", "IT", "Finance", "Finance", "HR", "IT"],
    "salary": [50000, 100000, 50000, 60000, 55000, 70000, 55000, 65000, 58000, 72000],
    "age": [25, 30, 35, 28, 32, 29, 27, 31, 33, 26]
}

df = pd.DataFrame(data)

df["bonus"] = df["salary"] * 0.1 # Create a new column "bonus" that is 10% of the "salary" column
df["total"] = df["bonus"] + df["salary"]

def rankingBySalary(salary):
    if salary >= 100000:
        return "Senior"
    elif salary >= 60000:
        return "Mid-level"
    else:
        return "Junior"

df["ranking"] = df["salary"].apply(rankingBySalary)
print(df)