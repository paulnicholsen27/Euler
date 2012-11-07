currencies = [200, 100, 50, 20, 10, 5, 2, 1]
#How many combinations of coins add up to 2 pounds?

def combo_generator(total):
	answer = 2 #for 1 200-piece and 2 100-pieces
	amount_left = total
	for b in range(2):
		amount_left = total - b * 100
		for c in range(int(amount_left/50) + 1):
			amount_left = total - b * 100 - 50*c
			for d in range(int(amount_left/20) + 1):
				amount_left = total - b * 100 - 50*c - 20*d
				for e in range(int(amount_left/10) +1):
					amount_left = total - b * 100 - 50*c - 20*d - 10*e
					for f in range(int(amount_left/5) +1):
						amount_left = total - b * 100 - 50*c - 20*d - 10*e - 5*f
						for g in range(int(amount_left/2) + 1):
							amount_left = total - b * 100 - 50*c - 20*d - 10*e - 5*f - 2 * g
							for h in range(int(amount_left/1) +1):
								if 100 * b + c*50 + d*20 + e*10 + f*5 + g*2 + h*1 == total:
									answer +=1
	return answer


print combo_generator(200)
