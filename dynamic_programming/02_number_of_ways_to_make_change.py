# Number Of Ways To Make Change

"""
Given an array of positive integers representing coin denominations and a single non-negative integer n representing a target amount of money, write a function that returns the number of ways to make change for that target amount using the given coin denominations.

Note that an unlimited amount of coins is at your disposal.


Sample Input
n = 6
denoms = [1, 5]

Sample Output
2 // 1x1 + 1x5 and 6x1

Example 1:
$6 [5, 1]

[0, 1, 2, 3, 4, 5, 6]
0 -> 0
1 -> 1
2 -> 1 * 2 -> 1
3 -> 1 * 3 -> 1
4 -> 1 * 4 -> 1
5 -> 1 * 5 | 5 * 1 -> 2
6 -> 1 * 5 + 1 * 1 | 1 * 6 -> 2

Example 2:
$10 [1, 5, 10, 25]

ways --> [1, 1, 1, 1, 1, 2, 2, 2, 2, 2,  4]
         [-, -, -, -, -, -, -, -, -, -, --]
         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


        DP Formula:
        ways[i] = ways[i] + ways[i - denom]

"""

# Solution 1
# Time: O(n*d) | Space: O(n)
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for _ in range(n+1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] = ways[amount] + ways[amount-denom]
    return ways[n]

if __name__ == "__main__":
    n = 10
    denoms = [1, 5, 10, 25]
    print(numberOfWaysToMakeChange(n, denoms))    
