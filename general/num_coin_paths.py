"""
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and
pennies (1 cent), write code to calculate the number of ways of representing n cents.
"""

coins = [1, 5, 10, 25]

def num_coins(target_sum):
    if target_sum is None or target_sum < 1:
        return False

    path = []
    explore(target_sum, path, [])
    return len(path)

def explore(target_sum, paths, current_path): 
    if target_sum == 0:
        path = sorted(current_path)
        if path not in paths:
            paths.append(path)
        return
    
    for coin in coins:
        if coin <= target_sum:
            current_path.append(coin)
            explore(target_sum - coin, paths, current_path)
            current_path.remove(coin)
    return


# firt case 
print num_coins(1)
print num_coins(2)
print num_coins(5)
print num_coins(10)
print num_coins(25) 
