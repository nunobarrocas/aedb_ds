from .tad_queue import Queue
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import EmptyQueueException

class ArrayQueue(Queue):
    def __init__(self):
        self.array_queue = SinglyLinkedList()

    def is_empty(self): 
        return self.array_queue.is_empty()

    def is_full(self):
        return False

    def size(self): 
        return self.array_queue.size()

    def enqueue(self, element):
        self.queue.insert_last(element)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException()
        return self.queue.remove_last()