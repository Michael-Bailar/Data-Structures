"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        old_self = self
        if self.prev:
            self.prev = None
        if self.value:
            self.value = None
        if self.next:
            self.next = None
        return old_self.value
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create instance of ListNode with value
        current = ListNode(value)
        # increment the DLL length attribute
        self.length = self.length + 1
        # if DLL is empty
        if self.length == 1:
            # set head and tail to the new node instance
            self.head = current
            self.tail = current
        # if DLL is not empty
        else:
            # set new node's next to current head
            current.next = self.head
            # set head's prev to new node
            self.prev = current
            # set head to the new node
            self.head = current
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store the value of the head
        old_head = self.head
        # decrement the length of the DLL
        self.length = self.length - 1
        # delete the head
        
        # if head.next is not None
        if self.head.next:
            # set head.next's prev to None
            self.head.prev = None
            # set head to head.next
            self.head = old_head.next
        # else (if head.next is None)
        else:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None

        # return the value
        return self.tail
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance of ListNode with value
        current = ListNode(value)
        # increment the DLL length attribute
        self.length = self.length + 1
        # if DLL is empty
        if self.length == 1:
            # set head and tail to the new node instance
            self.head = current
            self.tail = current
        # if DLL is not empty
        if self.length > 1:
            # set new node's prev to current tail
            current.prev = self.tail
            # set tail's next to new node
            self.next = current
            # set tail to the new node
            self.tail = current

            
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # store the value of the tail
        old_tail = self.tail
        # decrement the length of the DLL
        self.length = self.length - 1
        # delete the tail
        # if tail.prev is not None
        if self.tail.prev:
            # set tail.prev's next to None
            self.tail.prev = None
            # set tail to tail.prev
            self.tail = self.tail.prev
        # else (if tail.prev is None)
        else:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None

        # return the value
        return old_tail.value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        node.next = self.head
        self.head = node
        node.prev = None

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.head:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        if node.next is self.tail:
            self.tail.next = node
        node.next = None
        node.prev = self.tail
        self.tail = node


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass