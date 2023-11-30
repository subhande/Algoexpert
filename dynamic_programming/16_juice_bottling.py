# Juice Bottling

"""

You're given an array of integers prices of length n with the retail prices of various quantities of juice. Each index in this array corresponds to the price of that amount of juice. For example, prices[2] would be the retail price of 2 units of juice.

You have n - 1 total units of juice. For example, if the length of prices is 5, then you would have 4 total units of juice. Write a function to determine the optimal way to bottle the juice such that it maximizes revenue. 

This function should return a list of all of the juice quantities required in ascending order.

Note that the first value in the prices array will always be 0, because there is no value in no juice. All other values will be positive integers. Additionally, a larger quantity of juice will not always be more expensive than a smaller quantity. For simplicity, all of the test cases only have one possible solution.


Sample Input
prices = [0, 1, 3, 2]


Sample Output
// We have 3 total units of juice
// because the length of the prices is 4
// To maximize revenue, we split the juice into
// quantities of 1 and 2, giving a revenue of 1 + 3 = 4
[1, 2]


"""

# My Solution: Dynamic Programming
# Time: O(n^2) | Space: O(n^2)


def juiceBottling(prices):
    # Write your code here.
    maxRevenue = [0 for _ in range(len(prices))]

    maxRevenue[0] = prices[0]
    maxRevenue[1] = prices[1]
    indexs = [[idx] for idx, _ in enumerate(prices)]
    indexs[1] = [1]

    for i in range(2, len(prices)):
        maxRevenue[i] = prices[i]
        indexs
        for j in range(1, i):
            if maxRevenue[i] < maxRevenue[i - j] + maxRevenue[j]:
                maxRevenue[i] = maxRevenue[i - j] + maxRevenue[j]
                indexs[i] = indexs[i - j] + indexs[j]

    return sorted(indexs[-1])


# Solution 2: Algoexpert Solution

# Time: O(n^2) | Space: O(n^2)


def juiceBottling(prices):
    numSizes = len(prices)
    maxProfit = [0] * numSizes
    solutions = [[]] * numSizes

    for size in range(numSizes):
        for dividingPoint in range(size + 1):
            possibleProfit = prices[dividingPoint] + maxProfit[size - dividingPoint]
            if possibleProfit > maxProfit[size]:
                maxProfit[size] = possibleProfit
                solutions[size] = [dividingPoint] + solutions[size - dividingPoint]

    return solutions[-1]


# Solution 2: Algoexpert Solution

# Time: O(n^2) | Space: O(n)


def juiceBottling(prices):
    numSizes = len(prices)
    maxProfit = [0] * numSizes
    dividingPoints = [0] * numSizes

    for size in range(numSizes):
        for dividingPoint in range(size + 1):
            possibleProfit = prices[dividingPoint] + maxProfit[size - dividingPoint]
            if possibleProfit > maxProfit[size]:
                maxProfit[size] = possibleProfit
                dividingPoints[size] = dividingPoint

    solutions = []
    currentDividingPoint = numSizes-1
    while currentDividingPoint > 0:
        solutions.append(dividingPoints[currentDividingPoint])
        currentDividingPoint -= dividingPoints[currentDividingPoint]


    return solutions