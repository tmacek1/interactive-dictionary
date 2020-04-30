import json
from difflib import get_close_matches

'''
    This program replicates real-life dictionary usage.
    It searches for targeted word and prints explanation.
    Program uses external json file as datasource.
'''


def main_func(word):
    # load data from json file
    data = json.load(open("data.json"))

    # test for acronym fist
    if word.isupper():
        return data[word]

    # initial checks
    word.lower()
    checkForDigits = word.isalpha()
    test = get_close_matches(word, data.keys())

    if not word:
        return "word must have at least 1 letter"

    if checkForDigits == False:
        return "there are no words with digits in dictionary"

    # main logic
    if word in data:
        return (data[word])
    elif word.capitalize() in data:
        return (data[word.capitalize()])
    elif test:
        result = input("did you mean: '" + str(test[0]) +
                       "'? --------> enter Y if yes, or N if no : ")
        if result == "Y":
            return data[test[0]]
        elif result == "N":
            return "the word doesnt exists in dict, please try another word"
        else:
            return "wrong entry"
    else:
        return "the word doesnt exists in dict, please try another word"


word = input("please enter the word that you would like to search in the dictionary:")
result = (main_func(word))

if type(result) == list:
    for r in result:
        print(r)
else:
    print(str(result))
