"""
Given an array of integers (positive and negative) find the largest continuous sum.
"""

def large_cont_sum(arr):
    # edge case when the array is empty 
    if len(arr)==0:
        return 0 
    # we initialize our max sum and current sum to the first element of the array
    max_sum = current_sum = arr[0]
    # rest of elements in array
    for num in arr[1:]:
        # comparing what we have so far with the next number 
        current_sum = max(current_sum+num, num)
        # comparing the current sum and the max sum that we have kept track of 
        max_sum = max(current_sum, max_sum)
    
    return max_sum