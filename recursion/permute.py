"""
permute.py
Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.
For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
Note: If a character is repeated, treat each occurence as distinct, for example an input of 'xxx' would return a list with 6 "versions" of 'xxx'
"""

def permute(s):

    out = []

    # base case 
    if len(s) == 1:
        out = [s]
    else:
        # for every letter in string 
        for i, let in enumerate(s):
            # for every permutation resulting from step 2 and 3
            for perm in permute(s[:i] + s[i+1:]):
                # add it to the output
                out += [let + perm]
    return out