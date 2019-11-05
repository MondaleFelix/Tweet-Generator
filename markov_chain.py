text = "one fish two fish red fish blue fish"

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
		# print(following_words_dict)
		counter += 1


	print(following_words_dict)


get_following_words(text)