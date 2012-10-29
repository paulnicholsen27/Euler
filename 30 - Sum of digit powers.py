answer = 0
for n in range (2,1000000):
	integers = map(int,str(n))
	sum = 0
	for digit in integers:
		sum += (digit ** 5)
	if sum == n:
		answer += sum
		print sum
print answer