'''Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. 
The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their 
difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum 
and difference are pentagonal and D = |Pk - Pj| is minimised; what is 
the value of D?'''

from math import sqrt

def pentagonal_list_generator(length):
	pents = []
	for n in range(1,length):
		pents.append(pentagonal_maker(n))
	return pents

def pentagonal_maker(n):
	return (3*n**2 - n)/2

def pentagonal_checker(n):
	#checks to see if a given number is pentagonal (using discriminant of quad formula)
	disc = sqrt(1 + 24 * n)
	return disc == int(disc)

def pair_checker(n):
	pents = pentagonal_list_generator(n)
	smallest_difference = 10**10
	for k in range(1,len(pents)):
		i = 1
		j = i+k
		while i <= len(pents)-k:
			if pents[i] >= distance_to_next_pent(j):
				print "testing:", i, j, k
				if pentagonal_checker(pentagonal_maker(i) + pentagonal_maker(j)) and \
					pentagonal_checker(pentagonal_maker(j) - pentagonal_maker(i)):
					return k
			j+=1
			i+=1
	return "None"

def distance_to_next_pent(index):
	distance = 3 * index + 4
	return distance

# def pair_checker():
# 	pents = pentagonal_list_generator(100)
# 	smallest_difference = 10**10
# 	best_index = 0,0
# 	for i in range(len(pents)):
# 		print "Looking....", i
# 		j = i + 1
# 		while pents[i] >= distance_to_next_pent(j):
# 			print "j: ", j
# 			if (pentagonal_maker(i) + pentagonal_maker(j) in pents and 
# 				pentagonal_maker(j) - pentagonal_maker(i) in pents):
# 				difference = pentagonal_maker(j) - pentagonal_maker(i)
# 				if difference < smallest_difference:
# 					smallest_difference = difference
# 					best_index = i,j
# 			j += 1
# 	return smallest_difference

print pair_checker(250)