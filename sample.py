import histogram as hist
import sys
import random

text = "Mondale is the coolest person alive"

def return_word(histogram):
	random_index = random.randint(0, len(histogram) - 1)
	return list(histogram)[random_index]

test_histogram = hist.histogram(text)


print(return_word(test_histogram))