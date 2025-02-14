# Reference: https://pandas.pydata.org/docs/reference/series.html

# 1. pandas has 2 structures:
## DataFrame (2 dimensional)
day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
Wednesday,15,Rain
Thursday,14,Cloudy
Friday,21,Sunny
Saturday,22,Sunny
Sunday,24,Sunny

## Series (1 dimensional)
1 column data like:
0    12
1    14
2    15
3    14
4    21
5    22
6    24
Name: temp,

## Use .reset_index() to convert Series to DataFrame