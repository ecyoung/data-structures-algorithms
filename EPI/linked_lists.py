# linked list class
class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

# search for a key | O(n)
def search_list(L, key):
    while L != None and L.data != key:
        L = L.next
    return L

# insert a new node after a specified node | O(1)
def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

# delete a node | O(1)
def delete_after(node):
    node.next = node.next.next

# merge two sorted lists 
def merge_two_sorted_lists(L1, L2):
    # creates a placeholder for the result
    dummyHead = tail = ListNode()
    while L1 != None and L2 != None:
        if L1.data <= L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
    # appends the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummyHead.next

# reverse a single sublist | O(f)
def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next
    # reverses sublist 
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
    return dummy_head.next

def main():
    L0 = ListNode(0)
    L1 = ListNode(1)
    L2 = ListNode(2)
    L3 = ListNode(3)
    L0.next = L1
    L1.next = L2
    L2.next = L3
    L4 = ListNode(4)
    insert_after(L1, L4)
    print(search_list(L0, 4))

if __name__ == "__main__":
    main()