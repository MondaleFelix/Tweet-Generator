class HashTable(object):

	def __init__(self, size):
		self.size = size
		#  creates the amount of buckets based on size
		self.buckets = [None] * self.size
		self.data = [None] * self.size

	def put(self, key , value):

		hash_value = self.hash_function(key, len(self.slots))

		if self.buckets[hash_value] is None:
			self.buckets[hash_value] = key
			self.data[hash_value] = value

	def hash_function(self, key, size):
		return key % size