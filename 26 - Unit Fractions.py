import math


def unit_fraction(n):
	longest_so_far = 1
	longest_decimal_so_far = "1"
	for denominator in range(2, n+1):
		dividends = []
		decimal_part = ""
		dividend = 10
		still_dividing = True
		while still_dividing:
			if dividend % denominator == 0:
				still_dividing = False
			elif dividend in dividends: 
				decimal_part += str(dividend/denominator)
				if len(decimal_part) > len(longest_decimal_so_far):
					longest_decimal_so_far = decimal_part
					longest_so_far = denominator
				still_dividing = False
			else:
				decimal_part += str(dividend/denominator)
				dividends.append(dividend)
				dividend = (dividend % denominator) * 10
	return longest_so_far


			
print unit_fraction(1000)
