# '''
# Linked List hash table key/value pair
# '''
#import bcrypt
import hashlib


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """hashedkey = self._hash_mod(key)
        Hash collisions should be handled with linked list chaining
        self.storage[hashedkey] = LinkedPair(key, value)"""
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            curr = self.storage[index]
            while curr.next is not None and curr.key != key:
                curr = curr.next
            if curr.key == key:
                curr.value = value
            return
        else:
            self.storage[index] = LinkedPair(key, value)
# """collisions, check to see if key is none, """"

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            print("Warning: Key not found")
        else:
            self.storage[index] = None

        #hashedkey = self._hash_mod(key)
        # if self.storage[hashedkey] == None:
        #   print('Warning')
        # else:
        #   self.storage[hashedkey] = None
# """check insert, similar to the way insert is handled, current and previous pair """"
    def retrieve(self, key):
        index = self._hash_mod(key)
        pair = self.storage[index]

        if pair is None:
            return None
        else:
            curr = self.storage[index]
            if curr.key == key:
                return curr.value
            while curr is not None:
                if curr.key == key:
                    return curr.value
                else:
                    curr = curr.next
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2

        new_storage = [None] * self.capacity

        for pair in self.storage:
            if pair is not None:
                new_index = self._hash_mod(pair.key)
                new_storage[new_index] = pair
        # for i in [item for item in self.storage if item != None]:
           # new_storage[self._hash_mod(i.key)] = LinkedPair(i.key, i.value)
        self.storage = new_storage
# """ multiply capacity by 2 instead of add """"

#"""check up on function above"""


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

   # (ht.remove("line_3"))
   # (ht.remove("waffles"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
