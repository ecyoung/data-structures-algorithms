"""
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
Output:

5 is the missing number
"""

# O(n^2) because of nested for loop for zip()
def finder1(arr1, arr2):
    # sort the arrays
    arr1.sort()
    arr2.sort()

    # zip() pairs together the corresponding indices of two arrays and puts them in a tuple
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    # in the edge case the missing number is the last element of arr1
    return arr1[-1]

# we use collections for hash table implementation
import collections 

# this is O(n log n)
def finder2(arr1, arr2):
    # this dictionary automatically adds in the key if the key doesn't already exist 
    d = collections.defaultdict(int)

    # adds all elements of arr2 to the dictionary
    for num in arr2:
        d[num] += 1
    # checks if there isn't an element of arr1 that is already in the dictionary
    for num in arr1:
        if d[num] == 0:
            return num
        # this handles duplicates 
        else:
            d[num] -= 1

# O(n)
# XOR - outputs true when only one is true 
def finder3(arr1, arr2):
    result = 0

    # perform an XOR between the numbers in the arrays (concatenated) 
    for num in arr1+arr2:
        result^=num
        print(result) 
    return result 