#  Zero Sum Subarray

"""
You're given a list of integers nums. Write a function that returns true if there exists a subarray whose sum is equal to 0, and false otherwise.

Constraints

n ≤ 100,000 where n is the length of nums

"""
# Time: O(n) | Space: O(n)
def zeroSumSubarray(nums):
    sums = set([0])
    currentSum = 0
    for num in nums:
        currentSum += num
        if currentSum in sums:
            return True
        sums.add(currentSum)
    return False