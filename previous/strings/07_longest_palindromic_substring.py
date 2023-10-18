# Longest Palindromic Substring

"""
Write a function that takes in a string and returns the longest palindromic substring.

A palindromic substring is defined as a substring that is written the same forward and backward. Note that single-character strings are palindromes.

You can assume that there will only be one longest palindromic substring.
"""

# Time: O(n^2) | Space: O(n) - where n is the length of the input string

# Time: O(n^3) | Space: O(1) - where n is the length of the input string
def longestPalindromicSubstring(string):
    window_size = len(string)
    n = len(string)
    for w in list(reversed(range(2, window_size+1))):
        for i in range(0, n-w+1):
            if string[i:i+w] == string[i:i+w][::-1]:
                return string[i:i+w]
    return string[0]

if __name__ == "__main__":
    string = "abaxyzzyxf"
    print(longestPalindromicSubstring(string))
