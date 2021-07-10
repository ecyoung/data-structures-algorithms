"""
factorial.py
implement the factorial problem recursively
"""
def fact(n):
    # base case 
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

# testing
print(fact(5)) 