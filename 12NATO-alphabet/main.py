import pandas as pd
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("nato_phonetic_alphabet.csv")
# print(df)
nato_dict = {row["letter"]:row["code"] for (index, row) in df.iterrows()}

print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")
phonetic_words = [nato_dict[letter.upper()] for letter in user_input]

print(phonetic_words)