import sys
import random

f = open("/usr/share/dict/words", "r")

words_list = f.readlines()
user_input = int(sys.argv[1])

shuffled_sentence = []


for i in range(user_input):

	# Appends n amount of random words from words list
	shuffled_sentence.append(words_list[random.randint(0,len(words_list) - 1)][2:])

print(" ".join(shuffled_sentence))

f.close()