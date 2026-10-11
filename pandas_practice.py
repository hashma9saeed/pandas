import pandas as pd
#******************************* Series Basics ****************************************************
#Create a Pandas Series.Display the Series its index and values.Find its data type.
data = pd.Series([12000, 15000, 11000, 18000, 22000])
print(data)
print(data.index)
print(data.values)
print(data.dtype)

#***************************** Custom Index *******************************************************
#Create a Pandas Series containing temperatures: Use the days Monday to Friday as the index.
#Display the temperature recorded on Wednesday.
#Display temperatures for Monday and Friday.
data = pd.Series([32, 35, 31, 29, 36],index =(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]))
print(data[["Wednesday"]])
print(data[["Monday","Friday"]])

#*************************** Series Operations *******************************************************
#Create two Pandas Series Perform: Addition, Subtraction, Multiplication
Product_A_sales = pd.Series([100, 150, 200, 250])
Product_B_sales = pd.Series([80, 120, 180, 220])
print(Product_A_sales + Product_B_sales)
print(Product_A_sales - Product_B_sales)
print(Product_A_sales * Product_B_sales)

#***************************** Creating And Inspecting  DataFrame *************************************
#Create a DataFrame and display its:
data = pd.DataFrame({
    "Name" : ["Ali","Sarah","Mushk","Saim","Farah"],
    "Age" : [27,20,30,29,26],
    "Salary" : [55000,15000,70000,60000,40000]
})
print(data)
print(data.shape)          #Number of rows and columns
print(data.columns)        #Column name
print(data.dtypes)         #datatype
print(data.head(3))        #first 3 rows
print(data.tail(3))        #last 3 rows
print(data.describe())     #Basic statistical summary

#***************************** Selecting Columns ****************************************************
#Select one column.
print(data["Age"])
#select multiple columns.
print(data[["Name","Age"]])
#Select all columns except Age.
print(data.drop("Age",axis = 1))

#***************************** Selecting Rows Using Loc And Iloc *************************************
#Use .loc to:
#Select the first employee.
print(data.loc[0,"Name"])
#Select rows 2–4.
print(data.loc[2:5,"Salary"])
#Select only Name and Salary for selected rows.
print(data.loc[2:5,["Name","Salary"]])
#Select Rows Using iloc:
print(data.iloc[3,1])                    #third row, first column
#selecting multiple rows/columns
data.iloc[0:3, [0, 2]]                   #rows at positions 0, 1, 2 and columns at positions 0 and 2

#****************************** Boolean Filtering *****************************************************
#Create a DataFrame containing employee salaries.
data = pd.DataFrame({
    "Employee": ["Ali", "Sarah", "Mushk", "Saim", "Farah"],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [55000, 60000, 75000, 65000, 50000]
})
#Employees earning more than 60,000.
print(data[data["Salary"] > 60000])
#Employees earning less than 40,000
print(data[data["Salary"] < 40000])
#Employees earning between 40,000 and 70,000.
print(data[(data["Salary"] >= 40000) & (data["Salary"] >= 70000)])
#Find employees who work in IT or earn more than 60,000.
print(data[(data["Department"] == "IT") | (data["Salary"] > 60000)])

#********************************* Sorting Data *******************************************************
#Create a DataFrame containing products and their prices.  
data = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Price": [80000, 2500, 4000, 30000, 5000]
})
#Sort products by price in ascending order.
print(data.sort_values("Price"))
#Sort products by price in descending order.
print(data.sort_values("Price", ascending=False))
#Sort by two columns simultaneously.
print(data.sort_values(["Price","Product"]))

#******************************** Add And Modify Columns **********************************************
#Create a DataFrame containing Product, Price, Quantity.
data = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Price": [80000, 2500, 4000, 30000, 5000],
    "Quantity": [5, 20, 15, 8, 12]
})
#Create a new Total_Sales column.
data["Total_Sales"] = data["Price"] * data["Quantity"]
print(data)
#Increase all prices by 10%.
data["Price"] = data["Price"]*1.10
print(data)
#Modify one existing column.
data["Quantity"] = [10, 25, 20, 12, 15]
print(data)

