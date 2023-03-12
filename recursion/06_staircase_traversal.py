# Staircase Traversal

"""
You're given two positive integers representing the height of a staircase and the maximum number of steps that you can advance up the staircase at a time. Write a function that returns the number of ways in which you can climb the staircase.

For example, if you were given a staircase of height = 3 and maxSteps = 2 you could climb the staircase in 3 ways. You could take 1 step, 1 step, then 1 step, you could also take 1 step, then 2 steps, and you could take 2 steps, then 1 step.

Note that maxSteps <= height will always be true.


Sample Input
height = 4
maxSteps = 2

Sample Output
5
// You can climb the staircase in the following ways:
// 1, 1, 1, 1
// 2, 1, 1
// 1, 2, 1
// 1, 1, 2
// 2, 2


"""

"""
if h == 0 or 1:
    return 1
else 
    return rec(-1) + rec(h-2) + ... + rec(h-maxSteps)
"""

# Brute Force Solution: Recursion
def numberOfWaysToTop(height, maxSteps):
    if height <= 1:
        return 1
    numberOfWays = 0
    for i in range(1, min(maxSteps, height) + 1):
        numberOfWays += numberOfWaysToTop(height - i, maxSteps)
    return numberOfWays

# Time: O(k^n) | Space: O(n) - where k is the maxSteps and n is the height of the staircase
def staircaseTraversal(height, maxSteps):
    return numberOfWaysToTop(height, maxSteps)


# Brute Force Solution: Memoization
def numberOfWaysToTop(height, maxSteps, memoize):
    if height in memoize:
        return memoize[height]
    numberOfWays = 0
    for i in range(1, min(maxSteps, height) + 1):
        numberOfWays += numberOfWaysToTop(height - i, maxSteps, memoize)
    memoize[height] = numberOfWays
    return numberOfWays
    

# Time: O(nk) | Space: O(n) - where k is the maxSteps and n is the height of the staircase
def staircaseTraversal(height, maxSteps):
    return numberOfWaysToTop(height, maxSteps, memoize={0: 1, 1: 1})


# Optimal Approach: Dynamic Programming 1
# Time: O(nk) | Space: O(n) - where k is the maxSteps and n is the height of the staircase
def staircaseTraversal(height, maxSteps):
    waysToTop = [0 for _ in range(height + 1)]
    waysToTop[0] = 1
    waysToTop[1] = 1

    for currentHeight in range(2, height + 1):
       step = 1
       while step <= maxSteps and step <= currentHeight:
           waysToTop[currentHeight] += waysToTop[currentHeight - step]
           step += 1
    return waysToTop[height]


# Optimal Approach: Dynamic Programming Memoization (Optimized)
# Time: O(nk) | Space: O(n) - where k is the maxSteps and n is the height of the staircase
def staircaseTraversal(height, maxSteps):
    currentNumberOfWays = 0
    waysToTop = [1]

    for currentHeight in range(1, height + 1):
        startOfWindow = currentHeight - maxSteps - 1
        endOfWindow = currentHeight - 1
        if startOfWindow >= 0:
            currentNumberOfWays -= waysToTop[startOfWindow]
        currentNumberOfWays += waysToTop[endOfWindow]
        waysToTop.append(currentNumberOfWays)

    return waysToTop[height]