import json
from difflib import get_close_matches

data = json.load(open("data.json"))

key= input("Enter your word:")

def my_dict(key):
    if key in data:
        return "The meaning of the word is",data[key]
    elif len(get_close_matches(key,data.keys())) > 0:
        yn= input("Did you mean %s? If yes, type'Y'.If No, type 'N'" %get_close_matches(key,data.keys())[0]) 
        if yn=="Y":
            return "Meaning of the word is",data[get_close_matches(key,data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exist bruv"    
    else:
        print("word doesn't exist")
print(my_dict(key.lower()))