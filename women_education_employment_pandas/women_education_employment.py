import pandas as pd
women_df = pd.read_csv("women_education_employment_pandas/women_education_employment.csv")
print(women_df)
#display the first five rows
print(women_df.head())                                         #gives 5 rows by default
#How many rows and columns are in this dataset
print(women_df.size)
#Display all column names
print(women_df.columns)
#Show data types of each column
print(women_df.dtypes)
#Show statistical summary of numerical columns
print(women_df.describe())
#First 3 rows of the dataset
print(women_df.head(2))
#Last 4 rows of the dataset
print(women_df.tail(4))
#Search and display all women living in "Karachi"
print(women_df[women_df["City"] == "Karachi"])
#Find employed women who have a Master's degree or higher
#(Master or PhD) and display only Name, Education, and Monthly_Income
print(women_df[(women_df["Employment_Status"] == "Employed") & (women_df["Education"].isin(["Master", "PhD"]))] 
[["Name","Education","Monthly_Income"]])
#Find all women who earn more than 100,000 per month
# Display Name, City, Field, and Monthly_Income
print(women_df[women_df["Monthly_Income"] > 100,000]
[["Name","City","Field","Monthly_Income"]])
#Check if there are any missing values in the dataset.If yes, show how many in each column
print(women_df.isna().sum())
#Convert Monthly_Income and Years_Experience to integer type.Then display the data types to confirm
print("Before conversion : ",women_df["Monthly_Income"].dtype)
print("Before conversion : ",women_df["Years_Experience"].dtype)
women_df["Monthly_Income"] = women_df["Monthly_Income"].astype(int)
women_df["Years_Experience"] = women_df["Years_Experience"].astype(int)
print("After conversion : ",women_df["Monthly_Income"].dtype)
print("After conversion : ",women_df["Years_Experience"].dtype)
#Remove all students (Employment_Status = "Student")
women_df = women_df[women_df["Employment_Status"] != "Student"]
print(women_df)
#Create a new DataFrame called "employed_women" with only employed women
employed_women = women_df[women_df["Employment_Status"] == "Employed"]
#Calculate the average monthly income of women in each city
#Sort from highest to lowest
women_df.groupby("City")["Monthly_Income"].mean().sort_values(ascending=False)
#Count how many women have each education level (Bachelor, Master, PhD)
women_df.groupby("Eduction")["Name"].count()
#Calculate the average years of experience for women in each field (CS,Engineering,Business,Medicine)
women_df.groupby("Field")["Years_Experience"].mean()
# Which city has the highest average income for women?
print(women_df.groupby("City")["Monthly_Icome"].mean().sort_values(ascending=False).head(1))
# Which field has the most employed women?
print(women_df[women_df["Employment_Status"] == "Employed"].groupby("Field")["Name"].count().sort_values(ascending=False).head(1))
# What is the average age of employed women?
print(women_df[women_df["Employment_Status"] == "Employed"]["Age"].mean())
# How many women with children are employed?
print(women_df[(women_df["Has_Children"] == "Yes") & (women_df["Employment_Status"] == "Employed")]
    ["Name"].count())
# What is the highest income among women in the dataset?
print(women_df["Monthly_Income"].max())
#Find women who:
# - Live in Lahore OR Islamabad
# - Have a Master's degree or PhD
# - Earn more than 100,000
# - Have more than 5 years of experience
# - Do NOT have children
# Display Name, City, Education, Monthly_Income, Years_Experience, Has_Children
print(
    women_df[
        (women_df["City"].isin(["Lahore", "Islamabad"])) &
        (women_df["Education"].isin(["Master", "PhD"])) &
        (women_df["Monthly_Income"] > 100000) &
        (women_df["Years_Experience"] > 5) &
        (women_df["Has_Children"] == "No")]
    
        [["Name", "City", "Education", "Monthly_Income",
         "Years_Experience", "Has_Children"]]
    
)


#*******************************************************************************************************
