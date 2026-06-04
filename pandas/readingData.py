import pandas as pd
import mysql.connector
from sqlalchemy import create_engine


# this is for excel
print("------READING EXCEL FILE------")
df = pd.read_excel("Book1.xlsx") # Read an Excel file into a DataFrame
print(df)


# this is for sql
print("------READING SQL FILE------")
engine = create_engine("mysql+mysqlconnector://root:@localhost/staff_leave_mgmt_db") # Create a SQLAlchemy engine

df = pd.read_sql("SELECT * FROM users", con=engine) # Read a SQL query into a DataFrame
print(df)