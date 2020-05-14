<<<<<<< HEAD
from .singly_linked_list import SinglyLinkedList
from .nodes import DoubleListNode
from ..exceptions import InvalidPositionException, EmptyListException
from .doubly_linked_list_iterator import DoublyLinkedListIterator
=======
from .nodes import DoubleListNode
from ..exceptions import EmptyListException, InvalidPositionException
from .doubly_linked_list_iterator import DoublyLinkedListIterator
from .singly_linked_list import SinglyLinkedList
>>>>>>> upstream/develop

class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        self.head = None
        self.tail = None
<<<<<<< HEAD
        self.num_elements = 0

    # Returns true iff the list contains no elements.
    
    def is_empty(self):
        return self.head == None

    # Returns the number of elements in the list.
    
    def size(self):
        return self.num_elements

    # Returns the first element of the list.
    # Throws EmptyListException.
    
    def get_first(self):
        return self.head.get_element()

    # Returns the last element of the list.
    # Throws EmptyListException.
    
    def get_last(self):
        return self.tail.get_element()

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    
    def get(self, position):
        if position >= self.size() or position < 0:
            raise InvalidPositionException("Invalid Position.")
        if position == 0:
            return self.get_first()
        elif position == self.size() - 1:
            return self.get_last()
        current_pos = 1
        current_node = self.head
        while True:            
            current_node = current_node.get_next()
            if current_pos == position:
                return current_node.get_element()
            current_pos +=1

=======
        self.count = 0

    def is_empty(self):
        return self.count == 0

    # Returns the number of elements in the list.
    def size(self):
        return self.count

    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):
        if self.count == 0:
            raise EmptyListException() 
        else:
            return self.head.get_element()

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
        if self.count == 0:
            raise EmptyListException() 
        else:
            return self.tail.get_element()

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):
        if self.size() == 0:
            raise EmptyListException()
        else:
            if position <= int(self.count/2):
                SinglyLinkedList.get(self, position)
            elif position > int(self.count/2):
                current_node = self.tail
                for _ in range(self.count - 1, position - 1, -1):
                    current_node = current_node.get_previous()
                return current_node.get_element()
      
>>>>>>> upstream/develop
    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
<<<<<<< HEAD
    
    def find(self, element):
        if element == self.head.get_element():
            return 0
        elif element == self.tail.get_element():
            return self.size()-1
        position = 1
        current_node = self.head
        while True:
            if position > self.size()-1:
                return -1
            current_node = current_node.get_next()
            if element == current_node.get_element():
                return position
            position +=1

    # Inserts the specified element at the first position in the list.
    
    def insert_first(self, element):        
        new_node = DoubleListNode(element, self.head, None)
        self.head = new_node
        self.tail = self.head       
        self.num_elements +=1

    # Inserts the specified element at the last position in the list.
    
    def insert_last(self, element):
        new_node = DoubleListNode(element, None, self.tail)
        self.tail.set_next(new_node)
        self.tail = new_node
        self.num_elements +=1
=======
    def find(self, element):
        SinglyLinkedList.find(self, element)

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        new_node = DoubleListNode(element, self.head, None)
        self.head.set_previous(new_node)
        self.head = new_node
        if self.count == 0:
            self.tail = new_node
        self.count += 1

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        new_node = DoubleListNode(element, None, self.tail)
        if self.count == 0:
            self.head = new_node
        self.tail.set_next(new_node)    
        self.tail = new_node
        self.count += 1
>>>>>>> upstream/develop

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
<<<<<<< HEAD
    
    def insert(self, element, position):
        if position > self.size() or position < 0:
            raise InvalidPositionException("Invalid Position.")
        if position == 0:
            return self.insert_first(element)
        elif position == self.size():
            return self.insert_last(element)
        current_pos = 1
        current_node=self.head            
        while True:
            previous = current_node            
            current_node = current_node.get_next()
            if current_pos == position:
                new_node = DoubleListNode(element, current_node, previous)
                current_node.set_previous(new_node)
                previous.set_next(new_node)
                self.num_elements +=1
                break       
            current_pos +=1

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    
    def remove_first(self):
        if self.is_empty() == True:
            raise EmptyListException("List is empty.")
        else:
            first_element = self.head.get_element()
            self.head = self.head.get_next()
            self.head.set_previous(None)
            self.num_elements -=1            
            return first_element
            

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    
    def remove_last(self):
        if self.is_empty() == True:
            raise EmptyListException("List is empty.")
        else:
            self.tail = self.tail.get_previous()
            self.tail.set_next(None)
            self.num_elements +=1
