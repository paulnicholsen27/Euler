#Not the most programmy solution, but I figured out a simple pattern in the numbers.

sum = 1
n = 3
while n <= 1001:
	sum += (4*n**2 - ((n-1) * 6))
	n +=2
print sum