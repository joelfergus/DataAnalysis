import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel("employee.xlsx")

salaries = df["SALARY"]

#calculates statistics
mean_salary = salaries.mean()
median_salary = salaries.median()

# creates the figure
plt.figure(figsize=(12, 8))

# creates the histogram
n, bins, patches = plt.hist(
    salaries,
    bins=10,
    color="skyblue",
    edgecolor="black",
    alpha=0.7,
    linewidth=0.8
)

# adds a vertical line for the mean salary
plt.axvline(
    mean_salary,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Mean Salary: ₦{mean_salary:,.0f}"
)

plt.axvline(
    median_salary,
    color="blue",
    linestyle="--",
    linewidth=2,
    label=f"Median Salary: ₦{median_salary:,.0f}"
)

plt.title(
    "Salary Distribution of Employees",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.xlabel(
    "Salary (₦)",
    fontsize=12,
    fontweight="bold",
    labelpad=10
)

plt.ylabel(
    "Number of Employees",
    fontsize=12,
    fontweight="bold"
)

plt.legend(fontsize=10)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.4
)

plt.tight_layout()
plt.savefig("salary_distribution.png", dpi=300, bbox_inches="tight")

print("created and saved file!!")