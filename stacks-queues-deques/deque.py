"""
deque.py
"""


class Deque(object):

    # Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque 
    def __init__(self):
        self.items = []
    
    # isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value. 
    def isEmpty(self):
        return self.items == []
    
    # addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.
    def addFront(self, item):
        self.items.append(item)
    
    # addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing. 
    def addRear(self, item):
        self.items.insert(0, item)

    # removeFront() removes the front item from the deque. It needs no paramters and returns the item. The deque is modified. 
    def removeFront(self):
        return self.items.pop()

    # removeRear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified. 
    def removeRear(self):
        return self.items.pop(0)
    
    # size() returns the number of items in the deque. It needs no parameters and returns an integer. 
    def size(self):
        return len(self.items)

# Testing 

d = Deque()
d.addFront("Hello")
d.addRear("World")
print(d.size())
print(d.removeFront() + " " + d.removeRear())
print(d.isEmpty())