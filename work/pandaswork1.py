import pandas as pd

df = pd.read_excel("employee.xlsx")

print(f"columns: {list(df.columns)}")

high_earners = df[df['SALARY'] > 70000]
print(f"employees earning more than 70000: \n {high_earners }")

print(f"female employees: \n {df[df['GENDER'] == 'F']}")

print(f"employees in lagos or abuja earning over 60000: \n {df[(df['LOCATION'].isin(['LAGOS', 'ABUJA'])) & (df['SALARY'] > 60000)]}")

high_performers = df[df["PERFORMANCE"] > 85]
print(f"high performers: \n {high_performers[['NAME', 'DEPARTMENT', 'SALARY']]}")
