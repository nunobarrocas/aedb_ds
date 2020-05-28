from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList
from item import Item

import ctypes

class HashTable(Dictionary):
    def __init__(self, size=101):
        self.array_size = size
        self.num_elements = 0
        self.table = (self.array_size * ctypes.py_object)() #Array of Pointers

        #Create an empty list for each table position
        for i in range(self.size):
            self.table[i] = SinglyLinkedList()        

    def size(self):
        return self.num_elements

    def is_full(self):
        return self.num_elements == self.array_size

    def get(self, k): pass

    def insert(self, k, v):
        idx = self.hash_function(k)
        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                raise DuplicatedKeyException()
        item = Item(k, v)
        self.table[idx].insert_last(item)
        self.num_elements += 1

    def update(self, k, v): pass

    def remove(self, k): pass

    def keys(self): pass

    def values(self): pass

    def items(self): pass

    def hash_function(self, k):
        return sum([ord(c) for c in k])