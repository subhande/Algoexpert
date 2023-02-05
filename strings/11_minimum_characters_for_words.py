# Minimum Characters for Words

"""
Write a function that takes in an array of words and returns the smallest array of characters needed to form all of the words. The characters don't need to be in any particular order. For example, given the array of words ["this", "that", "did", "deed", "them!", "a"], your function should return ["t", "t", "h", "i", "s", "a", "d", "d", "e", "m", "!"].

Note that you can always generate the input words by concatenating together the characters returned by your function.

# Sample Input

words = ["this", "that", "did", "deed", "them!", "a"]

# Sample Output

["t", "t", "h", "i", "s", "a", "d", "d", "e", "m", "!"]

"""
# Time: O(n * i) | Space: O(c) - where n is the number of words, i is the length of the longest word, and c is the number of unique characters across all words
def minimumCharactersForWords(words):
    character_dict = {}
    for word in words:
        current_word_character_dict = {}
        for character in word:
            if character not in current_word_character_dict:
                current_word_character_dict[character] = 1
            else:
                current_word_character_dict[character] += 1
        for k, v in current_word_character_dict.items():
            if k not in character_dict:
                character_dict[k] = v
            else:
                character_dict[k] = max(character_dict[k], v)
    min_characters = []
    for k, v in character_dict.items():
        min_characters += [k] * v
    return min_characters


if __name__ == "__main__":
    input__ = ["this", "that", "did", "deed", "them!", "a"]
    expected_output__ = ["t", "t", "h", "i", "s", "a", "d", "d", "e", "m", "!"]
    output = minimumCharactersForWords(input__)
    print(output)