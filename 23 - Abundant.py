import math

def abundant(n):
	abundant_numbers = []
	for number in range(n):
		factor = 1
		sum = 0
		while factor < (int(math.sqrt(number)) + 1):
			if number % factor == 0:
				if number != factor:
					sum += factor
					if number / factor != factor and number/factor != number:
						sum += (number/factor)
			factor += 1
		if sum > number:
			abundant_numbers.append(number)
	return abundant_numbers
	
def sum_generator(n):
	addend_list = abundant(n)
	sum_list = []
	for i in range(len(addend_list)):
		for j in range(i, len(addend_list)):
			sum_list.append(addend_list[i] + addend_list[j])
	not_a_sum = []
	for number in range(n):
		if number not in sum_list:
			not_a_sum.append(number)
	second_sum = 0
	for number in not_a_sum:
		second_sum += number
	print not_a_sum
	return not_a_sum
	
print sum_generator(28123)			

    
