
import pandas

data = pandas.read_csv("./Nato_python_converter/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
word = input("Enter a word: ").upper()
state = True
while state:
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letter in the alphabet")
        word = input("Enter a word: ").upper()
    else:
        state = False
    
print(output_list)
