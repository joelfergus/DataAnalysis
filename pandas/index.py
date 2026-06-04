import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "department": ["HR", "IT", "Finance", "Marketing", "HR", "IT"],
    "salary": [50000, 100000, 50000, 60000, 55000, 70000],
    "age": [25, 30, 35, 28, 32, 29]
}


df = pd.DataFrame(data)
print("\n-------------------THIS IS THE HEAD--------------------")
print(df.head()) # this prints the first 5 rows of the DataFrame df
print("\n-------------------THIS IS THE TAIL--------------------")
print(df.tail()) # this prints the last 5 rows of the DataFrame df
print("\n-------------------THIS IS THE SHAPE--------------------")
print(df.shape) # this prints the dimensions of the DataFrame df
print("\n-------------------THIS IS THE INFO--------------------")
print(df.info()) # this prints the summary of the DataFrame df, including the data types
print("\n-------------------THIS IS THE DESCRIPTION--------------------")
print(df.describe()) # this prints the statistical summary of the DataFrame df, including count,
print("\n-------------------THIS IS THE COLUMNS--------------------")
print(df.columns) # this prints the column names of the DataFrame df
print("\n-------------------THIS IS THE DATATYPE--------------------")
print(df.dtypes) # this prints the data types of each column in the DataFrame df
print("\n-------------------THIS IS THE NULL--------------------")
print(df.isnull().sum()) # this prints the number of null values in each column of the DataFrame df
print("\n-------------------THIS IS THE UNIQUE--------------------")
print(df["department"].unique()) # this prints the unique values in the "department" column of the DataFrame df 


print("\n-------------------THIS IS THE COLUMN SELECTION--------------------")

print(df[["salary", "name"]])
print("\n-------------------THIS IS THE ROW SELECTION--------------------")
#iloc, loc, and [] are used for column selection in pandas DataFrames.
#iloc is used for integer-based indexing, loc is used for label-based indexing, and []
#is used for both label-based and integer-based indexing, depending on the context.
print(df.iloc[0]) # this selects the first column of the DataFrame df using
print("------first 3 columns------")
print(df.iloc[0:3]) # this selects the first three rows of the DataFrame df using
print("------row and column------")
print(df.iloc[1,2]) # this selects the second row of the DataFrame df using

print("\n-------------------THIS IS FOR LOC--------------------")
print(df.loc[0:2, "department" : "age"]) # this selects the first row of the DataFrame df using loc