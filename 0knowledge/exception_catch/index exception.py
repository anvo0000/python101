# Index Exception
fruits = ["Apple", "Pear", "Orange"]
index = 4
try:
    print(fruits[index])
except IndexError:
    print("Fruit pie")
