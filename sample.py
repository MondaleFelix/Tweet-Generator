import histogram as hist
import sys
import random

text = "one fish two fish red fish blue fish"

def return_word(histogram):
	random_index = random.random()
	for key, value in histogram.items():
		if random_index < value:
			return key



test_histogram = hist.histogram(text)


print(return_word(test_histogram))

def generate_probability(histogram):
	total_words = sum(histogram.values())
	counter = 0
	new_histogram = {}
	for key, value in histogram.items():
		probability = value / total_words
		counter += probability
		new_histogram[key] =  counter
	return new_histogram



print(generate_probability(test_histogram))
print(return_word(generate_probability(test_histogram)))