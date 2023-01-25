# Group Anagrams

"""
Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.

Your function should return a list of anagram groups in no particular order.

# Sample Input
strings = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

# Sample Output
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]

"""

# Time: O(w*n*log(n)) | Space: O(wn) - where w is the number of words and n is the length of the longest word
def groupAnagrams(words):
    anagrams = []
    anagrams_dict = {}
    current_anagram = []
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagrams_dict:
            anagrams_dict[sorted_word] = [word]
        else:
            anagrams_dict[sorted_word] += [word]
    return list(anagrams_dict.values())


if __name__ == "__main__":
    strings = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    print(groupAnagrams(strings))