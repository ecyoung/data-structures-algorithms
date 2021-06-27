"""
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"
Note: Ignore spaces and capitalization. So "d g o" is an anagram of "God" and "dog" and "o d g".
"""
# O(n log n) --> can improve by implementing a hash table (Python dictionary)
def anagram1(s1, s2):
	# remove spaces and lowercase letters 
	s1 = s1.replace(" ", "").lower()
	s2 = s2.replace(" ", "").lower()
	# return boolean for sorted match 
	return sorted(s1) == sorted(s2)

# O(n)
def anagram2(s1, s2):

	# remove spaces and lowercase letters 
	s1 = s1.replace(" ", "").lower()
	s2 = s2.replace(" ", "").lower()

	# edge case to check if same number of letters 
	if len(s1) != len(s2):
		return False 

	# create counting dictionary 
	count = {}

	# fill dictionary for first string (add counts)
	# note that letter refers to potential dictionary keys
	for letter in s1:
		if letter in count:
			count[letter] += 1
		else:
			# initialze value to 1 if there are no current values
			count[letter] = 1

	# fill dictionary for second string (subtract counts)
	for k in count:
		if letter in count:
			count[letter] -= 1
		else:
			count[letter] = 1

	# check that all counts are 0
	for k in count:
		if count[k] != 0:
			return False

	# otherwise they are anagrams 
	return True

print(anagram1('dd','aa'))