text = "one fish two fish red fish blue fish"

def read_file(file):
	f = open(file, "r+")
	words = f.readlines()
	f.close()
	return words

def histogram(file):
	text = text.split()
	histograms = {}
	for word in text:
		count = text.count(word)
		histograms.update( {word: count})
	return histograms

# Returns the number of unique tokens
def unique_words(histogram):
	return len(histogram)

# Returns the occurences in histogram
def frequency(word, histogram):
	return histogram[word]

test_histogram = histogram(text)

print(frequency("fish", test_histogram))

print(test_histogram)