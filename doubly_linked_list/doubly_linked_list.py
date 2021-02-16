"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, new_next):
        self.next = new_next
    
    def set_prev(self, new_prev):
        self.prev = new_prev


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
        
        # if DLL is empty
        if self.length == 0:
            # set head and tail to the new node instance
            self.head = current
            self.tail = current
        # if DLL is not empty
        else:
            # set new node's next to current head
            current.set_next(self.head)
            # set head's prev to new node
            self.head.set_prev(current)
            # set head to the new node
            self.head = current
        # increment the DLL length attribute
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        return self.delete(self.head)
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance of ListNode with value
        current = ListNode(value)
        
        # if DLL is empty
        if self.length == 0:
            # set head and tail to the new node instance
            self.head = current
            self.tail = current
        # if DLL is not empty
        else:
            # set new node's prev to current tail
            current.set_prev(self.tail)
            # set tail's next to new node
            self.tail.set_next(current)
            # set tail to the new node
            self.tail = current

        # increment the DLL length attribute
        self.length += 1           
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        return self.delete(self.tail)
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.get_value())

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.get_value())


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        elif node.get_prev() is None:
            self.head = node.get_next()
            self.head.set_prev(None)
        elif node.get_next() is None:
            self.tail = node.get_prev()
            self.tail.set_next(None)
        else:
            prev_node = node.get_prev()
            next_node = node.get_next()
            prev_node.set_next(node.get_next)
            next_node.set_prev(node.get_prev)
        self.length -= 1
        return node.get_value()

        
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max = self.head.get_value()
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
            if current.get_value() > max:
                max = current.get_value()
        return max