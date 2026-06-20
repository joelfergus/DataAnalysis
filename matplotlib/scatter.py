import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel("employee.xlsx")

x = df["YEARS_EXPERIENCE"]
y = df["SALARY"]
plt.scatter(
    x,
    y,
    color = 'skyblue',
    edgecolors='black',
    linewidth=0.5,
    s=100, # THIS IS THE SIZE FOR EACH DOT, 100 IS MEDIUM SIZE
    alpha=0.8 #THIS IS THE TRANSPARENCY VALUE 0.8 IS SLIGHTLY SEE THROUGH
)

z = np.polyfit(x,y,2) #a value of 1 makes a straight line while 2 makes it a curve

p = np.poly1d(z)

x_line = np.linspace(x.min(), x.max(), 200)

plt.plot(
    x_line,
    p(x_line),
    color = "red",
    linestyle="--",
    linewidth=2,
    label="Trend Line"
)

plt.title(
    "Years of experience vs Salary",
    fontsize=16,
    fontweight="bold",
    pad = 20
)

plt.xlabel(
    "Years of experience",
    fontsize=16,
    fontweight="bold"
)

plt.ylabel(
    "Salary",
    fontsize=16,
    fontweight="bold"
)

plt.legend(
    fontsize=11
)

plt.grid(
    linestyle="--",
    alpha=0.4
)

plt.tight_layout()

plt.savefig(
    "experience_vs_salary.jpg",
    dpi=300,
    bbox_inches="tight"
)

print("Scatter image saved")

plt.close()
