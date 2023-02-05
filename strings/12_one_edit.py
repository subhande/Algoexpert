# One Edit

"""
You're given two strings of lowercase English alphabetic letters. Write a function that returns a boolean representing whether the two strings are one edit away from each other. An edit is defined as one of the following:

Inserting one character anywhere in the string.
Deleting one character from the string.
Substituting one character for another in the string.
Note that you can't add more than one character to a string.

# Sample Input
string1 = "abc"
string2 = "yabc"

# Sample Output
true

"""

def oneEdit(stringOne, stringTwo):
    n = len(stringOne)
    m = len(stringTwo)
    length = min(n, m)

    if abs(n - m) > 1:
        return False

    for i in range(length):
        if stringOne[i] != stringTwo[i]:
            if n == m:
                return stringOne[i+1:] == stringTwo[i+1:]
            elif n < m:
                return stringOne[i:] == stringTwo[i+1:]
            else:
                return stringOne[i+1:] == stringTwo[i:]
    return True

if __name__ == "__main__":
    input__ = ["abc", "yabc"]
    expected_output__ = True
    output = oneEdit(*input__)
    print(output)