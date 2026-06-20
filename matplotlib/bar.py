import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#numpy meansnumerical python
#print(np.mean([1, 2, 3, 4, 5])) #mean of a list of numbers

df = pd.read_excel("employee.xlsx") #read an excel file into a pandas DataFrame


departments_average = (
    df.groupby("DEPARTMENT")["SALARY"].mean().sort_values(ascending=False) #group the DataFrame by the "DEPARTMENT" column, calculate the mean of the "SALARY" column for each department, and sort the results in descending order
)

#print(departments_average) #print the average salary for each department

departments_max = (
    df.groupby("DEPARTMENT")["SALARY"].max().sort_values(ascending=False) # this is basically group by and order by in SQL, it groups the data by the "DEPARTMENT" column, calculates the maximum of the "SALARY" column for each department, and sorts the results in descending order
)


departments_min = (
    df.groupby("DEPARTMENT")["SALARY"].min().sort_values(ascending=False)
)


departments_count = (
    df.groupby("DEPARTMENT")["SALARY"].count().sort_values(ascending=False)

)

number_of_departments = len(departments_average) # Get the number of unique departments

fig_width = max(10,  number_of_departments * 0.6) # Set the figure width based on the number of departments, with a minimum width of 10 inches
fig_height = 8 # Set the figure height to 8 inches
plt.figure(figsize=(fig_width, fig_height)) # Create a new figure with the specified width and height
colors = plt.cm.Set3(np.linspace(0, 1, number_of_departments)) # Generate a list of colors using the Set3 colormap, with a number of colors equal to the number of departments 
#print(colors)


# create a bar chart
bars = plt.bar(
    departments_average.index, # Set the x-axis labels to the department names
    departments_average.values, # Set the y-axis values to the average salaries
    color=colors, # Set the color of each bar to the corresponding color in the colors list
    edgecolor="black", # Set the edge color of the bars to black
    linewidth=0.8 # Set the width of the edges of the bars to 0.8 points
)

for bar, value in zip(bars, departments_average.values):
    plt.text(
        bar.get_x() + bar.get_width() / 2, # Set the x-coordinate of the text to the center of the bar
        bar.get_height() + (departments_average.max() * 0.01), # Set the y-coordinate of the text to be slightly above the top of the bar
        f"₦{value:,.0f}", # Format the value as a string with commas as thousands separators and no decimal places, and add a currency symbol (₦) in front of it
        ha="center", # Align the text horizontally to the center ha means horizontal alignment
        va="bottom",   # Align the text vertically to the bottom
        fontsize=8,
        fontweight="bold",
        rotation=90
    ) # this loop adds text labels to each bar in the bar chart, displaying the average salary for each department above the corresponding bar

plt.title(
    "Average Salary by Department", 
    fontsize= 16, 
    fontweight="bold",
    pad = 20
) # this sets the title of the bar chart to "Average Salary by Department", with a font size of 16 points, bold font weight, and a padding of 20 points between the title and the top of the plot

plt.xlabel(
    "Department", 
    fontsize= 12, 
    fontweight="bold",
    labelpad = 10
)


plt.ylabel(   
    "Average Salary (₦)", 
    fontsize= 12, 
    fontweight="bold",
    labelpad = 10
)

plt.xticks(
    rotation=45,
    ha="right",
    fontsize=9
    ) # Rotate the x-axis labels by 45 degrees and align them to the right

plt.grid(
    axis = "y",
    linestyle = "--",
    alpha = 0.4
)

plt.ylim(
    0,
    departments_average.max() * 1.125
)

plt.tight_layout() # Adjust the layout of the plot to prevent overlapping elements

plt.savefig(
    "average_salary_by_department.png",
    dpi = 300, # Save the plot as a PNG file with a resolution of 300 dots per inch (DPI)
    bbox_inches = "tight" # Adjust the bounding box of the saved figure to fit tightly around the plot elements
)

plt.close() # Close the current figure to free up memory and resources
print("Created and saved file: average_salary_by_department.png") # Print a message indicating that the file has been created and saved successfully

