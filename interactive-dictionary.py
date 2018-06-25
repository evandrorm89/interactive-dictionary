import json
#module to get close matches of a word, in case of a mistype from the user
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
	#some conditionals for the user input not to be case-sensitive
	if w.lower() in data:
		return data[w.lower()]

	elif w.capitalize() in data:
		return data[w.capitalize()]

	elif w.upper() in data:
		return data[w.upper()]
		
	elif len (get_close_matches(w, data.keys())) > 0:
		x = input("Did you mean %s instead? (y/n)" % get_close_matches(w, data.keys())[0])
		x = x.lower()
		if x == 'y':
			return data[get_close_matches(w, data.keys())[0]]
		elif x == 'n':
			w = input ("What did you mean then? ")
			return translate (w)
		else:
			return "please, enter y or n"
	else:
		return "The word doesn't exist"

word = input ("Type a word: ")

output = translate(word)
#in case there is more than one meaning for the word, the output will be a list of those meanings
if type(output) == list:
	for i in output:
		print (i)
else:
	print (output)
