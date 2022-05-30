import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

question = input("Enter a word: ").upper()


try:
    nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
    result = [nato_alphabet[x] for x in question]
    print(result)
except KeyError as error_1:
    print(f"{error_1} is not a valid letter.")





