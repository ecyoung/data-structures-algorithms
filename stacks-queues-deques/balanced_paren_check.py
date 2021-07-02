"""
balanced_paren_Check.py

Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. Assume that the string doesn’t contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.
"""
sys.path.append(".")

from stack import Stack

def balance_check(s):
    
    # check edge case 
    if len(s) % 2 == 1:
        return False
    
    opening = set("([{")
    matches = set([("(", ")"), ("[", "]"), ("{", "}")])
    
    stack = Stack()
    for paren in s:
        if paren in opening:
            stack.push(paren)
        else:
            if stack.size() == 0:
                return False
            last_open = stack.pop()
            if (last_open, paren) not in matches:
                return False
    return stack.size() == 0
