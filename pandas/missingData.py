import pandas as pd

data = {
    "name": ["Alice", "Bob", None, "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"],
    "department": ["HR", "IT", "Finance", None, "HR", "IT", "Finance", "Finance", "HR", "IT"],
    "salary": [None, 100000, 50000, 60000, 55000, 70000, 55000, 65000, 58000, 72000],
    "age": [25, None, 35, 28, 32, 29, 27, 31, 33, 26]
}

df = pd.DataFrame(data)
print(df.isnull().sum()) # Check for missing values in the DataFrame

print("------FULL DATASET------")
print(df)


print("------DROP MISSING VALUES------")
dropMissing = df.dropna() # Drop rows with missing values
print(dropMissing)  
print("------DROP MISSING NAME------")
print(df.dropna(subset=["name"])) # Drop rows with missing values in the "name" column
print("------FILL MISSING VALUES WITH AVERAGE VALUE------")
df["salary"] = df["salary"].fillna(df["salary"].mean()) # Fill missing values in the "salary" column with the average salary
print(df)



#use mean for salaries and age, and use "Unknown" for missing names and departments
#use median for age
#drop rows only when the whole row is useless