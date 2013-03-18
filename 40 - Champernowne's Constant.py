'''An irrational decimal fraction is created by concatenating 
the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the 
value of the following expression.

d1  d10  d100  d1000  d10000  d100000  d1000000'''

champ = ""

start = 1
while len(champ) < 1000000:
	champ += str(start)
	start += 1

print champ[:50]
answer = 1
power = 0
while power <= 6:
	answer *= int(champ[10**power - 1])
	power += 1

print answer

