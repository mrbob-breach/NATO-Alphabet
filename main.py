import pandas

# Create dictionary from csv file
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv", sep=',')
mydict = {row['letter']: row['code'] for (index, row) in nato_df.iterrows()}

# Translate the user input to the phonetic code word
user_input = input("Input a word to be translated: ").upper()
output = [mydict[letter] for letter in user_input]
print(output)
