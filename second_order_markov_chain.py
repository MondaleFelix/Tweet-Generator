import random

text = "one fish two fish red fish blue fish"
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


for i in range(len(words_list)):

	if i == 0:
		q.add(words_list[i])
		q.add(words_list[i+1])

	elif i == len(words_list) -1 :
		break

	else: 
		q.remove()
		q.add(words_list[i +1])

	print(q.items)







