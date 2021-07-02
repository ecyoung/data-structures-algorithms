"""
balanced_paren_Check.py
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
