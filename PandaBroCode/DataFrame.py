import pandas as pd

# dataFrame = A tabular data structure with rows and columns.(2 Dimensional)
            #  similar to an Excel spreadaheet

data = {
    "Name" : ["Spongebob", "Patrick", "Squidward"],
    "Age" : [30,35,50]
}

df = pd.DataFrame(data, index = ["A","B","C"])
# print(df)
# print(df.loc["A"])
# print(df.iloc[2])

# Add a new column 

df["job"] = ["Cook","N/A","Cashier"]
# print(df)

# Add new rows

new_rows = pd.DataFrame([{"Name" : "Sandy", "Age":28,"Job":"Engineer"},
                        {"Name" : "Eugene", "Age":60,"Job":"Manager"}],
                        index=["D","E"])
df = pd.concat([df, new_rows])
print(df)
