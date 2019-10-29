import random
import sys

text = "one fish two fish red fish blue fish"

def histogram(text):
	text = text.split()
	histograms = {}
	for word in text:
		count = text.count(word)
		histograms.update( {word: count})
	return histograms

def unique_words(histogram):
	return len(histogram)

def frequency(word, histogram):
	return histogram[word]

test_histogram = histogram(text)

print(frequency("fish", test_histogram))
# Should print 4