#******************************* Delete Column And Rows ********************************************
#Remove one column.
print(data.drop("Price",axis = 1))
#Remove two columns.
print(data.drop(["Price","Quantity"],axis = 1))
#Remove a specific row
print(data.drop(2,axis = 0))

#*************************** Rename Coumns *********************************************************
#Create a DataFrame with poorly named columns.
data = pd.DataFrame({
    "emp_name": ["Ali", "Sarah", "Mushk", "Saim", "Farah"],
    "emp_age": [27, 20, 30, 29, 26],
    "emp_salary": [55000, 60000, 75000, 65000, 50000]
})
#Rename them to: Name, Age, Salary
print(data.rename(columns={
    "emp_name": "Name",
    "emp_age": "Age",
    "emp_salary": "Salary"
}))

#****************************** Handle Missing Values ************************************************
#Create a DataFrame containing missing values using NaN.
import numpy as np
data = pd.DataFrame({
    "Name": ["Ali", "Sarah", "Mushk", "Saim"],
    "Age": [20, np.nan, 22, 21],
    "Salary": [50000, 60000, np.nan, 55000]
})
#Detect missing values.
print(data.isna())
#Count missing values in each column.
print(data.isna().sum())
#Remove rows containing missing values.
print(data.dropna())
#Replace missing numerical values with the column mean.
print(data.fillna(data.mean(numeric_only = True)))

#******************************* Duplicate Data *******************************************************
#Create a DataFrame containing duplicate rows
data = pd.DataFrame({
    "Name": ["Ali", "Sarah", "Ali", "Saim"],
    "Age": [20, 22, 20, 21],
    "Salary": [50000, 60000, 50000, 55000]
})
#Identify duplicate rows.
print(data.duplicated())
#Count duplicates.
print(data.duplicated().sum())
#Remove duplicate rows.
print(data.drop_duplicates())

#****************************** String Operations ****************************************************
#Create a Series containing names:
names = pd.Series(["Ali Khan", "Sara Ahmed", "Hassan Raza", "Ayesha Malik"])
#Convert names to uppercase.
print(names.str.upper())
#Convert names to lowercase.
print(names.str.lower())
#Find names containing "a".
print(names[names.str.contains("a")])
#Find the length of each name.
print(len(names))

#*********************************** Groupby ********************************************************
#Create a DataFrame:
data = pd.DataFrame({
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Employee": ["Ali", "Sara", "Ahmed", "Ayesha", "Hassan"],
    "Salary": [40000, 60000, 55000, 70000, 45000]
})
#Average salary for each department.
print(data.groupby("Department")["Salary"].mean())
#Maximum salary for each department.
print(data.groupby("Department")["Salary"].max())
#Number of employees in each department.
print(data.groupby("Department")["Employee"].count())

#************************** Value Counts ************************************************************
#Frequency of each category.
data = pd.Series(["IT", "CS", "IT", "SE", "CS", "IT", "AI", "SE", "CS"])
print(data.value_counts())

#************************** Combine DataFrames *******************************************************
#create a dataframe and perform:
#concat()
month1 = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Sales": [50000, 2000, 3000]
})
month2 = pd.DataFrame({
    "Product": ["Monitor", "Laptop", "Mouse"],
    "Sales": [15000, 55000, 2500]
})
print(pd.concat([month1, month2], ignore_index=True))

# merge()
customers = pd.DataFrame({
    "Customer_ID": [1, 2, 3],
    "Customer": ["Ali", "Sara", "Ahmed"]
})

orders = pd.DataFrame({
    "Customer_ID": [1, 2, 3],
    "Amount": [5000, 7000, 4000]
})
print(pd.merge(customers, orders, on="Customer_ID"))

#******************************************************************************************************