import histogram as hist
import sys
import random

text = "one fish two fish red fish blue fish"

def return_word(histogram):
	#  Returns a random float from 0 - 1
	random_index = random.random()
	# returns word if value is greater than random_index
	print(random_index)
	for key, value in histogram.items():
		if random_index < value:
			return key






#  Returns a histogram with the probability assigned to the key
def generate_probability(histogram):
	total_words = sum(histogram.values())
	counter = 0
	new_histogram = {}
	for key, value in histogram.items():
		probability = value / total_words
		counter += probability
		key =  counter
	return new_histogram



test_histogram = hist.histogram(text)
print(generate_probability(test_histogram))
print(return_word(generate_probability(test_histogram)))