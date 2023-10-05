# Max Subset Sum No Adjacent

"""
Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array.

If the input array is empty, the function should return 0.

Sample Input
array = [75, 105, 120, 75, 90, 135]

Sample Output
330 // 75 + 120 + 135


Example 1:
arr = [7, 10, 12, 7, 9, 14]

[7, max(7, 10), max(7+12, 10), max(7+12, 10+7, 7+7), 7+12+9, 7+12+9+14]
[7, 10, 19, 19, 28, 33]

DP Formula:

arr[i] = max(arr[i-1], arr[i-2] + arr[i])

"""


# Solution 1
# Time: O(n) | Space: O(n)
def maxSubsetSumNoAdjacent(array):
    maxSums = array[:]
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
    return maxSums[-1]


# Solution 2
# Time: O(n) | Space: O(1)
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first
