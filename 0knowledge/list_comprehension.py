#Comprehension
# Can be applied to Python sequences: list, tuple, string, range
##Syntax: new_list = [new_item for item in list]
## List comprehension with if: new_list = [new_item for item in list if condition]


# original list to create a new_numbers from numbers
numbers = [1, 2, 3]
new_numbers = []
for n in numbers:
    new_numbers.append(n+1)

print (numbers)
print (new_numbers)

# List Comprehension
new_numbers2 = [n+1 for n in numbers]
print(new_numbers2)

#Apply List Comprehension to string
name = "AnVo0000"
chars = [letter for letter in name]
print(chars)

# range(1,5)
double_range = [n*2 for n in range(1,5)]
print(double_range)

# Find the name has less than 4 letters.
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
# Find the name has greater than 4 letters and uppercase them
long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)

#Find even number
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(snum) for snum in list_of_strings]
result = [num for num in numbers if num%2==0]
print(result)
