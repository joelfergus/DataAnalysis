import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#numpy meansnumerical python
#print(np.mean([1, 2, 3, 4, 5])) #mean of a list of numbers

df = pd.read_excel("employee.xlsx") #read an excel file into a pandas DataFrame

departmentAverage = df.groupby("DEPARTMENT")["SALARY"].mean().sort_values(ascending=False) #group the DataFrame by the "DEPARTMENT" column, calculate the mean of the "SALARY" column for each department, and sort the results in descending order

departmentCount = df["DEPARTMENT"].value_counts() # Count the number of occurrences of each unique value in the "DEPARTMENT" column

salaries = df["SALARY"] # Extract the "SALARY" column from the DataFrame
number_of_departments = len(departmentAverage) # Get the number of unique departments

colors = plt.cm.Set3(np.linspace(0, 1, number_of_departments)) # Generate a list of colors using the Set3 colormap, with a number of colors equal to the number of departments

#creating a 2 by 2 grid
fig, axs =plt.subplots(2, 2, figsize=(12, 10)) # Create a 2x2 grid of subplots with a figure size of 12x10 inches
# this creates 2 rows and 2 columnns

fig.suptitle("EmployeeAnalysis Dashboard", fontsize=16, fontweight="bold") # Set the overall title for the figure with a font size of 16 and bold weight


ax1 = axs[0, 0] # Select the first subplot (top-left)
bars = ax1.bar(
    departmentAverage.index,
    departmentAverage.values, 
    color=colors, 
    edgecolor="black",
    linewidth=0.6 
)


for bar, val in zip(bars, departmentAverage.values):
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + (departmentAverage.max() * 0.01),
        f"₦{val:,.0f}",
        ha="center",
        va="bottom",
        fontsize=7,
        fontweight="bold",
        rotation=90
    )

ax1.set_title("Average Salary by Department", fontsize=12, fontweight="bold") # Set the title for the first subplot with a font size of 12 and bold weight
ax1.set_xlabel("Department", fontsize=10, fontweight="bold") # Set the x-axis label for the first subplot with a font size of 10 and bold weight
ax1.set_ylabel("Average Salary", fontsize=10, fontweight="bold") # Set
ax1.set_ylim(0, departmentAverage.max() * 1.2)# Set the y-axis limits for the first subplot to be from 0 to 120% of the maximum average salary
ax1.tick_params(axis="x", rotation=30)
ax1.grid(axis="y", linestyle="--", alpha=0.4)


#pie
ax2 = axs[0, 1] # Select the second subplot (top-right)
ax2.pie(
    departmentCount.values,
    labels=departmentCount.index,
    autopct="%1.1f%%", # Display the percentage of each slice with one decimal place
    startangle=140, # Start the pie chart at a 90-degree angle
    colors=plt.cm.Set3(np.linspace(0, 1, len(departmentCount))), # Use the Set3 colormap to generate colors for each slice
    wedgeprops=dict(width=0.6)#

) 

ax2.set_title("Headcount by Department", fontsize=12, fontweight="bold") # Set the title for the second subplot with a font size of 12 and bold weight

ax3 = axs[1, 0] # Select the third subplot (bottom-left)
ax3.hist(
    salaries,
    bins=10, # Set the number of bins for the histogram to 10
    color="#6851ff", # Set the color of the bars in the histogram
    edgecolor="black", # Set the edge color of the bars in the histogram to yellow
    linewidth=0.8 # Set the width of the edges of the bars in the histogram to 0.8 points
)
ax3.axvline(
    salaries.mean(), # Draw a vertical line at the mean salary
    color="red", # Set the color of the line to red
    linestyle="--", # Set the line style to dashed
    linewidth=2, # Set the width of the line to 1.5 points
    label=f"Mean: ${salaries.mean():,.0f}" # Add a label to the line displaying the mean salary formatted with commas and no decimal places
)

ax3.axvline(
    salaries.median(), # Draw a vertical line at the median salary
    color="orange", # Set the color of the line to orange
    linestyle="--", # Set the line style to dashed
    linewidth=2, # Set the width of the line to 1.5 points
    label=f"Median: ${salaries.median():,.0f}" # Add a label to the line displaying the median salary formatted with commas and no decimal places
)
ax3.set_title("Salary Distribution", fontsize=12, fontweight="bold") # Set the title for the third subplot with a font size of 12 and bold weight
ax3.set_xlabel("Salary ($)", fontsize=10, fontweight="bold") # Set the
ax3.set_ylabel("Count", fontsize=10, fontweight="bold") # Set the
ax3.legend(fontsize=8)
ax3.grid(axis="y", linestyle="--", alpha=0.4)


#SCATTER PLOT
ax4 = axs[1, 1] # Select the fourth subplot (bottom-right)
ax4.scatter(
    df["YEARS_EXPERIENCE"],
    df["SALARY"],
    color= '#A23B72',
    edgecolor="black",
    linewidth=0.4,
    s=80,
    alpha=0.8
)

z = np.polyfit(df["YEARS_EXPERIENCE"], df["SALARY"], 1)
p = np.poly1d(z)
xr = np.linspace(df["YEARS_EXPERIENCE"].min(), df["YEARS_EXPERIENCE"].max(), 200)
ax4.plot(
    xr,
    p(xr),
    'r--',
    linewidth=2,
    label='Trend'
)
ax4.set_title("Salary vs Experience", fontweight="bold")
ax4.set_xlabel("Years of Experience", fontsize=10) 
ax4.set_ylabel("Salary ($)", fontsize=10) 
ax4.legend(fontsize=9)
ax4.grid(axis="y", linestyle="--", alpha=0.4)




plt.tight_layout(pad=3.0) # Adjust the spacing between subplots to prevent overlap, with a padding of 3.0 inches
plt.savefig(
    "employee_analysis_dashboard.png", # Save the figure as a PNG file with the specified filename
    dpi=300, # Set the resolution of the saved figure to 300 dots per inch (DPI)
    bbox_inches="tight" # Adjust the bounding box of the saved figure to fit tightly around the content
)

plt.close()
print("Dashboard saved as employee_analysis_dashboard.png") # Print a message indicating that the dashboard has been saved successfully