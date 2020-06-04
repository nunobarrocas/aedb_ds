from .tad_queue import Queue
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import EmptyQueueException

class ListQueue(Queue):
    def __init__(self):
        self.queue = SinglyLinkedList()

    def is_empty(self):
        return self.queue.is_empty()

    def is_full(self):
        return False

    def size(self):
        return self.queue.size()

    def enqueue(self, element):
        self.queue.insert_last(element)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException()
        return self.queue.remove_first()