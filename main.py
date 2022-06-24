# 1. Get list of ABC and corresponding code. 
# 2. Function to get input string and generate morse code.

import pandas as pd

file = pd.read_csv("code.csv")

# dictionary of Latin and Morse ABC and numbers without symbols.
code = {row.Letter: row.Morse for (index, row) in file.iterrows()}

#Converter function:
def converter(input):
    output = ""
    for letter in input:
        try:
            output += f"{code[letter]}\n"
        except KeyError:
            output += f"{letter}\n"

    print(f"Here is your code (symbols and spaces are shown as symbols):\n{output}")

print("**** MORSE CODE CONVERTER ****")
words = input(f"Enter latin text to convert to Morse code: ")
converter(words.upper())

