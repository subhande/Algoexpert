# Max Sum Increasing subsequence

"""
Write a function that takes in a non-empty array of integers and returns the greatest sum that can be generated from a strictly-increasing subsequence in the array as well as an array of the numbers in that subsequence.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

You can assume that there will only be one increasing subsequence with the greatest sum.

Sample Input
array = [10, 70, 20, 30, 50, 11, 30]

Sample Output
[110, [10, 20, 30, 50]] // The subsequence [10, 20, 30, 50] is strictly increasing and yields the greatest sum: 110.

Explanation:

sums[i] = max(sums[i], sums[j] + array[i]) for all j < i and array[j] < array[i]

array -> [8, 12, 2, 3, 15, 5, 7]
sums ->  [8, 20, 2, 5, 35, 10, 17]
seqs ->  [[8], [8, 12], [2], [2, 3], [8, 12, 15], [2, 3, 5], [2, 3, 5, 7]]
seqsIndexs -> [None, 0, None, 2, 1, 3, 6]

currentNum = array[i]
otherNum = array[j] where 0 <= j < i
if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
    sums[i] = sums[j] + currentNum
    sequences[i] = j

"""

# Solution 1: My solution
# Time: O(n^2) | Space: O(n^2)
def maxSumIncreasingSubsequence(array):
    if len(array) == 1:
        return [array[0], array]
    sums = [float("-inf") for _ in range(len(array) + 1)]
    sums[1] = array[0]
    sques = [[] for _ in range(len(array) + 1)]
    sques[1] = [array[0]]
    for i in range(2, len(array)+1):
        sums[i] = array[i-1]
        sques[i] = [array[i-1]]
        for j in range (1, i):
            if array[j-1] == array[i-1]:
                new_sum = max(sums[i], sums[i]+array[j-1])
                if sums[i] < sums[j] + array[i-1]:
                    sums[i] = new_sum
                    sques[i] = sques[j] + [array[i-1]]
    return [max(sums), sques[sums.index(max(sums))]]


# Solution 2: AlgoExpert solution
# Time: O(n^2) | Space: O(n)
def maxSumIncreasingSubsequence(array):
    sequences = [None for x in array]
    sums = array[:]
    maxSumIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]


def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))
