
import itertools, string

def prime(n): 
#determines if n is prime
	if n == 1:
	    return False
	factor_list = [1,n]
	for divisor in range(2,int(n**.5)+1):
	    if n % divisor == 0:
	        return False
	return True

def pandigital_generator(n, start=1):
	#returns all pandigitals using all integers from start to n
	pans = []
	perms = itertools.permutations(range(start, n+1))
	for j in perms:
		strng = ""
		for number in j:
			strng += str(number)
		if strng[0] != str(0):
			pans.append(int(strng))
	return pans

def letter_scores():
	#returns dictionary of letters with their positions in the alphabet
	scores = {}
	for letter in string.uppercase:
		scores[letter] = string.uppercase.index(letter) + 1
	return scores

def get_max_value(dictionary):
	#returns highest numerical value and associated key in a dictionary
	max_key = ''
	max_value = 0
	for key in dictionary:
		if dictionary[key] > max_value:
			max_value = dictionary[key]
			max_key = key
	return key, max_value

def triangle_number_list(n):
	'''returns list of all triangle numbers <= n 
	where a triangle number is defined as a number
	of the form x(x+1) / 2 where x is an integer'''
	triangle_numbers = []
	current = 1
	while True:
		next_number = current * (current+1) / 2
		if next_number > n:
			return triangle_numbers
		else:
			triangle_numbers.append(next_number)
			current += 1
