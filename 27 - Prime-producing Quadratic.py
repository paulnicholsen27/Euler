# n**2 + An + B

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
	

def quadratic_primes(n):
	b_coefficients = prime_list(1000)
	highest_x = 0
	product = 0
	for a in range(-1000, 1001):
		for b in b_coefficients:
			making_primes = True
			x = 0
			while making_primes:
				result = x**2 + a*x + b
				if result < 0 or not prime(result):
					if x > highest_x:
						highest_x = x
						product = a * b
					making_primes = False
				x+=1
	return highest_x, product
				
print quadratic_primes(1000)