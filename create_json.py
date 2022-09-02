import readline
import json
import sys

# python3 create_json.py first_annotator/second_pass

if len(sys.argv) == 2:
	# My files
	folder = sys.argv[1]
	true_files = open(f'{folder}/true.txt', 'r')
	false_files = open(f'{folder}/false.txt', 'r')

	true_dict = {}
	false_dict = {}
	true_lines = true_files.readlines()
	false_lines = false_files.readlines()

	string = []
	for line in true_lines:
		string.append(line)
		if line.isspace():
			id = string.pop(0)
			true_dict[id] = ''.join([str(elem) for elem in string])
			string = []

	with open(f'{folder}/true.json', 'w') as fp:
		json.dump(true_dict, fp, ensure_ascii=False)

	string = []
	for line in false_lines:
		string.append(line)
		if line.isspace():
			id = string.pop(0)
			false_dict[id] = ''.join([str(elem) for elem in string])
			string = []

	with open(f'{folder}/false.json', 'w') as fp:
		json.dump(false_dict, fp, ensure_ascii=False)
else:
	print("Usage example: python3 create_json.py <folder path to annotation files>")