import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"],
    "department": ["HR", "IT", "Finance", "Finance", "HR", "IT", "Finance", "Finance", "HR", "IT"],
    "salary": [50000, 100000, 50000, 60000, 55000, 70000, 55000, 65000, 58000, 72000],
    "age": [25, 30, 35, 28, 32, 29, 27, 31, 33, 26]
}

df = pd.DataFrame(data)

High_earners = df[df["salary"] > 65000] # Filter the DataFrame to include only rows where the salary is above the average salary
print(High_earners)

ITHigh_earners = df[(df["department"] == "IT") & (df["salary"] > 65000)] # Filter the DataFrame to include only rows where the department is IT and the salary is above the average salary
print(ITHigh_earners)


ITorFinance = df[(df["department"] == "IT") | (df["department"] == "Finance")] # Filter the DataFrame to include only rows where the department is either IT or Finance
print(ITorFinance)

print("------------THIS IS FOR TEXT FILTERING------------------")
ITtext = df[df["department"].str.contains("IT")]
print(ITtext)

print("             -------This is for Not------               ")
notHR = df[df["department"] != "HR"] # Filter the DataFrame to include only rows where the department is not HR
print(notHR)

print("-------This is for multiple values(ISIN FUNCTION)------")
HRandFinance =df[df["department"].isin(["HR", "Finance"])] # Filter the DataFrame to include only rows where the department is either HR or Finance
print(HRandFinance)
