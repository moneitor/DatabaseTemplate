import json
from difflib import SequenceMatcher, get_close_matches

my_file = "data.json"
data_dict = json.load(open(my_file, "r"))


def compare(a="", b=""):
    return SequenceMatcher(None, str(a), str(b)).ratio()


def definition(dictionary=dict, key=""):
    close_match = ''
    key = key.lower()
    filter_dict = get_close_matches(key, dictionary, cutoff=0.7)
    ratio = 0
    for w in filter_dict:
        if compare(w, key) > ratio:
            ratio = compare(w, key)
            close_match = w
    if ratio == 1:
        return dictionary[close_match]
    elif ratio > 0.7:
        print("Did you mean {} with a ratio of {}?".format(close_match, ratio))
        answer = input("\npress 'y' for yes and 'n' for not. ")
        if answer.startswith("y"):
            for element in dictionary[close_match]:
                print("MEANING: ", element, "\n")
        else:
            print("no such word")
    else:
        print("There is no similar word in the dictionary. ")


request = input("Do you want to look for a word? 'y' or 'n'. ")

while request.startswith("y") or request == "yes":
    word = input("Enter a word: ")
    definition(data_dict, word)
    request = input("Do you want to look for a word? 'y' or 'n'. ")

