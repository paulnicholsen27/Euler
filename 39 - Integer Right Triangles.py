'''If p is the perimeter of a right angle triangle with integral 
length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?'''

from collections import defaultdict

triplets = '''( 3 , 4 , 5 )	( 5, 12, 13)	( 7, 24, 25)	( 8, 15, 17) 
( 9, 40, 41)	(11, 60, 61)	(12, 35, 37)	(13, 84, 85)
(16, 63, 65)	(20, 21, 29)	(28, 45, 53)	(33, 56, 65)
(36, 77, 85)	(39, 80, 89)	(48, 55, 73)	(65, 72, 97)
 (20, 99, 101)	(60, 91, 109)	(15, 112, 113)	(44, 117, 125)
(88, 105, 137)	(17, 144, 145)	(24, 143, 145)	(51, 140, 149)
(85, 132, 157)	(119, 120, 169)	(52, 165, 173)	(19, 180, 181)
(57, 176, 185)	(104, 153, 185)	(95, 168, 193)	(28, 195, 197)
(84, 187, 205)	(133, 156, 205)	(21, 220, 221)	(140, 171, 221)
(60, 221, 229)	(105, 208, 233)	(120, 209, 241)	(32, 255, 257)
(23, 264, 265)	(96, 247, 265)	(69, 260, 269)	(115, 252, 277)
(160, 231, 281)	(161, 240, 289)	(68, 285, 293)'''

output = []
skipped = [" ", "\n", "\t"]
while triplets:
	current_char = triplets[0]
	triplets = triplets[1:]
	if current_char == "(":
		current_triplet = ()
		new_int = ""
	elif current_char == ")":
		current_triplet += (int(new_int),)
		output.append(current_triplet)
	elif current_char in skipped:
		pass
	elif current_char in "0123456789":
		new_int += current_char
	elif current_char == ",":
		current_triplet += (int(new_int),)
		new_int = ""
print output

perimeters = defaultdict(int)
for triplet in output:
	perimeter = sum(triplet)
	while perimeter < 1000:
		perimeters[perimeter] +=1
		perimeter += sum(triplet)

max_solutions = 0
best_perimeter = 0
for key in perimeters:
	if perimeters[key] > max_solutions:
		max_solutions = perimeters[key]
		best_perimeter = key
print best_perimeter, perimeters[best_perimeter]
print perimeters[120]
