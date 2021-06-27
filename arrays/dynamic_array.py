import ctypes 

# builds python dynamic array from scratch 
class DynamicArray(object):

    def __init__(self):
        # size is 0 by default because the array is empty
        self.n = 0
        # initial capacity is set to 1 element
        self.capacity = 1
        # make_array is a function that will double the capacity of the current array
        self.A = self.make_array(self.capacity)
    
    def __len__(self):
        # returns length of the current array
        return self.n
    
    def __getitem__(self, k):
        # returns element at index k 
        if not 0 <= k < self.n:
            return IndexError("k is out of bounds!")
        
        return self.A[k]

    def append(self, ele):
        # checks if count is equal to capacity
        if self.n == self.capacity:
            self._resize(2*self.capacity) # 2x if capacity isn't enough

        self.A[self.n] = ele
        self.n += 1

    # _ denotes a private method
    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()   

"""
# testing
arr = DynamicArray()
arr.append(1)
arr.append(2)
print(arr[1]) 
"""