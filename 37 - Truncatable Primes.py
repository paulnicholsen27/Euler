# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def prime(n): #determines if n is prime
	if n == 1:
	    return False
	factor_list = [1,n]
	for divisor in range(2,int(n**.5)+1):
	    if n % divisor == 0:
	        return False
	return True

def prime_list(n):
    list=[2]
    a = 3
    while a <= n:
        if prime(a):
            list.append(a)
            a += 2
        else:
            a += 2
    return list

def truncator(n):
	numbers = [n]
	digits = map(int, str(n))
	while len(digits) > 1:
		digits.pop()
		shorter_number = int(''.join(str(i) for i in digits))
		numbers.append(shorter_number)
	digits = map(int, str(n))
	while len(digits) > 1:
		digits.pop(0)
		shorter_number = int(''.join(str(i) for i in digits))
		numbers.append(shorter_number)
	return numbers

def truncator_locater():
	sum = 0
	answers = []
	bad_digits = [4,6,8,0] #non-prime digits
	primes = prime_list(10**6)
	for potential in primes:
		if potential > 20:
			digits = map(int,str(potential))
			worth_checking = not any(x in digits for x in bad_digits)
			if worth_checking:
				truncateds = truncator(potential)
				all_prime = all(prime(trunc) for trunc in truncateds)
				if all_prime:
					sum += potential
					answers.append(potential)
	print answers
	return sum

print truncator_locater()
