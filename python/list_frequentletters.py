"""list which returns the frequencies of eachletter in a sentence"""
import string 

CHARACTERS = list(string.ascii_lowercase)+[" "]

def letter_frequency(sentence):
    frequencies =[(c,0) for c in CHARACTERS]
    for letters in sentence:
        index=CHARACTERS.index(letters)
        frequencies[index]=(letters,frequencies[index][1]+1)
    return frequencies



print(letter_frequency("this is a new line"))