'''The nth term of the sequence of triangle numbers is given by, tn = n(n+1) / 2; 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical 
position and adding these values we form a word value. For example, the word value 
for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we 
shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing 
nearly two-thousand common English words, how many are triangle words?'''

import string
from eulertools import letter_scores, get_max_value, triangle_number_list

def make_wordlist(file):
	wordlist = []
	g = open(file)
	for word in g:
		unstripped_words = word.split(",")
	for word in unstripped_words:
		wordlist.append(word[1:-1])
	return wordlist

wordlist = make_wordlist('words.txt')
letter_scores = letter_scores()

def get_word_scores(wordlist):
	word_scores = {}
	for word in wordlist:
		score = 0
		for letter in word:
			score += letter_scores[letter]
		word_scores[word] = score
	return word_scores

word_scores = get_word_scores(wordlist)
max_word_score = get_max_value(word_scores)[1]
triangle_numbers = triangle_number_list(max_word_score)
triangle_words = []
for word in word_scores:
	if word_scores[word] in triangle_numbers:
		triangle_words.append(word)

print len(triangle_words)