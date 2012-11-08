# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)


def palindrome_checker(n):
	n = str(n)
	if len(n) == 1 or len(n) == 0:
		return True
	elif n[0] == n[-1]:
		return palindrome_checker(n[1:-1])
	else:
		return False

def palindrome_checker_checker():
	print palindrome_checker("A") == True
	print palindrome_checker("AB") == False
	print palindrome_checker("ABBA") == True
	print palindrome_checker("ABCDEDCBA") == True
	print palindrome_checker(12345) == False
	print palindrome_checker(123454321) == True
	print palindrome_checker(123321) == True

def binary_decimal_comp(n):
	sum = 0
	for number in range(n):
		if palindrome_checker(number) and palindrome_checker(int(bin(number)[2:])):
			sum += number
	return sum

print binary_decimal_comp(10**6)
