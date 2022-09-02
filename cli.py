import readline

main = open('original_files/main_files/main.txt', 'r+')
true = open('original_files/main_files/true.txt', 'a+')
false = open('original_files/main_files/false.txt', 'a+')
cursor = open('original_files/main_files/cursor.txt', 'r+')
cursor_backup = open('original_files/main_files/cursor_backup.txt', 'a+')

lines = []
certainty_str = ""

def isBlank (myString):
    return not (myString and myString.strip())

# Read previous cursor location
main.seek(int(cursor.readline()))

# Scan every line in main.txt
line = main.readline()

while line:
	lines.append(line)
	choice = ""

	# Show current accumulated lines and ask input from user
	if line.isspace():
		# Need to strip last element so certainty_str is glued to passage
		last_elem = lines.pop().strip()
		lines.append(last_elem)
		print(' '.join([str(elem) for elem in lines]))

		# Check input for true or false response
		while (choice != 'T' and choice != 't' and choice != 'true' and choice != 'True' and choice != 'F' and choice != 'f' and choice != 'false' and choice != 'False'):
			choice = input("True or False?: ")

			# If choice is true
			if choice == 'T' or choice == 't' or choice == 'true' or choice == 'True':
				certainty_level = ""

				# Check if certainty is digit
				while certainty_level.isdigit() == False:
					certainty_level = input("Degree of certainty (1-5): ")

					# If it is digit then check if it between boundaries (1-5)
					if certainty_level.isdigit():
						certainty_level = int(certainty_level)
						if certainty_level > 0 and certainty_level < 6:
							certainty_str = f"Degree of Certainty (1-5): {str(certainty_level)}\n\n"
							certainty_level = str(certainty_level)
						else:
							print("Wrong input. Numbers must be between 1-5. Try again...")
							certainty_level = ""
					else:
						print("Wrong input. Input is not a number. Try again...")

				true.writelines(lines)
				true.writelines(certainty_str)

				# Save current read position
				cursor.seek(0)
				cursor.write(str(main.tell()))

				# Save all cursor positions for backup
				cursor_backup.write(str(f"{main.tell()}\n"))

			# If choice is false
			elif choice == 'F' or choice == 'f' or choice == 'false' or choice == 'False':
				certainty_level = ""
				lemma = ""
				tags = ""
				data = ""

				# Check is string is not empty
				while isBlank(lemma):
					lemma = input("Correct Lemma: ")
				lemma = f'Correct Lemma: {lemma}\n'

				# Check is string is not empty
				while isBlank(tags):
					tags = input("Correct Tag(s): ")
				tags = f'Correct Tag(s): {tags}\n'

				# Check is string is not empty
				while isBlank(data):
					data = input("Corrected Data: ")
				data = f'Correct Data: {data}\n'

				# Check if certainty is digit
				while certainty_level.isdigit() == False:
					certainty_level = input("Degree of certainty (1-5): ")

					# If it is digit then check if it between boundaries (1-5)
					if certainty_level.isdigit():
						certainty_level = int(certainty_level)
						if certainty_level > 0 and certainty_level < 6:
							certainty_str = f"Degree of Certainty (1-5): {str(certainty_level)}\n\n"
							certainty_level = str(certainty_level)
						else:
							print("Wrong input. Numbers must be between 1-5. Try again...")
							certainty_level = ""
					else:
						print("Wrong input. Input is not a number. Try again...")

				false.writelines(lines)
				false.writelines(lemma)
				false.writelines(tags)
				false.writelines(data)
				false.writelines(certainty_str)

				# Save current read position
				cursor.seek(0)
				cursor.write(str(main.tell()))

				# Save all cursor positions for backup
				cursor_backup.write(str(f"{main.tell()}\n"))

			# If neither of inputs is true or false
			else:
				print("Wrong input. Try again...")
		lines = []
	line = main.readline()

main.close()
true.close()
false.close()
cursor.close()
cursor_backup.close()
