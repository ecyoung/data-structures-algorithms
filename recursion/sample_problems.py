"""
sample_problems.py
"""
# problem 1
def rec_sum(n):
    # base case 
    if n == 0:
        return 0
    # recursive case 
    else:
        return n + rec_sum(n-1)

# testing
# print(rec_sum(4))

# problem 2
def sum_func(n):
    if len(str(n)) == 1:
        return n
    else: 
        return n % 10 + sum_func(n / 10)

# problem 3
def word_split(phrase, list_of_words, output = None):
    if output is None: 
        output = []
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)
    return output