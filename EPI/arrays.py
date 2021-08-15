# O(n) time | O(1) space
def even_odd(A):
    next_even = 0
    next_odd = len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A

# O(n) time | O(1) space
def dutch_flag_partition(pivot_idx, arr):
    pivot = arr[pivot_idx]
    # group elements smaller than array
    smaller = 0
    for i in range(len(arr)):
        if arr[i] < pivot:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller += 1
    # group elements larger than array
    larger = len(arr) - 1
    for i in reversed(range(len(arr))):
        if arr[i] > pivot:
            arr[i], arr[larger] = arr[larger], arr[i]
            larger -= 1
    return arr

def main():
    A = [10, 4, 5, 6, 3, 2, 9, 4]
    print(dutch_flag_partition(3, A))

if __name__ =="__main__":
    main()