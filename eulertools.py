
import itertools

def prime(n): 
#determines if n is prime
	if n == 1:
	    return False
	factor_list = [1,n]
	for divisor in range(2,int(n**.5)+1):
	    if n % divisor == 0:
	        return False
	return True

def pandigital_generator(n):
	#returns all pandigitals of length n
	pans = []
	perms = itertools.permutations(range(1,n+1))
	for j in perms:
		strng = ""
		for number in j:
			strng += str(number)
		pans.append(int(strng))
	return pans