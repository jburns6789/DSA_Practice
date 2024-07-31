def find_first_duplicate(my_list):
    seen = set()
    for element in my_list:
        if element in seen:
            return element
        seen.add(element)
    return None


my_list = [2, 5, 1, 2, 3, 5, 1, 2, 4]
first_duplicate = find_first_duplicate(my_list)
print(first_duplicate)

# Using a dictionary

num_dict = {}

for index, num in enumerate(my_list):
    if num in num_dict:
        print({num})
        break
    else:
        num_dict[num] = index
else:
    print("no duplicates found")


# In Python, a set is an unordered collection of unique elements. Unlike lists or tuples, sets
# do not allow duplicate values. This makes them useful for situations where you want to store
# a collection of items and automatically eliminate duplicates.

# Hash tables, hash maps, unordered maps, dictionaries, objects(internally mapped as a dictionary)
# dictionaries are ordered in python
# HAVE TO KNOW!!!

# "key": "value"  <---- hash function implemented
# SHA-256 HASH Generator idempotent same input in a function always outputs the same output
# used in cryptography
# REALLY FAST data access

# collisions are when two key value pairs are inserted in the same address space in memory,
# turns into a linked list, can't avoid, with increased data and decreased memory collision occurs
# if you continue to add to the same memory space to reduce access and insert speed
# slows down to O(n/k) k is the size of the table
# many ways to resolve collisions, this is the main downside

# https://www.miraclesalad.com/webtools/md5.php
# https://www.cs.usfca.edu/~galles/visualization/OpenHash.html

# insert O(1)
# lookup O(1)
# delete O(1)
# search O(1)

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key: # <---- first item set
                item[1] = value # <---- second item set
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return
        raise KeyError(key)


# Usage example:
ht = HashTable()
ht.insert("name", "Alice")
ht.insert("age", 30)
print(ht.get("name"))  # Output: Alice
ht.remove("name")
# ht.get("name")  # This would raise a KeyError

