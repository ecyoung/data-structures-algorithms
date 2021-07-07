"""
linked_list_reversal.py

Since we want to do this in place we want to make the function operate in O(1) space, meaning we don't want to create a new list, so we will simply use the current nodes. Time wise, we can perform the reversal in O(n).
We can reverse the list by changing the next pointer of each node. Each node's next pointer should point to the previous node.
In one pass from head to tail of our input list, we will point each node's next pointer to the previous element. 
Make sure to copy current.nextnode into nextnode before setting current.nextnode to previous. 
"""

class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None 

def reverse(head):
    # Set up current, previous, and next nodes
    current = head 
    previous = None 
    nextnode = None 

    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current 
        current = nextnode

    return previous
# Testing 
# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

# Before reversal
print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

# Call reverse
reverse(a)

# After reversal
print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)

