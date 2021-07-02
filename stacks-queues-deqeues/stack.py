"""
stack.py
"""

class Stack(object):

    # uses the Python list to construct a stack 
    def __init__(self):
        self.items = []
    
    # returns a boolean that determines if the item is empty
    def isEmpty(self):
        return self.items == []

    # adds a new item on top of the stack   
    def push(self, item):
        self.items.append(item)
    
    # pop() removes and returns last value from the list or the given index value
    def pop(self):
        return self.items.pop()

    # peek() simply checks what the current item is at the top of the stack
    def peek(self):
        return self.items[len(self.items)-1]
    
    # size() checks the length of the stack
    def size(self):
        return len(self.items)

# Testing
s = Stack()
s.push(1)
s.push(2)
print(s.pop())
print(s.peek())
print(s.size())

