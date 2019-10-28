import random
import sys

text = "one fish two fish red fish blue fish"

def histogram(text):
	text = text.split()
	histograms = {}
	for word in text:
		count = text.count(word)
		histograms.update( {word: count})
	print(histograms)

histogram(text)
