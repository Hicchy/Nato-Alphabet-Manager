import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_alphabet)

question = input("Enter a word: ").upper()

result = [nato_alphabet[x] for x in question]
print(result)

