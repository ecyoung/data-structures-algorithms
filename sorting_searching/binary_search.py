"""
binary_search.py
"""
def binary_search(arr, ele):
    # first and last index values 
    first = 0
    last = len(arr) - 1

    found = False

    while first <= last and not found:
        mid = int((first + last) // 2)

        # match found 
        if arr[mid] == ele:
            found = True 
        
        # set new midpoints up or down depending on comparison
        else:
            # set down
            if ele < arr[mid]:
                last = mid - 1
            # set up
            else:
                first = mid + 1
    return found 

def rec_bin_search(arr, ele):
    # base case 
    if len(arr) == 0:
        return False 
    
    else:
        mid = int(len(arr) // 2)

        # if match found 
        if arr[mid] == ele:
            return True 
        else:
            # call again on second half
            if ele < arr[mid]:
                return rec_bin_search(arr[:mid], ele)
            # or call on first half 
            else:
                return rec_bin_search(arr[mid+1:], ele)

# testing 
arr = [1,2,3,4,5,6,7,8,9,10]

print(rec_bin_search(arr,121))