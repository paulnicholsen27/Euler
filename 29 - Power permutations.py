distinct_terms = []
for a in range(2,101):
	for b in range(2, 101):
		if a**b not in distinct_terms:
			distinct_terms.append(a**b)
print len(distinct_terms)

print len(set([i**j for i in range(2,101) for j in range(2,101)]))