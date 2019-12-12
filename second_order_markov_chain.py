import random

text = "i like cats and you like cats i like dogs but you hate dogs"
words_list = text.split(" ")


class Queue():

	def __init__(self):
		self.items = []

	def is_empty(self, size):
		return self.items == []

	def add(self, item):
		self.items.insert(1,item)

	def remove(self):
		self.items.pop(0)

	def size(self):
		return len(self.items)



q = Queue()
n = 2

arr = []
histogram = {}

for i in range(len(words_list)):

	if i == 0:
		q.add(words_list[i])
		q.add(words_list[i+1])

	elif i == len(words_list) -1 :
		break

	else: 
		q.remove()
		q.add(words_list[i +1])



	key = " ".join(q.items)

	# histogram[key] = 1
	arr.append(key)

counter = 0
for tokens in arr:
	value = [arr[0], 1] 
	histogram[tokens] = value


def get_following_words(array):

	following_words_dict = {}
	counter = 1

	for word in array:
		if word is not array[len(array) -1]:
			# Breaks if word is last word in list
			if word is words_list[len(array) - 1]:
				break

				# 
			if word not in following_words_dict:
				following_words_dict[word] = []

				following_words_dict[word].append(array[counter])
				following_words_dict[word].append(1)



			else:
				following_words_dict[word].append(array[counter])
				following_words_dict[word][1] +=1
			counter += 1
	# print(following_words_dict)

	return following_words_dict

print(get_following_words(arr))

