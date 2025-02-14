# Data Source: https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data

import pandas as pd
FILE = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
OUTPUT = "squirrel_count.csv"
column_name = ["Fur Color", "Count"]


data = pd.read_csv(FILE)
# print(data.columns)

pri_color_count = data["Primary Fur Color"].value_counts()


df = pri_color_count.reset_index() # Use .reset_index() to convert Series to DataFrame
df.columns = column_name
print("before\n", df)

df["Fur Color"] = df["Fur Color"].astype("string")
df.loc[df["Fur Color"] == "Cinnamon", "Fur Color"] = "Red"

print("after\n", df)
print("type", type(df))

df.to_csv(OUTPUT)