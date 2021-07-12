"""
fib_rec.py
"""

# iterative solution
def fib_iter(n):
    a, b = 0, 1
    for i in range(n):
        # tuple unpacking
        a,b = b, a+b
    return a

# testing 
# print(fib_iter(10))

# recursive solution
def fib_rec(n):
    # base case 
    if n == 0 or n == 1:
        return n 
    # recursive case 
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# testing 
# print(fib_rec(10))

# dp solution
# set cache
n = 10
cache = [None]*(n+1)
def fib_dyn(n):
    # base case
    if n == 0 or n == 1:
        return n
    # check cache 
    if cache[n] != None:
        return cache[n]
    # keep setting cache 
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)

    return cache[n]
# testing 
print(fib_dyn(10))