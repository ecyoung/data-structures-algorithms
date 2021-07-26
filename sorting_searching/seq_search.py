"""
seq_search.py
"""

def seq_search(arr, ele):
    # start at position 0 
    pos = 0
    # found becomes true if ele is in the list
    found = False

    # go until end of list 
    while pos < len(arr) and not found:

        # if match 
        if arr[pos] == ele:
            found = True 
        
        # else move one down 
        else: 
            pos += 1
    
    return found 

def ordered_seq_search(arr, ele):
    # sequential search for an ordered list 
    # start at position 0 
    pos = 0
    # found becomes true if ele is in the list
    found = False 

    # stop marker 
    stopped = False 

    # go until end of list 
    while pos < len(arr) and not found and not stopped:
        # if match 
        if arr[pos] == ele:
            found = True 
        else:
            # check if element is greater 
            if arr[pos] > ele:
                stopped = True 

            # otherwise move on
            else:
                pos += 1
    return found

# testing 
arr = [1,6,7,44,5,6,2]
print(seq_search(arr,99))