def print_upper_words(words):
	for word in words:
		print(word.upper())

def print_upper_ewords(words):
	for word in words:
		if word.startswith('e') or word.startswith('E'):
			print(word.upper())

print_upper_ewords(["eagle", "Edward", "Alfred"])

def print_upper_words3(words, must_start_with):
	for word in words:
		for letter in must_start_with:
			if word.startswith(letter):
				print(word.upper())

print_upper_words3(["eagle", "Edward", "Alfred", 'ana', "zope"], must_start_with=["A", "E"])
        # EDWARD
        # ALFRED
			