import string

names = []
letter_values = {}

f = open('22 - names.txt')
f = f.read()
f = f.split(",")
for name in f:
	names.append(name[1:-1])
names.sort()

letter_values = dict(zip((string.uppercase), range(1,27)))
print letter_values

def name_value(name):
	list_total = 0
	for position in (range(len(names))):
		name_total = 0
		for letter in names[position]:
			name_total += letter_values[letter]
		list_total += (name_total * (position+1))	
	return list_total

print name_value(names)