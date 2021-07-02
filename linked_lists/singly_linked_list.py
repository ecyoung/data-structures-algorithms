"""
singly_linked_list.py
Pros:
Linked lists have constant time insertions and deletions in any position. In comparison, arrays require O(n) time to do the same thing. 
Linked lists can continue to expand without having to specify their sizr ahead of time. 
Cons: 
To access an element in a linked list, you need to take O(k) time to go from the head of the list to the kth element. In contrast, arrays have constant time operations to access elements in an array. 
"""

class Node(object):
    
    def __init__(self, value):
        self.value = value 
        self.nextnode = None 

# intialize nodes 
a = Node(1)
b = Node(2)
c = Node(3)

# link nodes 
a.nextnode = b
b.nextnode = c

# testing 
print(a.value)
print(a.nextnode.value)