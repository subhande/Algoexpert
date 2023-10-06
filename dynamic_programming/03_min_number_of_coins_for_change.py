# Min Number Of Coins For Change

"""
Given an array of positive integers representing coin denominations and a single non-negative integer n representing a target amount of money, write a function that returns the smallest number of coins needed to make change for (to sum up to) that target amount using the given coin denominations.

Note that you have access to an unlimited amount of coins. In other words, if the denominations are [1, 5, 10], you have access to an unlimited amount of 1s, 5s, and 10s.

If it's impossible to make change for the target amount, return -1.


Sample Input
n = 7
denoms = [1, 5, 10]

Sample Output
3 // 2x1 + 1x5

Example 1:

Example 1:
$7 [1, 5, 10]

numberOfCoins --> [0, 1, 2, 3, 4, 1, 2, 3]
         [-, -, -, -, -, -, -, -]
         [0, 1, 2, 3, 4, 5, 6, 7]


        DP Formula:
        numberOfCoins[i] = min(numberOfCoins[i], numberOfCoins[i - denom] + 1)


"""

# Time: O(nd) | Space: O(n)
def minNumberOfCoinsForChange(n, denoms):
    numberOfCoins = [float("inf") for _ in range(n+1)]
    numberOfCoins[0] = 0
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount :
                numberOfCoins[amount] = min(numberOfCoins[amount], numberOfCoins[amount-denom]+1)
    return numberOfCoins[n] if numberOfCoins[n] != float("inf") else -1


if __name__ == "__main__":
    n = 7
    denoms = [1, 5, 10]
    print(minNumberOfCoinsForChange(n, denoms))
