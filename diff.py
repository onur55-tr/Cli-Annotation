import json
import readline
from termcolor import colored
import difflib

# https://stackoverflow.com/questions/32500167/how-to-show-diff-of-two-string-sequences-in-colors
def get_edits_string(old, new):
    result = ""
    codes = difflib.SequenceMatcher(a=old, b=new).get_opcodes()
    for code in codes:
        if code[0] == "equal":
            result += colored(old[code[1]:code[2]], 'white')
        elif code[0] == "delete":
            result += colored(old[code[1]:code[2]], 'red')
        elif code[0] == "insert":
            result += colored(new[code[3]:code[4]], 'green')
        elif code[0] == "replace":
            result += (colored(old[code[1]:code[2]], 'red') + colored(new[code[3]:code[4]], 'green'))
    return result

def make_choice(id, his_dict):
	choice = ""
	while choice != 'a' and choice != 'A' and choice != 'agree' and choice != 'Agree' and choice != 'd' and choice != 'D' and choice != 'disagree' and choice != 'Disagree':
		choice = input("Agree of Disagree?: ")
		if choice == 'a' or choice == 'A' or choice == 'agree' or choice == 'Agree':
			agree.write(id)
			agree.writelines(his_dict[id])
		elif choice == 'd' or choice == 'D' or choice == 'disagree' or choice == 'Disagree':
			disagree.write(id)
			disagree.writelines(his_dict[id])
	checkpoint.seek(0)
	checkpoint.write(id.split()[1])

ben = input("1. First annotator\n2. Second annotator\nWho am I?\n")

# Load json data
my_folder = 'first_annotator/second_pass'
his_folder = 'second_annotator/second_pass'

if ben == "2":
	my_folder, his_folder = his_folder, my_folder

with open(f"{my_folder}/false.json", "r") as json_file:
	my_dict = json.load(json_file)

with open(f"{his_folder}/false.json", "r") as json_file:
	his_dict = json.load(json_file)

checkpoint = open(f"{my_folder}/curr_id.txt", 'r+')
save = checkpoint.readline()

# Open agree.txt and disagree.txt
agree = open(f"{my_folder}/agree.txt", 'a+')
disagree = open(f"{my_folder}/disagree.txt", 'a+')

for id, val in his_dict.items():
	if int(id.split()[1]) <= int(save):
		continue

	# If his ID is in my files
	if id in my_dict:
		# If there is diff between ID's print it and make choice
		if my_dict[id] != his_dict[id]:
			print("----------------------------------------------")
			print("My annotation difference")
			print(f"{id}{get_edits_string(my_dict[id].strip(), his_dict[id].strip())}")
			make_choice(id, his_dict)

		# Else continue because his ID and my ID is identical
		continue

	# Else his ID is not in my files
	print("----------------------------------------------")
	print("Other annotators annotation")
	print(f"{id}{his_dict[id].strip()}")
	make_choice(id, his_dict)
