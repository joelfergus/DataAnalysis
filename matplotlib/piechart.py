import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("employee.xlsx")

departments_count = df["DEPARTMENT"].value_counts()

labels = departments_count.index.tolist()
sizes = departments_count.values.tolist()
number_of_departments = departments_count.sum() 
# Get the total number of employees

colors = plt.cm.Set3(np.linspace(0, 1, number_of_departments))
# Generate a list of colors using the Set3 colormap, with a number of colors equal to the number of departments

explode = [0.05] * len(labels)  
# Explode all slices slightly for better visibility

wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    colors=colors,
    explode=explode,
    startangle=140,
    shadow=True,
    wedgeprops=dict(width=0.6)
)

#styling the percentage text
for autotext in autotexts: 
    autotext.set_fontsize(10)
    autotext.set_fontweight("bold")

plt.title(
    "Employee Distribution by Department",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.savefig("department_distribution_pie.png", dpi=300, bbox_inches="tight")  # Save the figure as a PNG file with a resolution of 300 dpi
print("Pie chart saved as 'department_distribution_pie.png'")  # Print a message indicating that the pie chart has been saved
plt.close()  # Close the figure to free up memory