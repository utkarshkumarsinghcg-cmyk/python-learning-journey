import pandas as pd
data  = [100,102,104,200,202]

# Series =  pd.Series(data, index=["A","B","C","D","E"])

# Series.loc["C"] = 200
# print(Series)
# print(Series.loc["A"])
# print(Series.loc["C"])
# print(Series.iloc[1])
# print(Series[Series>=200])
# print(Series[Series<200])

calories = {
    "day 1": 1750,
    "day 2" : 2100,
    "day 3" : 1700,
}

Series = pd.Series(calories)
print(Series)
print(Series.loc["day 1"])
print(Series.loc["day 2"])
Series.loc["day 3"] += 500 
print(Series.loc["day 3"])
print(Series[Series >= 2000])