=======
    def insert(self, element, position):
        if position not in range(0, self.count):
            raise InvalidPositionException()
        elif not self.count == None:
            if position == 0:
                self.insert_first(element)
            elif position == self.count:
                self.insert_last(element)
            elif position <= int(self.count/2):
                new_node = DoubleListNode(element, None, None)
                previous_node = self.head
                current_node = self.head.get_next()
                for _ in range(0, position-1):
                    previous_node = previous_node.get_next()
                    current_node = current_node.get_next()
                previous_node.set_next(new_node)
                new_node.set_next(current_node)
                current_node.set_previous(new_node)
                new_node.set_previous(previous_node)
                self.count += 1
            elif position > int(self.count/2):
                new_node = DoubleListNode(element, None, None)
                previous_node = self.tail
                current_node = self.tail.get_previous()
                for _ in range(self.tail, position-1. -1):
                    previous_node = previous_node.get_previous()
                    current_node = current_node.get_previous()
                previous_node.set_previous(new_node)
                new_node.set_previous(current_node)
                current_node.set_next(new_node)
                new_node.set_next(previous_node)
                self.count += 1      
        else:
            raise EmptyListException() 

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):
        if self.size() == 0:
            raise EmptyListException()
        if self.count != 0:
            first_node = self.head
            self.head = self.head.get_next()
            first_node.set_next(None)
            self.head.set_previous(None)
            self.count -= 1
            return first_node.get_element()
        if self.count == 1:
            self.make_empty()       


    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        if self.size() == 0:
            raise EmptyListException()    
        if self.count != 0:
            last_node = self.tail
            self.tail = self.tail.get_previous()
            last_node.set_previous(None)
            self.tail.set_next(None)
            self.count -= 1
            return last_node.get_element()
        elif self.count == 1:
            self.make_empty()
>>>>>>> upstream/develop
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
<<<<<<< HEAD
    
    def remove(self, position):
        if position >= self.size() or position < 0:
                raise InvalidPositionException("Invalid Position.")
        if position == 0:
            return self.remove_first()
        elif position == self.size() - 1:
            return self.remove_last()
        current_pos = 1
        current_node = self.head        
        while True:
            previous = current_node            
            current_node = current_node.get_next()
            if current_pos == position:                
                previous.set_next(current_node.get_next())
                current_node.get_next().set_previous(previous)
                self.num_elements -=1
                break
            current_pos +=1
    
    # Removes all elements from the list.
    
    def make_empty(self):
        self.num_elements = 0
        self.head = None
        self.tail = None

    # Returns an iterator of the elements in the list (in proper sequence).
    
    def iterator(self):        
        iterator = DoublyLinkedListIterator(self.tail)        
        while iterator.has_previous() != False:
            elem = iterator.previous()
            print(elem)
=======
    def remove(self, position):
        if self.size() == 0:
            raise InvalidPositionException()
        elif self.count == 1:
            self.make_empty()
        elif self.count != 0:
            if position == 0:
                return self.remove_first()
            elif position == self.count - 1:
                return self.remove_last()
            elif position <= int(self.count/2):
                selected_node = self.head
                selected_node = selected_node.get_next()
                current_node = self.head
                for _ in range(0, position - 1):
                    selected_node = selected_node.get_next()
                    current_node = current_node.get_next()
                current_node.set_next(selected_node.get_next())
                selected_node.get_next().set_previous(current_node)
                selected_node.set_next(None)
                selected_node.set_previous(None)
                self.count -= 1
                return selected_node.get_element()
            elif position > int(self.count/2):
                selected_node = self.tail
                selected_node = selected_node.get_previous()
                current_node = self.tail
                for _ in range(self.count - 1, position - 1, -1):
                    selected_node = selected_node.get_previous()
                    current_node = current_node.get_previous()
                current_node.set_previous(selected_node.get_previous())
                selected_node.get_preivous().set_next(current_node)    
                selected_node.set_next(None)
                selected_node.set_previous(None)
                self.count -= 1
                return selected_node.get_element()

    # Removes all elements from the list.
    def make_empty(self):
        SinglyLinkedList.make_empty(self)

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self):
        if self.size() == 0:
            raise EmptyListException()
        else:               
            iterator = DoublyLinkedListIterator(self.head, self.tail)
            return iterator
>>>>>>> upstream/develop
