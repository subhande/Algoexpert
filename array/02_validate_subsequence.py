"""
Validate Subsequence
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.
Sample Input
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
Sample Output
true
Sample Input
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 22, 25, 6, -1, 8, 10, 10]
Sample Output
false
Sample Input
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [22, 25, 6]
Sample Output
true
"""


# Time Complexity: O(n) | Space Complexity: O(n)
def isValidSubsequence(array, sequence):
    pos = 0
    sequence_pos = [False] * len(sequence)
    for i in range(len(array)):
        if pos == len(sequence):
            break
        if array[i] == sequence[pos]:
            sequence_pos[pos] = True
            pos += 1
    return all(sequence_pos)

# Time Complexity: O(n) | Space Complexity: O(1)
def isValidSubsequence(array, sequence):
    pos = 0
    if len(array) < len(sequence):
        return False
    for i in range(len(array)):
        if pos == len(sequence):
            break
        if array[i] == sequence[pos]:
            pos += 1
    return len(sequence) == pos