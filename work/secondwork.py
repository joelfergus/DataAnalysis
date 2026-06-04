import pandas as pd

df = pd.read_excel("Book1.xlsx")

print(f"total number of employees {len(df)}")
print(f"number of columns {len(df.columns), list(df.columns)}")
print(f"average salary {df["SALARY"].mean()}")

print(f"highest age {df["AGE"].max()}")
print(f"lowest age {df["AGE"].min()}")
print(f"missing values {df.isnull().sum()}")