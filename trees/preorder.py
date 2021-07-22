"""
preorder.py
"""

def preorder_func(tree):
    if tree:
        print(tree.getRootVal())
        preorder_func(tree.getLeftChild())
        preorder_func(tree.getRightChild())

def preorder_oop(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preorder_oop()
    if self.rightChild:
        self.rightChild.preorder_oop()