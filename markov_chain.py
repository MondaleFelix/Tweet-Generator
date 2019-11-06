import random


text = "one fish two fish red fish blue fish"

class MarkovChain(dic):
	
	__init__(self, words_list):
	
	super(MarkovChain, self).__init__()	

def get_following_words(text):
	words_list = text.split()
	following_words_dict = {}
	counter = 1

	for word in words_list:
		if word is words_list[len(words_list) - 1]:
			break

		if word not in following_words_dict:
			following_words_dict[word] = []
			following_words_dict[word].append(words_list[counter])
		else:
			following_words_dict[word].append(words_list[counter])
		counter += 1

	return following_words_dict

def return_sentence(hist, num_of_words, starting_word):
	
	sentence = [starting_word]

	next_word = get_next_word(hist[starting_word])

	while len(sentence) is not num_of_words:
		sentence.append(next_word)

		next_word = get_next_word(hist[next_word])


	print(sentence)



def get_next_word(array):
	return array[random.randint(0,len(array) - 1)]

return_sentence(get_following_words(text), 10 , "fish")
