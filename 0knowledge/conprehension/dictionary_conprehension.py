# ## syntax
# # new_dict = {new_key: new_value for (key, value) in nato_dict.items() if test}
# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {name:random.randint(1,100) for name in names}
#
# print(student_scores)
#
# passed_students = {name:score for name, score in student_scores.items() if score>= 60}
# print(passed_students)


# create a dictionary called result
# that takes each word in the given sentence -> word = key
# and calculates the number of letters in each word.  -> len(word) = value
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split(" ")}
print(result)

# create a dictionary called weather_f
# that takes each temperature in degrees Celsius
# and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f use this formula: (temp_c * 9/5) + 32 = temp_f
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp_c * 9/5) + 32 for day, temp_c in weather_c.items()}
print(weather_f)