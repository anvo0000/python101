import pandas as pd

# Create a dataframe from scratch
data_dict = {
"students": ["Amy", "James", "Angela"],
"scores": ["76", "50", "65"]
}
data_student = pd.DataFrame(data=data_dict)
data_student.to_csv("students.csv")
# print(data_student)

#Loop through rows of a df
# best practices
for (index, row) in data_student.iterrows():
    print(row["students"])

# not good, if column name have space, or like Python keywords
for (index, row) in data_student.iterrows():
    print(row.students)