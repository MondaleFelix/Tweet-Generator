import sys
import random

words_list = sys.argv[1:]

def shuffle_words():
	random.shuffle(words_list)
	return words_list


if __name__ == "__main__":
	words_list = shuffle_words()
	return words_list