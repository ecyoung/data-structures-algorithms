"""
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
"""

def compress(s):
    # store into dictionary 
    compress_dict = {}
    for letter in s: 
        if letter not in compress_dict:
            compress_dict[letter] = 1
        else:
            compress_dict[letter] += 1
    key_lst = []
    for i in compress_dict.keys():
        key_lst.append(i)
    
    val_lst = []
    for i in compress_dict.values():
        val_lst.append(i)
    
    output = ""
    for i in range(len(key_lst)):
        output += (str(key_lst[i]))
        output += (str(val_lst[i]))
    return output

# testing 
print(compress('AAAAABBBBCCCC'))
