def fibonacci(n):
	fibo_list = [1,2]
	first = 1
	second = 2
	for number in range (3,n):
		third = first + second
		if len(str(third)) == 1000:
			return len(fibo_list) + 2
		else:
			fibo_list.append(third)
			first = second
			second = third

print fibonacci(1000000)