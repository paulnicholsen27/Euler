# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import itertools


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

def circle_generator(number, digits):
	circles = [number]
	new_circle = True
	while new_circle:
		digits.append(digits.pop(0))
		next_circle = int(''.join(str(i) for i in digits))
		if next_circle == number:
			new_circle = False
		else:
			circles.append(next_circle)
	return circles

def circular_prime(n):
	primes = prime_list(n)
	answers = [2,5]
	for number in primes:
		if number not in answers:
			circular_prime = True
			digits = map(int, str(number))
			for digit in digits:
				if digit % 2 == 0 or digit == 5: #no number with an even digit or a 5 will be prime
					circular_prime = False
			if circular_prime:
				circles = circle_generator(number, digits)
				for circular_number in circles:
					if circular_number not in primes:
						circular_prime = False
			if circular_prime:
				answers.append(circles[n] for n in range(len(circles)))
# 				print(int(circle) for circle in circles)
				print "circles: ", circles, number
				print "type(circles): ", type(circles)
				print "type(circles[0]): ", type(circles[0])
				print "circles[0]: ", circles[0]
	print(answers)
	print len(answers)

circular_prime(100000)
