# figure is the whole window or page that everything is drawn on, it can contain multiple axes
# axes is the area where the data is plotted, it can be multiple in a figure
#xlabel is the label for the x-axis, ylabel is the label for the y-axis, title is the title of the plot
#legend is the box that explains the symbols and colors used in the plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("employee.xlsx")

salaries = df["SALARY"].tolist()


plt.figure(figsize=(10, 5))
plt.plot(salaries)
plt.title("Employee Salaries")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.tight_layout() #prevents labels from being cut off
plt.savefig("employee.png", dpi=150) #saves the figure as a png file with a resolution of 150 dpi
plt.close() #closes the figure to free up memory
print("created and saved file!!")