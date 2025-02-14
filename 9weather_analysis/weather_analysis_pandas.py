# Weather Analysis by using Pandas
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

temp_list = data["temp"].to_list()
sum_temp = sum(temp_list)
count_temp = len(temp_list)
avg = sum_temp/count_temp
print(avg)


print(f"Series mean = avg: {data["temp"].mean()}")
print(f"Series max: {data["temp"].max()}")

# Get data in columns
print(data["condition"])
print(data.condition)

# Get data in a row
print(data[data.day == "Monday"])
print("Day has max temp: ", data[data.temp == data.temp.max()])


# Convert Monday's temp to F
monday = data[data.day == "Monday"]
f = (monday.temp * 9/5) + 32
print("Monday F:", f)

