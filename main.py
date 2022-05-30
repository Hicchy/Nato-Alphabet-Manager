import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")






def phonetise():
    continues = True
    while continues:
        try:
            question = input("Enter a word: ").upper()
            nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
            result = [nato_alphabet[x] for x in question]
        except KeyError:
            print(f"{question} is not a valid input")
        else:
            print(result)
            continues = False


phonetise()
