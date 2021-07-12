"""
reverse.py
Reverse a string using recursion
"""

def reverse(s):
    # base case 
    if len(s) == 1:
        return s
    # recursion
    return reverse(s[1:]) + s[0]

print(reverse("hello world"))