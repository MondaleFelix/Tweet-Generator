#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)


        #  Returns bucket using hash function
    def get_bucket(self, key):
    	bucket_index = self._bucket_index(key)
    	return self.buckets[bucket_index]

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""

      	# O(n) Dependant on only the size of the buckets as keys are apended per bucket


        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n) Why and under what conditions?"""

      	# O(n) Dependant on only the size of the buckets as values are apended per bucket

        values = []
        for bucket in self.buckets:
        	for key, value in bucket.items():
        		values.append(value)
        return values
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) Why and under what conditions?"""


      	# O(n) Dependant on only the size of the buckets as items are apended per bucket

        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""

        # O(n) Dependant on size of buckets

        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket

        count = 0

        for bucket in self.buckets:
        	count += bucket.length()
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

        # O(1) Constant time as we are we know the index of the bucket 

        bucket = self.get_bucket(key)

        if bucket.find(lambda item: item[0] == key) is None:
        	return False
        else: 
        	return True


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))


        # O(1) Constant time as we are we know the index of the bucket 

        bucket = self.get_bucket(key)

        found_data = bucket.find(lambda item: item[0] == key)

        if found_data is None:
        	raise KeyError("Key not found: {}".format(key))

        else: 

        	return found_data[1]


    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""

        # O(1) Constant time as we are we know the index of the bucket 

        # Get bucket using hash function
        bucket = self.get_bucket(key)

        # Data found in bucket
        current_data = bucket.find(lambda item: item[0] == key)
        print(current_data)
        # Data to be added
        new_data = [key, value]
        print(new_data)

        # Adds data if not found
        if current_data is None:
        	bucket.append(new_data)

        #  Updates data 
        else:
        	current_data[1] = value
        	# current_data = (key,)





        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))


        # O(1) Constant time as we are we know the index of the bucket 
        bucket = self.get_bucket(key)

        found_data = bucket.find(lambda item: item[0] == key)

        if found_data is None:
        	raise KeyError("Key is not found:{}".format(key))
        else:
        	bucket.delete(key)

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
