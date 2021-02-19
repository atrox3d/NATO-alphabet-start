student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
phonetic_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# import json
# print(json.dumps(phonetic_df.to_dict(), indent=4))

# for index, row in phonetic_df.iterrows():
#     print(row.letter, row.code)
nato = {row.letter: row.code for index, row in phonetic_df.iterrows()}
# print(json.dumps(nato, indent=4))

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
print("NATO Alphabet word encoder.")


def generate_phonetic():
    user_input = input("insert word to encode: ")
    try:
        nato_list = [nato[char.upper()] for char in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_list)


generate_phonetic()
