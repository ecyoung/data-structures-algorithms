"""
rec_coin.py
Implement a Fibonnaci Sequence in three different ways:

Recursively
Dynamically (Using Memoization to store results)
Iteratively
"""

def rec_coin(target, coins):
    min_coins = target
    # base case 
    if target in coins:
        return 1
    else:
        # for every coin value that is <= my target
        for i in [c for c in coins if c <= target]: 
            num_coins = 1 + rec_coin(target-i, coins)
            # reset minimum if the new num_coins less than min_coins
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

def rec_coin_dynam(target, coins, known_results):

    # default output to target
    min_coins = target

    # base case 
    if target in coins:
        known_results[target] = 2
        return 1
    # return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    
    else:
        # for every coin value that is <= taget
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin_dynam(target-i, coins, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                # reset that known result 
                known_results[target] = min_coins
    return min_coins