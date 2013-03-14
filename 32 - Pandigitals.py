'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.'''

import itertools

def pandigital():
	products = []
	permutations = itertools.permutations(range(1,10))
	print permutations
	for permutation in permutations:
		product = equation_maker(permutation)
		if product:
			products.append(int(product))
	print "done", set(products)
	return sum(list(set(products)))



def equation_maker(permutation):
	'''better solution given that working equations must be 2-digit * 3-digit = 4-digit
	or 1-digit * 4-digit = 4-digit'''
	equation_string = "".join("%s" %digit for digit in permutation)
	first_factor = equation_string[:2]
	second_factor = equation_string[2:5]
	product = equation_string[5:]
	if equation_tester(first_factor, second_factor, product):
		return product
	else:
		first_factor = equation_string[0]
		second_factor = equation_string[1:5]
		if equation_tester(first_factor, second_factor, product):
			return product 

def equation_tester(first_factor, second_factor, product):
	return int(first_factor) * int(second_factor) == int(product)



#THIS WAS SUPER SLOW, BUT WORKED.  NOT SMART THOUGH.
# def equation_tester(permutation):
# 	new_products = []
# 	equation_string = "".join("%s" %digit for digit in permutation)
# 	mult_location = 1
# 	equals_location = mult_location + 1
# 	while mult_location < len(permutation) - 1:
# 		while equals_location < len(permutation):
# 			first_factor = equation_string[:mult_location] 
# 			second_factor = equation_string[mult_location:equals_location]
# 			product = equation_string[equals_location:]
# 			if (first_factor == 1 or 
# 				second_factor == 1 or
# 				or first_factor > second_factor or #no sense checking things twice.  I'm not Santa.
# 				int(product) < int(second_factor) or 
# 				int(product) < int(first_factor) or
# 				first_factor[-1] == 5 or 
# 				second_factor[-1] == 5 or 
# 				product[-1] == 5):
# 					pass
# 			elif int(first_factor) * int(second_factor) == int(product):
# 				new_products.append(int(product))
# 				print product
# 			equals_location += 1
# 		mult_location += 1
# 		equals_location = mult_location + 1
# 	return new_products

print pandigital() 	