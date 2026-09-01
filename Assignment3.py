import pandas as pd

data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": ["Single", "Married", "Single", "Married", "Divorced",
                       "Married", "Divorced", "Single", "Married", "Single"],
    "Taxable Income": ["125K", "100K", "70K", "120K", "95K",
                       "60K", "220K", "85K", "75K", "90K"],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

print(df)

print(df.loc[[0, 4, 7, 8]])

print(df.loc[3:7])

print(df.iloc[4:9, 2:5])

print(df.iloc[:, 1:4])



df1 = pd.read_csv("UCS420/Iris.csv")

print(df1.head())




df1 = df1.drop(4)
df1 = df1.drop(df1.columns[3], axis=1)

print(df1)





data2 = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01",
                     "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

df2 = pd.DataFrame(data2)

df2.to_csv("employees.csv", index=False)

print(df2)

print(df2.shape)

print(df2.info())

print(df2.describe())

print(df2.head(5))

print(df2.tail(3))

print("Average salary:", df2["Salary"].mean())

print("Total bonus:", df2["Bonus"].sum())

print("Youngest age:", df2["Age"].min())

print("Highest rating:", df2["Rating"].max())

df2 = df2.sort_values("Salary", ascending=False)

def category(rating):

    if rating >= 4.5:

        return "Excellent"

    elif rating >= 4.0:

        return "Good"

    else:

        return "Average"

df2["Performance"] = df2["Rating"].apply(category)

print(df2.isnull().sum())

df2 = df2.rename(columns={"Employee_ID": "ID"})

print(df2[df2["Years_of_Experience"] > 5])

print(df2[df2["Department"] == "IT"])

df2["Tax"] = df2["Salary"] * 0.10

df2.to_csv("employees_modified.csv", index=False)

print(df2)