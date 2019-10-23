import sys
import random

f = open("/usr/share/dict/words", "r")

words_list = f.readlines()

for i in range(int(sys.argv[1])):
	print(words_list[random.randint(0,len(words_list) - 1)])