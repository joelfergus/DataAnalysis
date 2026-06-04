import pandas as pd

df = pd.read_excel("employee.xlsx")

df["Monthly_Salary"] = df["SALARY"] / 12


def calculate_bonus(row):
    if row["DEPARTMENT"] == "FINANCE":
        return row["SALARY"] * 0.15
    elif row["DEPARTMENT"] == "IT":
        return row["SALARY"] * 0.12
    else:
        return row["SALARY"] * 0.10

df["bonus"] = df.apply(calculate_bonus, axis=1)

def seniority(salary):
    if salary >= 100000:
        return "Senior"
    elif salary >= 60000:
        return "Mid-level"
    else:
        return "Junior"

df["seniority"] = df["SALARY"].apply(seniority)

def performance_rating(performance):
    if performance >= 90:
        return "A"
    elif performance >= 80:
        return "B"
    elif performance >= 70:
        return "C"
    elif performance < 70:
         return "D"

df["performance_grade"] = df["PERFORMANCE"].apply(performance_rating)






print(df[["NAME", "Monthly_Salary", "bonus", "seniority", "performance_grade"]])


