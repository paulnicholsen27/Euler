# The fraction 49/98 is a curious fraction, as an inexperienced
# mathematician in attempting to simplify it may incorrectly believe 
# that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, 
# less than one in value, and containing two digits in the numerator and 
# denominator.

# If the product of these four fractions is given in its lowest common 
# terms, find the value of the denominator.

from __future__ import division 

def fraction_maker():
	results = []
	for denominator in range(10,99):
		numerator = 10
		while numerator < denominator:	
			if numerator/denominator == canceller(numerator, denominator):
				results.append(numerator/denominator)
				print numerator, "/", denominator
			numerator += 1
	print results
	return reduce(lambda x, y: x * y, results)



def canceller(numerator, denominator):
	tens_place_numerator = int(numerator/10)
	tens_place_denominator = int(denominator/10)
	ones_place_numerator = numerator % 10
	ones_place_denominator = denominator % 10
	if not all([tens_place_denominator, tens_place_numerator, 
				ones_place_denominator, ones_place_numerator]):
		return None
	if tens_place_numerator == ones_place_denominator:
		reduced_fraction = ones_place_numerator / tens_place_denominator
		return reduced_fraction
	elif ones_place_numerator == tens_place_denominator:
		reduced_fraction = tens_place_numerator / ones_place_denominator
		return reduced_fraction
	else:
		return None

print fraction_maker()
