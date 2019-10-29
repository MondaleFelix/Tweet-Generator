text = "one fish two fish red fish blue fish"

def create_lists(text):
	text = text.split()
	count_list = []
	for word in text:
		count = text.count(word)
		word_count = [word, count]
		if word_count not in count_list:
			count_list.append( word_count)
	return count_list

def unique_words(list):
	return len(list)

def frequency(word, list):
	return [word]

# test_histogram = histogram(text)

# print(frequency("fish", test_histogram))

test_list = create_lists(text)

print(unique_words(test_list))
