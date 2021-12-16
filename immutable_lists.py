def lists(full, add, remove):
	"""
	This function takes in an original list of strings, adds a new list of strings,
	and then removes elements from the third list of strings. Duplicates are removed
	and then the new list is sorted by 2 keys: character count and then reverse 
	alphabetical.

	Input:
		full - list of strings, any type
		add - list of strings, any type
		remove - list of strings, any type

	Output:
		new_list - new list, tuple
		
	"""

	# Make easily editable copies of the input
	full = [x for x in full]
	add = [x for x in add]
	remove = [x for x in remove]

	# Append the 'full' and 'add' lists
	full.extend(add)

	# Remove duplicates and elements in the 'remove' list
	full = [x for i, x in enumerate(full) if x not in full[:i] and x not in remove]

	# Sort the list by character count and reverse alphabetical
	full = sorted(full, key=lambda x: (len(x), x), reverse = True)

	# Convert to tuple
	new_list = tuple(full)

	return tuple(new_list)


a = ("one", "two", "three", "zulu")
b = ("one", "two", "five", "six")
c = ("two", "five")

print(lists(a,b,c))
