# Longest Common Subsequence

"""
Write a function that takes in two strings and returns their longest common subsequence.

A subsequence of a string is a set of characters that aren't necessarily adjacent in the string but that are in the same order as they appear in the string. For instance, the characters ["a", "c", "d"] form a subsequence of the string "abcd", and so do the characters ["b", "d"]. Note that a single character in a string and the string itself are both valid subsequences of the string.


You can assume that there will only be one longest common subsequence.

Sample Input
str1 = "ZXVVYZW"
str2 = "XKYKZPW"

Sample Output
["X", "Y", "Z", "W"]

Explanation:

    " " "Z" "X" "V" "V" "Y" "Z" "W"
    " "
    "X"
    "K"
    "Y"
    "K"
    "Z"
    "P"
    "W"


"""

# Solution 1


# Time: O(nm*min(n, m)) | Space: O(nm*min(n, m))
def longestCommonSubsequence(str1, str2):
    lcs = [[[] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + [str2[i - 1]]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key=len)

    return lcs[-1][-1]


# Solution 3

# Time: O(nm) | Space: O(nm)
def longestCommonSubsequence(str1, str2):
    lcs = [[[None, 0, None, None] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    # [None (current letter), 0 (length of current lcs), None (previous i), None (previous j)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lcs[i][j] = [str2[i - 1], str[i - 1], str2[i - 1][j - 1], i - 1, j - 1]
            else:
                if len(lcs[i - 1][j]) > len(lcs[i][j - 1]):
                    lcs[i][j] = [None, lcs[i - 1][j], i - 1, j]
                else:
                    lcs[i][j] = [None, lcs[i][j - 1], i, j - 1]

    return buildSequence(lcs)


def buildSequence(lcs):
    sequence = []
    i = len(lcs) - 1
    j = len(lcs[0]) - 1
    while i != 0 and j != 0:
        currentEntry = lcs[i][j]
        if currentEntry[0] is not None:
            sequence.append(currentEntry[0])
        i = currentEntry[3]
        j = currentEntry[4]
    return list(reversed(sequence))


# Solution 2


# Time: O(nm*min(n, m)) | Space: O(min(n, m)^2)
def longestCommonSubsequence(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2

    evenLcs = [[] for x in range(len(small) + 1)]
    oddLcs = [[] for x in range(len(small) + 1)]

    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            currentLcs = oddLcs
            previousLcs = evenLcs
        else:
            currentLcs = evenLcs
            previousLcs = oddLcs
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                currentLcs[j] = previousLcs[j - 1] + [big[i - 1]]
            else:
                currentLcs[j] = max(previousLcs[j], currentLcs[j - 1], key=len)
    return evenLcs[-1] if len(big) % 2 == 0 else oddLcs[-1]


# Solution 4
# Time: O(nm) | Space: O(nm)
def longestCommonSubsequence(str1, str2):
    lengths = [[0 for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lengths[i][j] = lengths[i - 1][j - 1] + 1
            else:
                lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])

    return buildSequence(lengths, str1)


def buildSequence(lengths, string):
    sequence = []
    i = len(lengths) - 1
    j = len(lengths[0]) - 1
    while i != 0 and j != 0:
        if lengths[i][j] == lengths[i - 1][j]:
            i -= 1
        elif lengths[i][j] == lengths[i][j - 1]:
            j -= 1
        else:
            sequence.append(string[j - 1])
            i -= 1
            j -= 1
    return list(reversed(sequence))
