"""
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)
would return 2 pairs:

 (1,3)
 (2,2)
 """

 # O(N) - set data structure
def pair_sum(arr, k):
    # edge case
    if len(arr)<2:
        return
    
    # sets for tracking - sets get rid of duplicates 
    seen = set()
    output = set()

    # do a linear scan of the array 
    for num in arr:
        # set target as k - the current element = what you want to search for 
        target = k-num
        # add target if its not recorded in set seen yet
        # note that k = num + target
        if target not in seen:
            seen.add(num)
        # output is a tuple that contains the minimum of num, target and max of num, target
        else:
            # min first then max to order the tuple
            output.add(((min(num,target), max(num, target))))
    
    # map() iterates over all elements of list(output) and makes them strings
    # print("\n".join(map(str,list(output))))

    # returns number of unique pairs that add up to k 
    return len(output)

# testing
# pair_sum([1,3,2,2],4)