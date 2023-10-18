# First Non-Reapeating Character

"""
# Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's first non-repeating character.

# The first non-repeating character is the first character in a string that occurs only once.

# If the input string doesn't have any non-repeating characters, your function should return -1.

# Sample Input
# string = "abcdcaf"
# Sample Output
# 1
"""


# Time: O(n) | Space: O(n)
# O(n) time | 0(1) space - where n is the length of the input string The constant space is because the input string only has lowercase 
# English-alphabet letters; thus, our hash table will never have more than 26 character frequencies.
def firstNonRepeatingCharacter(string):
    frequency = {}
    non_repeating_char = ""
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    for k, v in frequency.items():
        if v == 1:
            non_repeating_char = k
            return string.index(non_repeating_char)
    return -1
