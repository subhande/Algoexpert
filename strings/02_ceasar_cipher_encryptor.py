# Ceasar Cipher Encryptor

"""
Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key.

Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by one returns the letter "a".

Sample Input
string = "xyz"
key = 2
Sample Output
"zab"

"""

# Time: O(n) | Space: O(n)
def caesarCipherEncryptor(string, key):
    new_string = ""
    for s in string:
        digit = ord(s) + key
        if digit > ord('z'):
            digit = 96 + (digit - ord('z')) % 26
        new_string += chr(digit)
    return new_string


if __name__ == "__main__":
    print(caesarCipherEncryptor("ovmqkwtujqmfkao", 52))