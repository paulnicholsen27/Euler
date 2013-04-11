'''We shall say that an n-digit number is pandigital if it 
makes use of all the digits 1 to n exactly once. For example, 2143 
is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?'''

import itertools
from eulertools import prime, pandigital_generator




def prime_pandigitals():
	#finds largest prime pandigital number
	length = 7 #8 and 9 digit pandigitals are divisible by 9
	while length > 3:
		potentials = pandigital_generator(length)
		potentials = [pandigital for pandigital in potentials if str(pandigital)[-1] not in [2,4,5,6,8]]
		potentials.sort()
		potentials.reverse()
		for potential in potentials:
			if prime(potential):
				return potential
		length -= 1
	return "No prime pandigitals found"


	

print prime_pandigitals()