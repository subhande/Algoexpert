# Non - Constructible Change

"""
Given an array of positive integers representing the values of coins in your
possession, write a function that returns the minimum amount of change (the
minimum sum of money) that you cannot create. The given coins can have any
positive integer value and aren't necessarily unique (i.e., you can have
multiple coins of the same value).
"""

# O(nk) time | O(k) space
def nonConstructibleChange(coins):
    # Write your code here.
    coins = sorted(coins)
    changes = []
    for idx, coin in enumerate(coins):
        if not changes:
            changes.append(coin)
        else:
            new_changes = [coin] + [change+coin for change in changes]
            changes.extend(new_changes)
    changes = sorted(list(set(changes)))
    if changes:
        for i in range(1, changes[-1]+2):
            if i not in changes:
                return i
    return 1

# O(nlogn) time | O(n) space
def nonConstructibleChange(coins):
    currentChangeCreated = 0
    for coin in sorted(coins):
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin
    return currentChangeCreated + 1


if __name__ == "__main__":
    coins = [1, 5, 1, 1, 1, 10, 15, 20, 100]
    expected = 55
    actual = nonConstructibleChange(coins)
    print(f"Expected result: {expected}")
    print(f"Actual result: {actual}")