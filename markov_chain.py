import random
import re


def get_clean_text(file):
    with open(file, "r") as f:
        text = f.read().split()
    text = [re.sub('[^A-Za-z]+', '', word).lower() for word in text]
    text = " ".join(text)
    return text


text = get_clean_text("corpus.txt")

	

def get_following_words(text):
	words_list = text.split()
	following_words_dict = {}
	counter = 1

	for word in words_list:

		# Breaks if word is last word in list
		if word is words_list[len(words_list) - 1]:
			break

			# 
		if word not in following_words_dict:
			following_words_dict[word] = []
			following_words_dict[word].append(words_list[counter])
		else:
			following_words_dict[word].append(words_list[counter])
		counter += 1
		# print(following_words_dict)

	return following_words_dict

def return_sentence(hist, num_of_words):
	
	random_word = random.choice(list(hist.keys()))

	sentence = [random_word]

	next_word = get_next_word(hist[random_word])

	while len(sentence) is not num_of_words:
		sentence.append(next_word)

		next_word = get_next_word(hist[next_word])

	sentence = " ".join(sentence)

	return sentence



def get_next_word(array):
	return array[random.randint(0,len(array) - 1)]

print(return_sentence(get_following_words(text), 10))
